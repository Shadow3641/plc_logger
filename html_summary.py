import pandas as pd
from config import LOG_FILE, CRITICAL_TAGS, RANGE_ALERTS
from charts import generate_udt_charts

def generate_daily_summary():
    """
    Generates a daily HTML summary of the latest PLC values with charts.

    Features:
        - Displays the most recent value for each tag
        - Highlights CRITICAL_TAGS in red
        - Highlights values out of RANGE_ALERTS in orange
        - Generates charts for all tags and returns file paths
        - Returns HTML string and list of chart files for email attachments

    Returns:
        html_body : str
            HTML-formatted table of latest values
        chart_files : list of str
            List of PNG chart file paths
    """
    # Generate charts first and get the file paths
    chart_files = generate_udt_charts()

    # Read CSV log into pandas DataFrame
    try:
        df = pd.read_csv(LOG_FILE, parse_dates=['Timestamp'])
    except FileNotFoundError:
        return "<p>No log file found for summary.</p>", chart_files

    if df.empty:
        return "<p>Log file is empty.</p>", chart_files

    # Use the last row as the latest values
    last_row = df.iloc[-1]

    # Start HTML table
    html_body = "<html><body>"
    html_body += "<h2>Daily PLC Summary</h2>"
    html_body += "<table border='1' cellpadding='5' cellspacing='0'>"
    html_body += "<tr><th>Tag</th><th>Value</th></tr>"

    for tag in last_row.index:
        if tag == "Timestamp":
            continue

        value = last_row[tag]

        # Default color is black
        color = "black"

        # Highlight CRITICAL_TAGS in red
        if tag in CRITICAL_TAGS:
            color = "red"

        # Highlight out-of-range values in orange
        elif tag in RANGE_ALERTS:
            min_val, max_val = RANGE_ALERTS[tag]
            try:
                num = float(value)
                if (min_val is not None and num < min_val) or (max_val is not None and num > max_val):
                    color = "orange"
            except (ValueError, TypeError):
                pass  # keep default color if value not numeric

        html_body += f"<tr><td>{tag}</td><td style='color:{color}'>{value}</td></tr>"

    html_body += "</table>"
    html_body += "<p>Charts are attached separately.</p>"
    html_body += "</body></html>"

    return html_body, chart_files
