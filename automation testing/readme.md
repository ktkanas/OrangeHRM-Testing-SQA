# 🧪 OrangeHRM Automation Testing Project

This repository showcases a complete **Selenium-based automation testing framework** built for the [OrangeHRM Demo Site](https://opensource-demo.orangehrmlive.com/). It is structured using Page Object Model (POM) and follows real-world practices suitable for QA portfolios, job interviews, and team collaboration.

---

## 📌 Tech Stack

- **Language**: Python 3.10+
- **Web Automation**: Selenium
- **Test Framework**: unittest
- **Driver Management**: webdriver-manager
- **Reporting**: Console (extendable to Allure)

---

---

## ✅ Features Covered

- Valid and invalid **Login** tests
- **Dashboard** widget verification
- **Leave Application** automation (form fill + submit)
- Reusable Page Objects with clean locator separation
- Easily extendable test structure

---

## 🚀 How to Run

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Tests
```bash
python tests/test_login.py
python tests/test_dashboard.py
python tests/test_leave.py
```

---

## 🧑‍💻 Author

**Muhammad Anas**  
QA Engineer | SQA Portfolio Contributor  
[anasktk.official@gmail.com](mailto:anasktk.official@gmail.com)

---

## 🌐 System Under Test
[OrangeHRM Demo Site](https://opensource-demo.orangehrmlive.com/)
