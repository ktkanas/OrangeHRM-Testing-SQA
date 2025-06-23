# ✅ Test Cases – Login Module

## Module: Login Page

**Objective:**  
To validate login functionality, including both valid and invalid user actions.

---

| TC ID       | Title                              | Type       | Priority | Preconditions      | Test Steps                                                                 | Expected Result                              | Status |
|-------------|------------------------------------|------------|----------|---------------------|----------------------------------------------------------------------------|-----------------------------------------------|--------|
| TC-LOGIN-01 | Login with valid credentials       | Functional | High     | Login page is loaded | 1. Enter Admin<br>2. Enter admin123<br>3. Click Login                      | Redirected to dashboard                        | ✅ Pass |
| TC-LOGIN-02 | Login with invalid password        | Negative   | High     | Login page is loaded | 1. Enter Admin<br>2. Enter wrong password<br>3. Click Login               | Error: Invalid credentials                     | ✅ Pass |
| TC-LOGIN-03 | Login with blank username          | Negative   | Medium   | Login page is loaded | 1. Leave username blank<br>2. Enter admin123<br>3. Click Login            | Error: Required field                          | ✅ Pass |
| TC-LOGIN-04 | Login with blank password          | Negative   | Medium   | Login page is loaded | 1. Enter Admin<br>2. Leave password blank<br>3. Click Login               | Error: Required field                          | ✅ Pass |
| TC-LOGIN-05 | Login with both fields blank       | Negative   | High     | Login page is loaded | 1. Leave both fields blank<br>2. Click Login                              | Error messages under both fields               | ✅ Pass |
| TC-LOGIN-06 | Password field masks input         | UI         | Low      | Login page is loaded | 1. Type password into field                                               | Input appears masked (••••)                    | ✅ Pass |
| TC-LOGIN-07 | Submit form using Enter key        | Functional | Medium   | Login page is loaded | 1. Enter valid credentials<br>2. Press Enter                              | Form submits and logs in                       | ✅ Pass |
| TC-LOGIN-08 | Remember Me functionality          | UI         | Low      | Login page is loaded | 1. Check "Remember Me"<br>2. Login<br>3. Logout<br>4. Reopen browser      | Username is retained                           | ✅ Pass |
| TC-LOGIN-09 | Case sensitivity in username field | Negative   | Low      | Login page is loaded | 1. Enter 'admin' instead of 'Admin'<br>2. Valid password<br>3. Click Login | Login fails if username is case-sensitive      | ✅ Pass |



![image](https://github.com/user-attachments/assets/2e50a259-e22e-40f4-af86-4f482a8ab35d)
