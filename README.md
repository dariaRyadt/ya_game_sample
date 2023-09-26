# ya_game_sample
Yandex Game sample test framework

# Project Setup Guide

## Prerequisites

Before you start working on this project, make sure you have the following software installed:

### Java
You need to have Java installed on your system.

### Scoop (for Windows)
Scoop is a convenient command-line installer for Windows. You can install it using PowerShell with the following command:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser # Optional: Needed to run a remote script the first time
irm get.scoop.sh | iex
```

### Allure (for Windows)
Allure is a tool designed for test report generation. You can install it using Scoop with the following command:
```powershell
scoop install allure
```

### Python
Make sure you have Python installed on your system.

### Project Setup
Install project requirements using pip:
```powershell
pip install -r requirements.txt
```

Configure your Python interpreter in your preferred development environment. Make sure you have the following packages installed:
- allure-pytest
- allure-python-commons

### Usage
1. Run test
```powershell
pytest .\tests\ 
```
2. Generate test reports using Allure:
```powershell
allure serve .allure_results
```
