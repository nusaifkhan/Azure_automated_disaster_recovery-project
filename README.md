# Azure Automated Disaster Recovery Project

## Overview
The **Azure Automated Disaster Recovery** project provides a streamlined solution for organizations to prepare for and recover from unexpected failures in their Azure cloud infrastructure. It ensures minimal downtime by automating the disaster recovery process, making it ideal for businesses focused on reliability and business continuity.

## What It Solves
Cloud environments are prone to unforeseen disruptions such as hardware failures, software bugs, or misconfigurations. Manually recovering cloud resources can be complex and time-consuming. This project addresses these challenges by:
- Automating backup creation and recovery operations for virtual machines (VMs).
- Monitoring resource integrity and resolving failures with minimal human intervention.
- Providing clear reports on backups and recovery operations for effective auditing and troubleshooting.

## Features
- **Automated Backups**: Regular snapshot creation for Azure VMs to ensure data protection.
- **Disaster Simulation**: A testing mechanism to simulate failures and validate recovery processes.
- **VM Recovery Automation**: Quickly restores VM states using pre-configured snapshots.
- **Integrity Checks**: Validates resource consistency and ensures recovery readiness.
- **Comprehensive Reporting**: Generates detailed logs and summaries for all backup and recovery tasks.

---

## Installation Guide

### Prerequisites
Before you begin, ensure you have:
- **Python 3.x** installed.
- An **Azure account** with permissions to manage resources (e.g., VM operations).
- **Azure CLI** installed and configured.
- Git installed on your system.

### Steps to Install
**Clone the Repository**:
```bash
   git clone https://github.com/nusaifkhan/Azure_automated_disaster_recovery-project.git
   cd Azure_automated_disaster_recovery-project

```
### Set Up a Virtual Environment: Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### Install Dependencies: Use pip to install the required Python libraries:
```bash
pip install -r requirements.txt
```

### Configure Azure CLI: Ensure you're authenticated to Azure:
```bash
az login
```
## Set Up Configuration Files
- **Edit `config/settings.json`** to include necessary Azure resource details.
- *(Optional)* Add your credentials to `azure_auth.py` if custom authentication is needed.

---

## Usage Guide

### Backup Creation
Run the following script to back up VMs:
```bash
bash scripts/backup.sh
```
## Disaster Simulation
Simulate a VM failure and trigger recovery operations:
```bash
bash scripts/disaster_test.sh
```

## Automated VM Recovery
**Recover a failed VM using snapshots:**
```bash
bash scripts/recover_vm.sh
```

## Run Unit Tests
**Verify the integrity of the system:**
```bash
python -m unittest discover tests/
```

```
File Structure
Azure-Automated-Disaster-Recovery/
├── config/                # Configuration files
├── python_scripts/        # Python scripts for core functionalities
├── reports/               # Backup and recovery reports
├── scripts/               # Shell scripts for automation
├── tests/                 # Unit test files
├── README.md              # Documentation
├── requirements.txt       # Dependencies list
└── .gitignore             # Ignored files
```

## Contributing
**Contributions are welcome! If you want to improve the project, please: Fork the repository.**
**Create a feature branch.**
**Submit a pull request with your changes.**

## License
**This project is licensed under the MIT License, allowing free and open use of the codebase.**

## Contact
**Created by Nusaif Khan.**
## For questions or feedback:
## Email: nusaifkhan21@gmail.com
## GitHub: @https://github.com/nusaifkhan


