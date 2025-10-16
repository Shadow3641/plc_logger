# main.py
"""
Main program for PLC Logger.

- Reads tags from the PLC
- Logs data to CSV
- Generates charts and HTML summaries
- Sends range-based alerts using the configured email method (SMTP or Outlook)
"""

import time
import datetime
from config import LOG_INTERVAL, TAGS
from plc_comm import read_tags
from logger import log_data
from charts import generate_charts
from html_summary import generate_html_summary
from alerts import check_range_alerts  # updated alerts module

def main():
    """
    Main loop for PLC logger.
    Continuously reads PLC data, logs it, generates charts/HTML, and sends alerts.
    """
    print("[INFO] Starting PLC Logger...")
    while True:
        try:
            # --- Step 1: Read PLC tags ---
            tag_data = read_tags(TAGS)
            timestamp = datetime.datetime.now()
            print(f"[INFO] Tags read at {timestamp}: {tag_data}")

            # --- Step 2: Log data to CSV ---
            log_data(tag_data, timestamp)

            # --- Step 3: Generate charts ---
            generate_charts()  # updates charts with latest data

            # --- Step 4: Generate HTML summary ---
            generate_html_summary()  # updates HTML report

            # --- Step 5: Check for range-based critical alerts ---
            check_range_alerts(tag_data)  # sends emails if values out of range

            # --- Step 6: Wait for next interval ---
            time.sleep(LOG_INTERVAL)

        except KeyboardInterrupt:
            print("[INFO] Logger stopped by user.")
            break
        except Exception as e:
            print(f"[ERROR] Exception in main loop: {e}")
            time.sleep(LOG_INTERVAL)  # wait before retrying

if __name__ == "__main__":
    main()
