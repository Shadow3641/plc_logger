# -----------------------------
# PLC Logger Configuration
# -----------------------------

# PLC Connection
PLC_IP = "192.168.1.10"               # Replace with your PLC IP
TAGS_TO_READ = ["Motor_Status_UDT", "Drive_Parameters_UDT", "Line_Pressure"]  # Tags to monitor
CRITICAL_TAGS = ["Motor_Status_UDT", "Drive_Parameters_UDT"]                    # Tags that trigger critical alerts

# Logging
LOG_FILE = "logs/plc_udt_log.csv"     # CSV log file location
LOG_INTERVAL = 5                      # Seconds between PLC reads

# Alerts
MAX_RETRIES = 3                        # Number of retries before a critical alert
RECONNECT_DELAY = 10                   # Seconds to wait after communication error
RANGE_ALERTS = {"Line_Pressure": (30, None)}  # Min/Max thresholds for range alerts
ALERT_THROTTLE_MINUTES = 30            # Minimum minutes between repeated alerts

# Daily Summary
DAILY_SUMMARY_HOUR = 18                # 24-hour format, hour to send summary email

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"         # SMTP server
SMTP_PORT = 587                        # SMTP port
EMAIL_USER = "your_email@gmail.com"    # Your email
EMAIL_PASSWORD = "your_email_password" # Your email password (replace with secure method)
EMAIL_TO = ["recipient@example.com"]   # List of recipients

# Logs folder
LOGS_FOLDER = "logs"
