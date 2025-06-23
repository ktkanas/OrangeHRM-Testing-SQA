# ❌ Negative Test Cases – OrangeHRM Demo

## Objective:  
To test how the application handles invalid input, blank submissions, unauthorized access, and unexpected user actions across modules.

---

| TC ID         | Title                                           | Module       | Priority | Preconditions      | Test Steps                                                                                  | Expected Result                                       | Status |
|---------------|-------------------------------------------------|--------------|----------|---------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------|--------|
| TC-NEG-01     | Login with wrong password                       | Login        | High     | Login page open     | 1. Enter username: Admin<br>2. Enter incorrect password<br>3. Click Login                  | Error: Invalid credentials                             | ✅ Pass |
| TC-NEG-02     | Login with all fields blank                     | Login        | High     | Login page open     | 1. Leave both fields empty<br>2. Click Login                                               | Error: Required fields                                 | ✅ Pass |
| TC-NEG-03     | Access /dashboard without login                 | Global       | High     | Not logged in       | 1. Manually enter URL: /dashboard                                                          | Redirected to login page                               | ✅ Pass |
| TC-NEG-04     | Submit Apply Leave with no data                 | Leave        | High     | On Apply Leave page | 1. Click Apply without selecting leave type or dates                                       | Error messages shown                                   | ✅ Pass |
| TC-NEG-05     | Search employee with non-existent name          | PIM          | Medium   | On PIM page         | 1. Enter name: “NoSuchUser123”<br>2. Click Search                                          | Message: “No Records Found”                            | ✅ Pass |
| TC-NEG-06     | Search directory with invalid filters           | Directory    | Medium   | On Directory page   | 1. Enter junk data and select conflicting filters<br>2. Click Search                       | No records found                                       | ✅ Pass |
| TC-NEG-07     | Submit leave request with past date             | Leave        | Medium   | On Apply Leave page | 1. Select a date in the past<br>2. Click Apply                                             | Error or validation depending on system                | ✅ Pass |
| TC-NEG-08     | Filter Admin users with blank criteria          | Admin        | Low      | On Admin page       | 1. Leave all filter fields blank<br>2. Click Search                                        | Full list returned                                     | ✅ Pass |
| TC-NEG-09     | Input special characters in Employee Search     | PIM          | Medium   | On PIM page         | 1. Enter: !@#$%^&*()<br>2. Click Search                                                    | No results found or input sanitized                    | ✅ Pass |
| TC-NEG-10     | Rapid refresh while submitting leave            | Leave        | Low      | On Apply Leave page | 1. Select fields<br>2. Click Apply and rapidly refresh page                                | Form may reset; data may be lost                       | ✅ Pass |
| TC-NEG-11     | Broken navigation with expired session          | Global       | Medium   | Session expired     | 1. Stay idle >20 mins<br>2. Click on any tab                                               | Redirected to login or error page                      | ✅ Pass |
| TC-NEG-12     | Input invalid employee ID (random digits)       | PIM          | Medium   | On PIM page         | 1. Enter: 9999999 in Employee ID<br>2. Click Search                                        | No employee record found                               | ✅ Pass |

