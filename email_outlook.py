# email_outlook.py
# Sends emails using Outlook Desktop via COM Automation
# Requires pywin32 (pip install pywin32)

import win32com.client as win32

def send_email(subject, body, recipients):
    """
    Sends an email using Outlook Desktop via COM Automation.

    Parameters:
        subject (str): Email subject line
        body (str): Email body (plain text)
        recipients (list of str): List of email addresses
    """
    try:
        # Initialize Outlook application
        outlook = win32.Dispatch('Outlook.Application')
        mail = outlook.CreateItem(0)  # 0 = olMailItem

        # Set email subject and body
        mail.Subject = subject
        mail.Body = body  # for plain text emails
        # mail.HTMLBody = body  # uncomment to send HTML emails

        # Add recipients
        for recipient in recipients:
            mail.Recipients.Add(recipient)

        # Send the email
        mail.Send()
        print(f"[INFO] Email sent via Outlook to: {', '.join(recipients)}")
    except Exception as e:
        print(f"[ERROR] Failed to send email via Outlook: {e}")
