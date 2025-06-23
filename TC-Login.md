# ✅ Test Cases – Login Module

## Module: Login Page

**Objective:**  
To verify the login functionality of the OrangeHRM demo site for both valid and invalid user interactions.

---

| TC ID       | Title                              | Type       | Priority | Preconditions      | Test Steps                                                                 | Expected Result                              |
|-------------|------------------------------------|------------|----------|---------------------|----------------------------------------------------------------------------|-----------------------------------------------|
| TC-LOGIN-01 | Login with valid credentials       | Functional | High     | Login page is loaded | 1. Enter username: Admin<br>2. Enter password: admin123<br>3. Click Login | User is redirected to dashboard               |
| TC-LOGIN-02 | Login with invalid password        | Negative   | High     | Login page is loaded | 1. Enter username: Admin<br>2. Enter wrong password<br>3. Click Login     | Error message "Invalid credentials" appears   |
| TC-LOGIN-03 | Login with blank username          | Negative   | Medium   | Login page is loaded | 1. Leave username blank<br>2. Enter password: admin123<br>3. Click Login  | Error: "Required" under username field        |
| TC-LOGIN-04 | Login with blank password          | Negative   | Medium   | Login page is loaded | 1. Enter username: Admin<br>2. Leave password blank<br>3. Click Login     | Error: "Required" under password field        |
| TC-LOGIN-05 | Login with both fields blank       | Negative   | High     | Login page is loaded | 1. Leave both fields blank<br>2. Click Login                             | Error: "Required" messages for both fields    |
| TC-LOGIN-06 | Password input is masked           | UI         | Low      | Login page is loaded | 1. Enter password into field                                              | Input appears masked as dots or asterisks     |
| TC-LOGIN-07 | Submit login form using Enter key  | Functional | Medium   | Login page is loaded | 1. Enter valid credentials<br>2. Press Enter key                         | Form is submitted and login succeeds          |
| TC-LOGIN-08 | "Remember Me" checkbox behavior    | UI         | Low      | Login page is loaded | 1. Check "Remember Me"<br>2. Login<br>3. Logout<br>4. Return to login     | Username is pre-filled or remembered          |
| TC-LOGIN-09 | Case sensitivity in username field | Negative   | Low      | Login page is loaded | 1. Enter username: admin<br>2. Enter password: admin123<br>3. Click Login | Login fails if username is case-sensitive     |



![image](https://github.com/user-attachments/assets/2e50a259-e22e-40f4-af86-4f482a8ab35d)
