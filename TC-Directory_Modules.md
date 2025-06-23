# ✅ Test Cases – Directory Module

## Module: Employee Directory – Search Staff Records

**Objective:**  
To verify that the directory module allows accurate employee search using various filters like name, job title, and location.

---

| TC ID         | Title                                  | Type       | Priority | Preconditions      | Test Steps                                                                                  | Expected Result                                       | Status |
|---------------|----------------------------------------|------------|----------|---------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------|--------|
| TC-DIR-01     | Access Directory module                | Functional | High     | User is logged in   | 1. Click “Directory” from sidebar or dashboard                                             | Directory search page loads                           | ✅ Pass |
| TC-DIR-02     | Search by full employee name           | Functional | High     | Directory page open | 1. Enter full name like "Linda Anderson"<br>2. Click Search                                | Linda’s record is shown                               | ✅ Pass |
| TC-DIR-03     | Search by partial employee name        | Functional | Medium   | Directory page open | 1. Enter partial name like "Linda"<br>2. Click Search                                      | All results matching "Linda" appear                   | ✅ Pass |
| TC-DIR-04     | Search with invalid name               | Negative   | Medium   | Directory page open | 1. Enter name like "Xyznobody"<br>2. Click Search                                          | Message: “No Records Found”                           | ✅ Pass |
| TC-DIR-05     | Search using Job Title filter          | Functional | Medium   | Directory page open | 1. Select Job Title: "Software Engineer"<br>2. Click Search                                | Employees with that job title are shown               | ✅ Pass |
| TC-DIR-06     | Search using Location filter           | Functional | Medium   | Directory page open | 1. Select Location: "New York Sales Office"<br>2. Click Search                             | Employees from selected location are displayed         | ✅ Pass |
| TC-DIR-07     | Combine Name + Job Title + Location    | Functional | High     | Directory page open | 1. Enter Name: Linda<br>2. Job Title: QA Engineer<br>3. Location: HQ<br>4. Click Search    | Matching record (if exists) appears                   | ✅ Pass |
| TC-DIR-08     | Clear filters                          | Functional | Low      | After applying filters | 1. Click Reset / Clear (if available)                                                     | Filters cleared and default directory reloaded         | ✅ Pass |
| TC-DIR-09     | Validate result card structure         | UI         | Low      | Search returns result | 1. Observe displayed employee cards                                                         | Name, title, contact, location should appear properly  | ✅ Pass |
| TC-DIR-10     | Submit search with all fields empty    | Functional | Low      | Directory page open | 1. Leave all fields blank<br>2. Click Search                                               | All employees listed                                  | ✅ Pass |

![image](https://github.com/user-attachments/assets/7dd3b7ee-972e-4d66-810b-aa9d8010ef08)
