# PLC Logger

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Shadow3641/plc_logger?style=social)](https://github.com/Shadow3641/plc_logger/stargazers)

**Modular PLC Logger for Logix/Allen-Bradley PLCs**  

This Python-based logger reads PLC tags, logs data, generates charts, creates HTML summaries, and sends range-based alerts via **SMTP or Outlook**. The project is modular, allowing easy maintenance and future enhancements.

---

## Features

- Read PLC tags using Allen-Bradley / Logix protocols  
- Log data to CSV files (`logs` folder)  
- Generate charts (`charts` folder) and HTML summaries (`logs` folder)  
- Range-based alerts for critical tags  
- Email alerts via **SMTP** or **Outlook**  
- Modular, maintainable code structure:
  - `main.py` — program entry point  
  - `plc_comm.py` — PLC communication  
  - `logger.py` — logging data to CSV  
  - `alerts.py` — email alerts and range checking  
  - `charts.py` — generate charts  
  - `html_summary.py` — generate HTML reports  
  - `email_outlook.py` — Outlook-specific email logic  
  - `utils.py` — helper functions  

---

## Configuration

1. Copy `config_template.py` to `config.py`.  
2. Replace placeholder values with your **PLC IP, tag names, logging intervals, and email settings**.  
3. Ensure sensitive information like passwords and IPs remain **in `config.py`**, which is ignored in GitHub.  

---

## Range Alerts

Set thresholds in `config.py`:

```python
# Format: "Tag_Name": (Lower_Limit, Upper_Limit)
RANGE_ALERTS = {
    "Pressure_Transmitter": (30, None),
    "Motor_Temperature": (None, 100),
    "Flow_Rate": (50, 200),
}```
Lower or upper limits can be set to None if not applicable.

Alerts are triggered when a tag value goes out of range.

## Running Locally (Python)

1. Ensure Python 3.x is installed.
2. Install dependencies (if any).
3. Run: `python main.py`

## Building a Server-Ready Executable (.exe)

If Python is not installed on the server, you can create a standalone `.exe` using PyInstaller.

### Step 1: Install PyInstaller
`pip install pyinstaller`

### Step 2: Prepare your project

- Make sure all modules (main.py, plc_comm.py, alerts.py, etc.) are in the project folder.

- Ensure config.py and config_template.py exist.

### Step 3: Use the build script

We provide a ready-to-use PowerShell script build_server_exe.ps1:

`build_server_exe.ps1`


- Cleans previous builds

- Uses hooks to include all local modules automatically

- Ensures logs and charts folders exist

- Generates `plc_logger.exe` in `dist`

### Step 4: Deploy on server

1. Copy plc_logger.exe to server folder.

2. Copy your local config.py with PLC credentials.

3. Run:

`plc_logger.exe`


No Python installation is required. The .exe is fully plug-and-play.

## GitHub Safety Notes

- Never commit config.py — it contains sensitive information.

- Always commit config_template.py to provide safe defaults for collaborators.

- Logs, charts, and templates are included in .exe builds automatically.

## **Folder Structure**

plc_logger/
│
├─ main.py                  # Program entry point
├─ plc_comm.py              # PLC communication
├─ logger.py                # Logging to CSV
├─ alerts.py                # Range-based alerts & email
├─ charts.py                # Chart generation
├─ html_summary.py          # HTML summary reports
├─ email_outlook.py         # Outlook email support
├─ utils.py                 # Helper functions
├─ config.py                # Local config with credentials (ignored in GitHub)
├─ config_template.py       # Template config for reference
├─ logs/                    # Log CSV files (created automatically)
├─ charts/                  # Generated chart images (created automatically)
├─ hooks/                   # PyInstaller hooks for auto-including modules
└─ build_server_exe.ps1     # PowerShell script to build standalone .exe

## Workflow Diagram

+-------------------+
|     PLC Tags      |
+--------+----------+
         |
         v
+-------------------+
|  plc_comm.py      |
|  (Read Tags)      |
+--------+----------+
         |
         v
+-------------------+
|  logger.py        |
|  (Write CSV)      |
+--------+----------+
         |
         v
+-------------------+
|  charts.py        |
|  (Generate Charts)|
+--------+----------+
         |
         v
+-------------------+
| html_summary.py   |
| (HTML Reports)    |
+--------+----------+
         |
         v
+-------------------+
| alerts.py         |
| (Email Alerts)    |
+-------------------+
         |
   +-----+-----+
   |           |
   v           v
SMTP         Outlook

## **License**

This project is licensed under the **GNU General Public License v3 (GPL-3.0)**. See [LICENSE](LICENSE) for details.


## **Contributing**

- Add new modules for additional functionality in a modular fashion.  
- Follow the existing commenting style for readability.  


## **Contact**

Developed by **Shadow3641**  
For support, suggestions, or improvements, create an issue or pull request on GitHub.
