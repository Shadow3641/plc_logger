import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from config import SMTP_SERVER, SMTP_PORT, EMAIL_USER, EMAIL_PASSWORD, EMAIL_TO
import os

def send_email(subject, body, attachments=None, html=False):
    """
    Sends an email with optional HTML content and attachments.

    Parameters:
        subject : str
            The subject line of the email.
        body : str
            The main content of the email. Can be plain text or HTML.
        attachments : list of str, optional
            File paths to attach to the email. Defaults to None.
        html : bool
            If True, send body as HTML; otherwise, plain text.

    Behavior:
        - Connects to the SMTP server using credentials from config.py
        - Creates a multipart email to handle attachments
        - Sends the email to all recipients defined in EMAIL_TO
        - Handles exceptions and prints errors to console
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = ", ".join(EMAIL_TO)
        msg['Subject'] = subject

        # Attach the main body (HTML or plain text)
        if html:
            msg.attach(MIMEText(body, 'html'))
        else:
            msg.attach(MIMEText(body, 'plain'))

        # Attach files if provided
        if attachments:
            for file_path in attachments:
                if os.path.exists(file_path):
                    with open(file_path, "rb") as f:
                        part = MIMEApplication(f.read(), Name=os.path.basename(file_path))
                        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
                        msg.attach(part)
                else:
                    print(f"⚠️ Attachment not found: {file_path}")

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure connection
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USER, EMAIL_TO, msg.as_string())

        print(f"✅ Email sent: {subject}")

    except Exception as e:
        print(f"⚠️ Failed to send email '{subject}': {e}")
