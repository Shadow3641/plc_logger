"""
config_template.py

Template configuration for PLC Logger.
Do NOT put passwords or sensitive info here.
Copy this file to config.py and fill in your server-specific settings.
"""

# -----------------------------
# PLC Connection Settings
# -----------------------------
PLC_IP = "192.168.1.10"            # PLC IP address
PLC_RACK = 0                        # PLC Rack (Allen-Bradley)
PLC_SLOT = 1                        # PLC Slot (Allen-Bradley)

# -----------------------------
# Logging Settings
# -----------------------------
LOG_INTERVAL = 5                     # Time between PLC reads in seconds
LOG_FILE = "logs/PLC_log.csv"        # CSV file to store logged data

# -----------------------------
# Alert Settings
# -----------------------------
ENABLE_ALERTS = True                 # Enable/disable range alerts
ENABLE_PDF_ALERTS = True             # Generate PDF alerts instead of emails
ENABLE_HTML_SUMMARY = True           # Generate HTML summary reports
EMAIL_METHOD = "SMTP"                # Email method: SMTP or OUTLOOK
ALERT_TAGS = {                        # Tags to monitor for range alerts
    "Pressure_Transmitter": (30, None),
    "Motor_Temperature": (None, 100),
    "Flow_Rate": (50, 200),
}

# -----------------------------
# Shift / Reporting Settings
# -----------------------------
SHIFT_REPORT_INTERVAL = 12            # Hours per shift to generate reports
GENERATE_CHARTS = True                # Enable/disable charts in shift report
GENERATE_PDF_REPORT = True            # Generate PDF shift report
GENERATE_HTML_REPORT = True           # Generate HTML summary at shift end

# -----------------------------
# Email Settings (Optional)
# -----------------------------
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "user@example.com"
SMTP_PASSWORD = "password"
EMAIL_FROM = "plclogger@example.com"
EMAIL_TO = ["tech1@example.com", "tech2@example.com"]