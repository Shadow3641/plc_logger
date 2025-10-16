import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from config import LOG_FILE, RANGE_ALERTS, LOGS_FOLDER
from utils import cleanup_old_files

def generate_udt_charts():
    """
    Generates trend charts for tags in the CSV log file.

    Features:
        - Cleans old chart files before generating new ones
        - Creates one chart per tag
        - Plots historical values over time
        - Highlights out-of-range areas based on RANGE_ALERTS
        - Saves each chart as a PNG in the logs folder

    Returns:
        chart_files : list of str
            File paths of all generated PNG charts
    """
    chart_files = []

    # Delete old PNGs older than 7 days to save disk space
    cleanup_old_files(LOGS_FOLDER, days=7, extension=".png")

    # Check if log file exists
    if not os.path.exists(LOG_FILE):
        print(f"⚠️ Log file not found: {LOG_FILE}")
        return chart_files

    # Read CSV log into pandas DataFrame
    df = pd.read_csv(LOG_FILE, parse_dates=['Timestamp'])

    # Iterate through all columns except Timestamp
    for tag in df.columns:
        if tag == "Timestamp":
            continue

        df[tag] = pd.to_numeric(df[tag], errors='coerce')

        plt.figure(figsize=(10, 4))
        plt.plot(df['Timestamp'], df[tag], label=tag, color='blue', marker='o', markersize=3)

        # Highlight RANGE_ALERTS if applicable
        if tag in RANGE_ALERTS:
            min_val, max_val = RANGE_ALERTS[tag]
            if min_val is not None:
                plt.axhline(min_val, color='red', linestyle='--', label='Min Threshold')
            if max_val is not None:
                plt.axhline(max_val, color='orange', linestyle='--', label='Max Threshold')

        plt.title(f"{tag} Trend")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.legend()
        plt.grid(True)

        # Save chart PNG in logs folder
        chart_file = os.path.join(LOGS_FOLDER, f"{tag}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        plt.tight_layout()
        plt.savefig(chart_file)
        plt.close()

        chart_files.append(chart_file)

    return chart_files
