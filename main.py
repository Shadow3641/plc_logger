"""
Main entry point for plc_logger.
Handles loop, logging, alerts, shift-based PDF reports, and chart generation.
"""

import time
import plc_comm
import logger
import alerts
import charts
import config

def main():
    """
    Main loop:
    - Read PLC tags at configured interval
    - Log data
    - Check alerts
    - Generate charts
    - Generate end-of-shift report
    """
    while True:
        tag_values = plc_comm.read_tags()
        logger.log_data(tag_values)
        alerts.check_alerts(tag_values)

        # Shift report
        alerts.shift_report_if_needed()

        # Generate charts for end-of-shift PDF
        charts.generate_charts()

        time.sleep(config.PLC_LOG_INTERVAL)

if __name__ == "__main__":
    main()
