# alerts.py
"""
Alerts module for PLC logger.

- Checks tags against defined ranges
- Sends email notifications using configured method (Outlook or SMTP)
"""

from config import RANGE_ALERTS, EMAIL_TO, EMAIL_METHOD
from email_outlook import send_email as send_email_outlook
# from email_smtp import send_email as send_email_smtp  # Optional SMTP support

def check_range_alerts(tag_data):
    """
    Check all critical tags against configured ranges.
    Sends alerts if a value falls outside its defined range.
    
    Parameters:
        tag_data (dict): Dictionary of {tag_name: value} from PLC read
    """
    for tag_name, (low, high) in RANGE_ALERTS.items():
        value = tag_data.get(tag_name)
        if value is None:
            continue

        alert_triggered = False
        if low is not None and value < low:
            alert_triggered = True
        if high is not None and value > high:
            alert_triggered = True

        if alert_triggered:
            subject = f"[ALERT] {tag_name} Out of Range"
            body = f"Tag: {tag_name}\nCurrent Value: {value}\nAllowed Range: {low} - {high}"

            if EMAIL_METHOD.upper() == "OUTLOOK":
                send_email_outlook(subject, body, EMAIL_TO)
            # elif EMAIL_METHOD.upper() == "SMTP":
            #     send_email_smtp(subject, body, EMAIL_TO)
            else:
                print(f"[WARNING] Unknown email method '{EMAIL_METHOD}'. Email not sent.")
