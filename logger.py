import csv
import os
from config import LOG_FILE

def ensure_csv_header(flat_keys):
    """
    Ensures that the CSV file exists and has a header row.

    Parameters:
        flat_keys : list of str
            List of all flattened tag names to include in the CSV header.

    Behavior:
        - Creates the CSV file if it doesn't exist.
        - Writes a header row: 'Timestamp' + all tag keys.
        - If file exists, does nothing (preserves existing data).
    """
    # Check if the file already exists
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            # Header row: Timestamp + all flattened tag names
            writer.writerow(["Timestamp"] + flat_keys)
        print(f"✅ Created new log file with header: {LOG_FILE}")


def log_row(row):
    """
    Appends a row of PLC data to the CSV log file.

    Parameters:
        row : list
            A list of values corresponding to the CSV header.
            The first value should always be a timestamp string.

    Behavior:
        - Opens the CSV file in append mode.
        - Writes the row.
        - Handles newlines automatically (cross-platform).
    """
    try:
        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(row)
    except Exception as e:
        # Log any error during writing (you may also write to a separate error log)
        print(f"⚠️ Failed to write to log file {LOG_FILE}: {e}")
