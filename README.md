# PLC Logger

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Shadow3641/plc_logger?style=social)](https://github.com/Shadow3641/plc_logger/stargazers)

**Modular PLC Logger for Logix/Allen-Bradley PLCs**  

This Python-based logger reads PLC tags, logs data, generates charts, creates PDF shift reports, and sends range-based alerts via **SMTP or Outlook**. The project is modular, allowing easy maintenance and future enhancements.

---

## Features

- Read PLC tags using Allen-Bradley / Logix protocols  
- Log data to CSV files (`logs` folder)  
- Generate charts (`charts` folder)  
- Range-based alerts for critical tags  
- PDF end-of-shift reports (`reports` folder)  
- Email alerts via **SMTP** or **Outlook**  
- Modular, maintainable code structure:
  - `main.py` — program entry point  
  - `plc_comm.py` — PLC communication  
  - `logger.py` — logging data to CSV  
  - `alerts.py` — alert handling and email  
  - `charts.py` — generate charts  
  - `report_pdf.py` — generate PDF shift reports  
  - `email_outlook.py` — Outlook-specific email logic  
  - `email_smtp.py` — SMTP-specific email logic  
  - `utils.py` — helper functions  

---

## Configuration

1. Copy `config_template.py` to `config.py`.  
2. Replace placeholder values with your **PLC IP, tag names, logging intervals, email settings, and shift times**.  
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
}
```
Lower or upper limits can be set to `None` if not applicable. Alerts are triggered when a tag value goes out of range.  

---

## Running Locally (Python)

1. Ensure Python 3.x is installed.  
2. Install dependencies:

```bash
pip install pylogix pandas matplotlib numpy jinja2 fpdf pywin32
```
3. Run:

```bash
python main.py
```

---

## Server Deployment (.exe)

If Python is not installed on the server:

### Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

### Step 2: Prepare your project

- Ensure all modules (`main.py`, `plc_comm.py`, `alerts.py`, etc.) are in the project folder.  
- Include `config.py` with credentials (ignored in GitHub).  

### Step 3: Use the build script

Run `build_server_exe.ps1`:

```powershell
# This script builds plc_logger.exe
.\build_server_exe.ps1
```

- Cleans previous builds  
- Includes all modules automatically  
- Ensures `logs` and `charts` folders exist  
- Generates `plc_logger.exe` in `dist`  

### Step 4: Deploy

1. Copy `plc_logger.exe` to the server folder.  
2. Copy your local `config.py`.  
3. Run `plc_logger.exe`.  

No Python installation is required. The .exe is fully plug-and-play.  

---

## Alerts & Reports

- If **email is enabled**, alerts are sent immediately with a configurable cooldown.  
- If **email is disabled**, alerts are compiled into the end-of-shift PDF report.  
- End-of-shift reports include charts, all alerts, and summary data for the shift.  

---

## Folder Structure

```markdown
plc_logger/
│
├─ main.py                  # Program entry point
├─ plc_comm.py              # PLC communication
├─ logger.py                # Logging to CSV
├─ alerts.py                # Alerts & email handling
├─ charts.py                # Chart generation
├─ report_pdf.py            # Shift-based PDF reports
├─ email_smtp.py            # SMTP email support
├─ email_outlook.py         # Outlook email support
├─ utils.py                 # Helper functions
├─ config.py                # Local config (ignored in GitHub)
├─ config_template.py       # Template config for reference
├─ logs/                    # Log CSV files
├─ charts/                  # Generated chart images
├─ reports/                 # Shift PDF reports
├─ hooks/                   # PyInstaller hooks
└─ build_server_exe.ps1     # PowerShell script to build standalone .exe
```

---

## Workflow Overview 🚀

The PLC Logger follows a structured, modular workflow. Each step is represented with badges for clarity.

| Step | Module             | Action                                | Status |
|------|------------------|--------------------------------------|--------|
| 1    | `plc_comm.py`     | Read PLC tags                         | ![Step1](https://img.shields.io/badge/Step-1-blue) |
| 2    | `logger.py`       | Write data to CSV                     | ![Step2](https://img.shields.io/badge/Step-2-green) |
| 3    | `charts.py`       | Generate charts                       | ![Step3](https://img.shields.io/badge/Step-3-orange) |
| 4    | `report_pdf.py`   | Generate end-of-shift PDF report      | ![Step4](https://img.shields.io/badge/Step-4-red) |
| 5    | `alerts.py`       | Send email alerts (if enabled)       | ![Step5](https://img.shields.io/badge/Step-5-purple) |

**Legend:**
- ![Step1](https://img.shields.io/badge/Step-1-blue) — PLC communication  
- ![Step2](https://img.shields.io/badge/Step-2-green) — Data logging  
- ![Step3](https://img.shields.io/badge/Step-3-orange) — Charts generation  
- ![Step4](https://img.shields.io/badge/Step-4-red) — PDF report creation  
- ![Step5](https://img.shields.io/badge/Step-5-purple) — Alerts & notifications  

> ⚡ Each step is modular, so you can extend or modify individual components without affecting others.

---

## GitHub Safety Notes

- Never commit `config.py` — contains credentials.  
- Always commit `config_template.py` for reference.  
- `logs/`, `charts/`, and `reports/` are ignored in GitHub.  

---

## License

This project is licensed under **GNU GPL v3**. See [LICENSE](LICENSE) for details.  

---

## Contributing

- Add modules in a modular fashion.  
- Follow existing commenting style.  

---

## Contact

Developed by **Shadow3641**  
For support, suggestions, or improvements, create an issue or pull request on GitHub.
