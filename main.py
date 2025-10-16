import time
from pylogix import PLC
from datetime import datetime

# Import custom modules
from config import TAGS_TO_READ, LOG_INTERVAL, DAILY_SUMMARY_HOUR, CRITICAL_TAGS, RECONNECT_DELAY
from plc_comm import flatten_udt, read_tag
from logger import ensure_csv_header, log_row
from alerts import check_critical, check_range
from html_summary import generate_daily_summary
from email_utils import send_email
from utils import format_timestamp, dict_to_row, cleanup_old_files

def main():
    """
    Main loop for the modular PLC logger.

    Features:
        - Reads tags (including UDTs) from the PLC
        - Logs data to CSV with dynamic headers
        - Checks CRITICAL_TAGS and RANGE_ALERTS
        - Sends immediate alert emails
        - Generates daily HTML summary with charts
        - Cleans old chart files automatically
        - Runs continuously at LOG_INTERVAL seconds
    """
    # Clean old chart PNGs (older than 7 days) to save space
    cleanup_old_files(folder="logs", days=7, extension=".png")

    # Create a PLC connection
    comm = PLC()
    comm.IPAddress = "192.168.1.10"  # Could also be imported from config

    # --- Determine CSV header from initial read ---
    flat_keys_set = set()
    with comm:
        for tag in TAGS_TO_READ:
            status, value = read_tag(comm, tag)
            if status == "Success":
                flat_keys_set.update(flatten_udt(tag, value).keys())
            else:
                flat_keys_set.add(tag)

    flat_keys = sorted(flat_keys_set)
    ensure_csv_header(flat_keys)

    # Track last daily summary date to avoid multiple sends
    last_summary_date = datetime.now().date()

    while True:
        row_dict = {}
        now = datetime.now()

        try:
            # --- Read all tags from PLC ---
            with comm:
                for tag in TAGS_TO_READ:
                    status, value = read_tag(comm, tag)
                    if status == "Success":
                        row_dict.update(flatten_udt(tag, value))
                        if tag in CRITICAL_TAGS:
                            check_critical(tag, success=True)
                    else:
                        row_dict[tag] = "Error"
                        if tag in CRITICAL_TAGS:
                            check_critical(tag, success=False)

            # --- Check RANGE_ALERTS ---
            for tag, value in row_dict.items():
                check_range(tag, value)

            # --- Log CSV ---
            row = [format_timestamp()] + dict_to_row(flat_keys, row_dict)
            log_row(row)

            # --- Daily HTML summary ---
            if now.hour == DAILY_SUMMARY_HOUR and last_summary_date != now.date():
                html_body, charts = generate_daily_summary()
                send_email(f"Daily PLC Summary {now:%Y-%m-%d}", html_body, attachments=charts, html=True)
                last_summary_date = now.date()

        except Exception as e:
            print(f"⚠️ PLC communication or script error: {e}")
            time.sleep(RECONNECT_DELAY)
            continue

        # Wait until next read cycle
        time.sleep(LOG_INTERVAL)

if __name__ == "__main__":
    print("Starting optimized modular PLC logger...")
    main()
