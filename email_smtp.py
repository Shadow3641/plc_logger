"""
Handles sending email alerts via SMTP.
"""

import smtplib
from email.message import EmailMessage
import config

def send_smtp_alert(tag, value):
    """
    Send an email using SMTP for a single alert.
    """
    msg = EmailMessage()
    msg["Subject"] = f"PLC ALERT: {tag}"
    msg["From"] = config.EMAIL_FROM
    msg["To"] = ", ".join(config.EMAIL_TO)
    msg.set_content(f"Alert: {tag} value {value} out of range")

    with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
        server.starttls()
        server.login(config.SMTP_USER, config.SMTP_PASS)
        server.send_message(msg)
