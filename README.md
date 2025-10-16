# PLC Logger

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Shadow3641/plc_logger?style=social)](https://github.com/Shadow3641/plc_logger/stargazers)

**Modular PLC Logger for Rockwell Logix PLCs**

---

## **Quick Start**

1. Install Python 3.8+  

2. Install required libraries: `pip install pylogix pandas matplotlib`

3. Configure PLC connection, tags, and email settings in `config.py`.  

4. Run the logger: `python main.py`

- Logs and charts will appear in `logs/`  
- Critical alerts and daily summaries are emailed automatically  

---

## **Features**

- Supports multiple mills and multiple PLCs  
- Fully modular structure for easy maintenance and expansion  
- Logs timestamps consistently using a utility module  
- Handles CRITICAL_TAGS and RANGE_ALERTS with email notifications  
- Generates trend charts automatically, with old files cleaned up  
- Daily HTML summary reports sent via email  
- Fully commented and optimized for readability and maintainability  

---

## **Folder Structure**

PLC_Logger/

├── config.py # Configuration variables (PLC IP, tags, thresholds, email)

├── main.py # Main loop tying all modules together

├── plc_comm.py # PLC communication and UDT flattening

├── alerts.py # Critical and range alerts

├── logger.py # CSV logging

├── charts.py # Trend chart generation

├── html_summary.py # HTML report generation

├── email_utils.py # Sending emails

├── utils.py # Helper functions

├── logs/ # Folder for CSV logs and PNG charts

├── README.md # Project overview

└── .gitignore # Files/folders excluded from Git

yaml
Copy code

---

## **Installation**

1. Install Python 3.8+  

2. Install required libraries: `pip install pylogix pandas matplotlib`

3. Configure your PLC connection, tags, and email settings in `config.py`.  

---

## **Usage**

Run the main loop: `python main.py`

- Data will be logged automatically at the interval defined in `config.py`.  
- Critical tag failures or range alerts will trigger email notifications.  
- Daily HTML summaries with trend charts will be sent via email.  

---

## **License**

This project is licensed under the **GNU General Public License v3 (GPL-3.0)**. See [LICENSE](LICENSE) for details.

---

## **Contributing**

- Add new PLCs, tags, or alert rules by updating `config.py`.  
- Add new modules for additional functionality in a modular fashion.  
- Follow the existing commenting style for readability.  

---

## **Contact**

Developed by **Shadow3641**  
For support, suggestions, or improvements, create an issue or pull request on GitHub.
