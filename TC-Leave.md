# ✅ Test Cases – Leave Module

## Module: Leave – Apply, View, Track Leave Requests

**Objective:**  
To validate that users can apply for leave, track status, and view their leave history through the Leave module.

---

| TC ID       | Title                                      | Type       | Priority | Preconditions       | Test Steps                                                                                     | Expected Result                                       | Status |
|-------------|--------------------------------------------|------------|----------|----------------------|------------------------------------------------------------------------------------------------|--------------------------------------------------------|--------|
| TC-LEAVE-01 | Access Leave module                        | Functional | High     | User is logged in    | 1. Click “Leave” on sidebar                                                                    | Leave dashboard page loads                            | ✅ Pass |
| TC-LEAVE-02 | Navigate to Apply Leave page              | Functional | High     | On Leave module      | 1. Click “Apply” tab from top bar                                                              | Apply Leave form is displayed                         | ✅ Pass |
| TC-LEAVE-03 | Apply for leave with valid details        | Functional | High     | On Apply Leave page  | 1. Select leave type<br>2. Choose dates<br>3. Add reason<br>4. Click Apply                    | Leave request is submitted                            | ✅ Pass |
| TC-LEAVE-04 | Apply for leave with overlapping dates    | Negative   | Medium   | On Apply Leave page  | 1. Submit new leave request for a date range that already has leave                           | Error shown or request rejected                       | ✅ Pass |
| TC-LEAVE-05 | Submit empty Apply Leave form             | Negative   | High     | On Apply Leave page  | 1. Click Apply without selecting dates or type                                                 | Required field errors are shown                       | ✅ Pass |
| TC-LEAVE-06 | Navigate to My Leave tab                  | Functional | Medium   | User is logged in    | 1. Click “My Leave” tab                                                                        | Table showing leave history/status is displayed       | ✅ Pass |
| TC-LEAVE-07 | View leave request status                 | Functional | Medium   | At My Leave tab      | 1. Look for previously submitted leave                                                         | Status like "Pending", "Approved", or "Rejected" shown | ✅ Pass |
| TC-LEAVE-08 | Filter leave records by date              | Functional | Medium   | At My Leave tab      | 1. Choose From and To date<br>2. Click Search                                                  | Only matching leave records shown                     | ✅ Pass |
| TC-LEAVE-09 | Submit half-day leave (if option present) | Functional | Low      | On Apply Leave page  | 1. Select half-day option<br>2. Choose appropriate date and type                              | Half-day leave request is submitted                   | ✅ Pass |
| TC-LEAVE-10 | Cancel or edit pending leave request      | UI/Negative| Medium   | Leave request pending | 1. Try editing/cancelling leave from My Leave tab                                             | Cancel option may not be available (read-only)         | ✅ Pass |
| TC-LEAVE-11 | UI validation for Apply Leave form        | UI         | Low      | On Apply Leave page  | 1. Check alignment of input boxes, labels, date pickers                                       | UI is responsive and properly structured              | ✅ Pass |
| TC-LEAVE-12 | Filter leave with no match                | Negative   | Medium   | At My Leave tab      | 1. Select dates that don’t include any requests<br>2. Click Search                             | Message “No Records Found” shown                      | ✅ Pass |
![image](https://github.com/user-attachments/assets/d4b0f220-e043-4820-8a47-2f977b108863)
