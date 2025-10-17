"""
Handles range-based alerts and PDF/email report triggers.
Can send emails or generate PDF reports for shift-based workflow.
"""

import os
import time
from datetime import datetime
import config
from report_pdf import generate_shift_report

# Keep track of last alert per tag for cooldown
last_alert_time = {}

def check_alerts(tag_values):
    """
    Check each tag value against configured RANGE_ALERTS.
    If EMAIL_ENABLED is True, send immediate alerts with cooldown.
    Otherwise, just log alerts for end-of-shift PDF.
    """
    alerts_triggered = []

    for tag, value in tag_values.items():
        if tag not in config.RANGE_ALERTS or value is None:
            continue
        
        low, high = config.RANGE_ALERTS[tag]
        alert_needed = False
        if low is not None and value < low:
            alert_needed = True
        if high is not None and value > high:
            alert_needed = True

        if alert_needed:
            now = time.time()
            last_time = last_alert_time.get(tag, 0)
            if config.EMAIL_ENABLED and now - last_time >= config.EMAIL_COOLDOWN:
                # Send immediate email alert
                send_email_alert(tag, value)
                last_alert_time[tag] = now
            
            # Add alert to end-of-shift report
            alerts_triggered.append((tag, value, datetime.now()))
    
    return alerts_triggered

def send_email_alert(tag, value):
    """
    Dispatch an email alert using the selected method.
    """
    if config.EMAIL_METHOD.upper() == "SMTP":
        from email_smtp import send_smtp_alert
        send_smtp_alert(tag, value)
    elif config.EMAIL_METHOD.upper() == "OUTLOOK":
        from email_outlook import send_outlook_alert
        send_outlook_alert(tag, value)

def shift_report_if_needed():
    """
    Check if current time is shift end and generate PDF report.
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if current_time in config.SHIFT_START_TIMES:
        generate_shift_report()
