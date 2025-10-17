"""
Generates charts from CSV logs for inclusion in PDF reports.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

CHART_FOLDER = "charts"
os.makedirs(CHART_FOLDER, exist_ok=True)

def generate_charts():
    """
    Generate charts for all logged tags in today's CSV.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join("logs", f"{today}.csv")
    if not os.path.exists(log_file):
        return

    df = pd.read_csv(log_file, parse_dates=["Timestamp"])
    for tag in df.columns:
        if tag == "Timestamp":
            continue
        plt.figure()
        plt.plot(df["Timestamp"], df[tag], label=tag)
        plt.xlabel("Time")
        plt.ylabel(tag)
        plt.title(f"{tag} over time")
        plt.legend()
        plt.tight_layout()
        chart_path = os.path.join(CHART_FOLDER, f"{tag}_{today}.png")
        plt.savefig(chart_path)
        plt.close()
