"""
Generates PDF reports with charts and alert summaries.
Combines the previous pdf_report.py and HTML summary functionality.
"""

import os
from fpdf import FPDF
import pandas as pd
import config
from datetime import datetime

PDF_FOLDER = config.PDF_REPORT_FOLDER
os.makedirs(PDF_FOLDER, exist_ok=True)

def generate_shift_report():
    """
    Generate end-of-shift PDF report including:
    - All tag logs for the shift
    - Alerts triggered during the shift
    - Charts (if any)
    """
    pdf_file = os.path.join(PDF_FOLDER, f"shift_report_{datetime.now().strftime('%Y-%m-%d_%H%M')}.pdf")
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "End-of-Shift Report", 0, 1, "C")
    
    # Insert shift log data
    pdf.set_font("Arial", "", 12)
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join("logs", f"{today}.csv")
    if os.path.exists(log_file):
        df = pd.read_csv(log_file)
        pdf.cell(0, 10, f"Tag logs for {today}", 0, 1)
        for _, row in df.iterrows():
            line = ", ".join([f"{col}: {row[col]}" for col in df.columns])
            pdf.multi_cell(0, 8, line)
    
    # Placeholder for chart images
    charts_folder = "charts"
    if os.path.exists(charts_folder):
        for file in os.listdir(charts_folder):
            if file.endswith(".png"):
                pdf.add_page()
                pdf.image(os.path.join(charts_folder, file), w=180)
    
    pdf.output(pdf_file)
