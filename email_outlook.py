"""
Handles sending email alerts using Microsoft Outlook.
"""

import win32com.client as win32
import config

def send_outlook_alert(tag, value):
    """
    Send an email via Outlook for a single alert.
    """
    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.To = ";".join(config.EMAIL_TO)
    mail.Subject = f"PLC ALERT: {tag}"
    mail.Body = f"Alert: {tag} value {value} out of range"
    mail.Send()
