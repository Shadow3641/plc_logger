"""
html_summary.py - Generate HTML summary reports
-----------------------------------------------
Creates a simple HTML summary table for PLC tag data.
Accepts a DataFrame for shift-based reporting.
"""

import os
from jinja2 import Template

def generate_html_summary(df, html_dir="logs"):
    """
    Generates an HTML summary for the provided DataFrame.

    Args:
        df (DataFrame): PLC tag data with timestamps
        html_dir (str): Folder to save HTML summary
    """
    os.makedirs(html_dir, exist_ok=True)

    # Simple Jinja2 HTML template
    html_template = """
    <html>
    <head><title>Shift Summary Report</title></head>
    <body>
        <h2>Shift Summary Report: {{ start_time }} - {{ end_time }}</h2>
        <table border="1" cellpadding="5" cellspacing="0">
            <tr>
                <th>Timestamp</th>
                {% for tag in tags %}
                <th>{{ tag }}</th>
                {% endfor %}
            </tr>
            {% for row in data %}
            <tr>
                <td>{{ row.timestamp }}</td>
                {% for tag in tags %}
                <td>{{ row[tag] }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """

    template = Template(html_template)

    # Prepare data for template
    data_rows = df.to_dict(orient="records")
    html_content = template.render(
        start_time=df["timestamp"].iloc[0],
        end_time=df["timestamp"].iloc[-1],
        tags=df.columns[1:],  # Skip timestamp
        data=data_rows
    )

    # Save HTML file
    filename = os.path.join(html_dir, f"shift_summary_{df['timestamp'].iloc[0].strftime('%Y%m%d_%H%M')}.html")
    with open(filename, "w") as f:
        f.write(html_content)
