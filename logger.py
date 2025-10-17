"""
Handles logging tag values to CSV.
Supports appending data to daily log files.
"""

import os
import pandas as pd
from datetime import datetime
import config

LOG_FOLDER = "logs"
os.makedirs(LOG_FOLDER, exist_ok=True)

def log_data(tag_values):
    """
    Append PLC tag values to CSV.
    Each day gets its own CSV file.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join(LOG_FOLDER, f"{today}.csv")
    
    # Prepare row with timestamp and tag values
    row = {"Timestamp": datetime.now()}
    row.update(tag_values)
    
    # Append to CSV
    df = pd.DataFrame([row])
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, mode='w', header=True, index=False)
