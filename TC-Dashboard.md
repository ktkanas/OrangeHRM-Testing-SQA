# ✅ Test Cases – Dashboard Module

## Module: Dashboard Page

**Objective:**  
To verify that the dashboard page loads correctly, displays appropriate widgets, and allows navigation to linked modules.

---

| TC ID          | Title                                      | Type       | Priority | Preconditions         | Test Steps                                                                                 | Expected Result                                       |
|----------------|--------------------------------------------|------------|----------|------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------|
| TC-DASH-01     | Load dashboard after login                 | Functional | High     | Successful login       | 1. Log in using valid credentials                                                          | Dashboard page loads with widgets                     |
| TC-DASH-02     | Check visibility of "Time at Work" widget  | UI         | Medium   | Logged in              | 1. Locate the "Time at Work" section on dashboard                                          | Widget is visible and structured correctly             |
| TC-DASH-03     | Check visibility of "Quick Launch" links   | UI         | Medium   | Logged in              | 1. Locate "Quick Launch" section                                                           | Buttons like “Assign Leave” and “Apply Leave” are shown |
| TC-DASH-04     | Click "Apply Leave" from Quick Launch      | Functional | High     | Logged in              | 1. Click "Apply Leave" in Quick Launch                                                     | Redirects to Leave Application page                    |
| TC-DASH-05     | Click "My Leave" from Quick Launch         | Functional | Medium   | Logged in              | 1. Click "My Leave" in Quick Launch                                                        | Redirects to My Leave summary page                     |
| TC-DASH-06     | Click "Assign Leave" from Quick Launch     | Functional | Medium   | Logged in              | 1. Click "Assign Leave" in Quick Launch                                                    | Redirects to Assign Leave page                         |
| TC-DASH-07     | UI responsiveness of dashboard             | UI         | Medium   | Logged in              | 1. Resize browser window                                                                   | Layout adjusts properly across sizes                   |
| TC-DASH-08     | Click profile > Logout                     | Functional | High     | Logged in              | 1. Click profile icon on top right<br>2. Click Logout                                      | Redirects to login screen                             |
| TC-DASH-09     | Refresh dashboard page                     | Functional | Low      | On dashboard           | 1. Press F5 or refresh page                                                                | Page reloads and retains correct UI state              |
| TC-DASH-10     | Verify logged-in user name is displayed    | UI         | Low      | Logged in              | 1. Observe the user profile name in top right                                              | Displays “Paul Collings” or current demo admin         |
