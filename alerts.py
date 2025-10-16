from datetime import datetime, timedelta
from email_utils import send_email
from config import CRITICAL_TAGS, RANGE_ALERTS, MAX_RETRIES, ALERT_THROTTLE_MINUTES

# Initialize retry counters for each critical tag
retry_counters = {tag: 0 for tag in CRITICAL_TAGS}

# Track the last alert timestamp for each tag to throttle repeated emails
last_alert_time = {tag: datetime.min for tag in set(CRITICAL_TAGS) | set(RANGE_ALERTS.keys())}


def check_critical(tag, success):
    """
    Handles CRITICAL_TAGS retry logic and sends alert emails if necessary.

    Parameters:
        tag : str
            The name of the tag being monitored.
        success : bool
            True if the tag read was successful, False if there was an error.

    Behavior:
        - If a critical tag fails, increment the retry counter.
        - When retries exceed MAX_RETRIES, send an email alert (throttled by ALERT_THROTTLE_MINUTES).
        - Resets the counter after success or after sending an alert.
    """
    now = datetime.now()

    if success:
        # Successful read: reset retry counter
        retry_counters[tag] = 0
    else:
        # Failed read: increment retry counter
        retry_counters[tag] += 1

        # If retries exceed threshold, send alert email (if not throttled)
        if retry_counters[tag] >= MAX_RETRIES:
            if now - last_alert_time[tag] > timedelta(minutes=ALERT_THROTTLE_MINUTES):
                subject = f"PLC Alert: Critical Tag '{tag}' failed"
                body = f"The critical tag '{tag}' failed {MAX_RETRIES} consecutive times at {now}"
                send_email(subject, body)
                last_alert_time[tag] = now  # Update last alert timestamp
            # Reset retry counter regardless after sending alert
            retry_counters[tag] = 0


def check_range(tag, value):
    """
    Checks RANGE_ALERTS for out-of-range values and sends alert emails (throttled).

    Parameters:
        tag : str
            The name of the tag to check.
        value : any
            The current value of the tag.

    Behavior:
        - If the tag has defined min/max thresholds, compare value.
        - If value is out of range and last alert was more than ALERT_THROTTLE_MINUTES ago, send email.
        - Skips check if value is None, Error, or cannot be converted to float.
    """
    now = datetime.now()

    # Only check tags that have range thresholds defined
    if tag in RANGE_ALERTS:
        min_val, max_val = RANGE_ALERTS[tag]

        # Skip if value is missing or not numeric
        if value in (None, "", "Error"):
            return

        try:
            num = float(value)
        except ValueError:
            return  # Cannot convert value to float, skip

        # Determine if out of range
        out_of_range = (min_val is not None and num < min_val) or (max_val is not None and num > max_val)

        # Send email if out of range and throttling allows
        if out_of_range and (now - last_alert_time[tag] > timedelta(minutes=ALERT_THROTTLE_MINUTES)):
            subject = f"PLC Alert: {tag} out of range"
            body = f"The tag '{tag}' has a value of {num} at {now}, which is outside the allowed range ({min_val}-{max_val})"
            send_email(subject, body)
            last_alert_time[tag] = now  # Update last alert timestamp
