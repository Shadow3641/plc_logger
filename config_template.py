"""
config_template.py

Template configuration for PLC Logger.
Copy this file to config.py and fill in your own details.
Sensitive values should remain ONLY in config.py (ignored by GitHub).
"""

# --- PLC CONNECTION SETTINGS ---
PLC_IP = "192.168.1.10"
PLC_TAGS = ["Pressure_Transmitter", "Motor_Temperature", "Flow_Rate"]

# --- LOGGING SETTINGS ---
LOG_INTERVAL = 5
LOG_DIR = "logs"
CHARTS_DIR = "charts"

# --- ALERT SETTINGS ---
RANGE_ALERTS = {
    "Pressure_Transmitter": (30, None),
    "Motor_Temperature": (None, 100),
    "Flow_Rate": (50, 200),
}

# --- EMAIL SETTINGS ---
# Available methods:
#   "smtp"   → use email_smtp.py (default)
#   "outlook" → use email_outlook.py for Outlook integration
EMAIL_METHOD = "smtp"

# --- SMTP CONFIGURATION (if using EMAIL_METHOD = "smtp") ---
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
SMTP_USERNAME = "youremail@domain.com"
SMTP_PASSWORD = "yourpassword"
EMAIL_RECIPIENTS = ["alerts@domain.com"]

# --- OUTLOOK CONFIGURATION (if using EMAIL_METHOD = "outlook") ---
OUTLOOK_SENDER = "youremail@domain.com"
OUTLOOK_RECIPIENTS = ["alerts@domain.com"]
OUTLOOK_SUBJECT_PREFIX = "[PLC ALERT]"
