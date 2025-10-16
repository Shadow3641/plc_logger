# config_template.py
"""
Template configuration file for PLC Logger

- Use this file as a starting point for creating your local config.py
- Replace placeholder values with actual PLC, email, and logging settings
"""

# --- PLC Configuration ---
PLC_IP = "PLC_IP_ADDRESS_HERE"  # Example: "192.168.0.10"
TAGS = ["Pressure_Transmitter", "Motor_Temperature", "Flow_Rate"]

# --- Logging Configuration ---
LOG_INTERVAL = 5  # seconds between reads
LOG_PATH = "logs"
CHART_PATH = "charts"
HTML_PATH = "logs"

# --- Email Configuration ---
EMAIL_METHOD = "OUTLOOK"  # Options: "SMTP" or "OUTLOOK"
EMAIL_TO = ["recipient@example.com"]

# SMTP example (optional)
SMTP_SERVER = "SMTP_SERVER_HERE"
SMTP_PORT = 587
EMAIL_USER = "YOUR_EMAIL_HERE"
EMAIL_PASSWORD = "YOUR_PASSWORD_HERE"

# --- Range Alerts Configuration ---
# Format: "Tag_Name": (Lower_Limit, Upper_Limit)
# Use None if no limit for that side
RANGE_ALERTS = {
    "Pressure_Transmitter": (30, None),
    "Motor_Temperature": (None, 100),
    "Flow_Rate": (50, 200),
    # Add more tags as needed
}

# --- Optional: Paths for templates or configs ---
CONFIG_TEMPLATE_PATH = "config_template.py"
