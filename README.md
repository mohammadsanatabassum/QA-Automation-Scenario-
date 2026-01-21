# ✅ QA Automation Scenario (HCLTech Case Study)

A complete **Selenium + Pytest Automation Framework** for testing an enterprise web application's **Authentication Module**.  
This project automates **Login**, **Invalid Login Error Validations**, and **Forgot Password** workflow using **Page Object Model (POM)** with reusable utilities, fixtures, logs, and HTML reporting.

---

## 🌐 Live Links

✅ **Project Dashboard (GitHub Pages):**  
https://mohammadsanatabassum.github.io/QA-Automation-Scenario-/

✅ **Latest Pytest HTML Report:**  
https://mohammadsanatabassum.github.io/QA-Automation-Scenario-/report.html

✅ **GitHub Actions (Run Tests):**  
https://github.com/mohammadsanatabassum/QA-Automation-Scenario-/actions

---

## 🧠 Case Study Problem Statement

HCLTech develops enterprise web applications that require rigorous testing before deployment.  
As a QA Automation Engineer, automate the testing of the **Authentication module**:

- Login Page
- Forgot Password
- Error message validations

---

## ✅ Implemented Tasks

✔ Automate login functionality with valid and invalid credentials  
✔ Validate error messages for incorrect login attempts  
✔ Automate “Forgot Password” workflow  
✔ Pytest structured framework (test organization + markers)  
✔ Reusable fixtures and utilities  
✔ Generate execution logs and HTML test reports  
✔ Handle dynamic elements and page loading delays  
✔ Data-driven testing using JSON

---

## 🏗️ Tech Stack

- **Python**
- **Selenium WebDriver**
- **Pytest**
- **webdriver-manager / Selenium Manager**
- **pytest-html** (HTML reports)
- **GitHub Actions (CI)**
- **GitHub Pages** (Dashboard + report hosting)

---

## 📁 Folder Structure

QA-Automation-Scenario-/
│
├── .github/workflows/
│ └── qa_tests.yml
│
├── config/
│ └── config.py
│
├── data/
│ └── login_data.json
│
├── docs/
│ ├── index.html
│ └── report.html
│
├── logs/
│ └── test_execution.log
│
├── pages/
│ ├── login_page.py
│ └── forgot_password_page.py
│
├── reports/
│ └── report.html
│
├── tests/
│ ├── conftest.py
│ ├── test_login.py
│ └── test_forgot_password.py
│
├── utilities/
│ ├── logger.py
│ └── wait_utils.py
│
├── requirements.txt
└── pytest.ini

📊 Reports & Logs Generated

✅ HTML Report:

reports/report.html

Published to docs/report.html for GitHub Pages

✅ Execution Log:

logs/test_execution.log

🤖 CI Execution (GitHub Actions)

This project is integrated with GitHub Actions CI:

Runs automation tests in headless chrome mode

Generates HTML report

Automatically publishes report to GitHub Pages

To run:
✅ Repo → Actions → Run QA Automation Tests → Run workflow
