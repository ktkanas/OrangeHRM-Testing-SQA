# ✅ Test Plan – OrangeHRM Demo Website

**Project:** OrangeHRM Manual Testing Project  
**Tester:** Muhammad Anas  
**Date:** June 2025

**Version:** 1.0  
**URL:** https://opensource-demo.orangehrmlive.com

---

## 🧪 1. Introduction

This test plan defines the approach, scope, resources, and schedule for the manual testing of the OrangeHRM demo system. The goal is to validate key functionalities and usability of the system from an end-user perspective.

---

## 🎯 2. Objectives

- Verify all major functionalities like login, employee search, leave application, and admin panel access  
- Ensure that non-functional aspects such as responsiveness and user experience are intact  
- Identify any UI bugs, broken links, or inconsistent behavior  

---

## 📦 3. Test Items

| Module    | Feature Description                   |
|-----------|----------------------------------------|
| Login     | User login with valid/invalid data     |
| Dashboard | Page layout and module navigation      |
| Admin     | View/search employees, access records  |
| PIM       | View employee details, search/filter   |
| Leave     | Apply for leave, view leave status     |
| Directory | Search staff in directory              |
| Profile   | View profile, logout                   |

---

## 🚫 4. Features Not to Be Tested

- Backend database operations  
- Email and notification systems  
- Role-based access controls (only Admin is exposed)  

---

## 🔍 5. Testing Strategy

- Manual Black Box Testing  
- Exploratory and scenario-based UI testing  
- Browser compatibility (Chrome, Firefox)  

---

## 🧪 6. Test Types

| Type             | Description                                |
|------------------|--------------------------------------------|
| ✅ Functional    | Verifying that all features work as expected |
| ❌ Negative      | Invalid inputs, blank fields, wrong data     |
| 📱 UI/Responsive | Checking layout, responsiveness, and design |
| 🧩 Exploratory   | Ad-hoc scenarios outside documented cases    |

---

## 📌 7. Deliverables

- OrangeHRM_Project_Overview.md  
- Test_Plan.md  
- Functional Test Cases  
- Negative Test Cases  
- Bug_Report.md  
- Test_Summary_Report.md  

---

## ✅ 8. Entry Criteria

- Application is accessible via public URL  
- Login credentials are available (Admin / admin123)  
- UI is stable and loads successfully  

## ❎ 9. Exit Criteria

- All test cases executed  
- Major bugs logged and reproducible  
- Final summary and report submitted  

---

## 👨‍💻 10. Roles and Responsibilities

| Role        | Responsibility                         |
|-------------|------------------------------------------|
| QA Engineer | Write, execute, and report test cases    |
| Reviewer    | Review documentation and coverage        |

---

## 🛠️ 11. Tools Used

- Browser (Chrome / Firefox)  
- Screenshot / Loom for evidence  
- Markdown & GitHub for documentation  
- Google Sheets (for local test tracking)  

---

## ⚠️ 12. Risks and Mitigation

| Risk                                 | Mitigation                                |
|--------------------------------------|--------------------------------------------|
| Demo data may reset or be limited    | Use short, repeatable test cycles          |
| Some modules may be read-only        | Focus on navigation and UI verification    |

---

## 📝 13. Approval

| Name          | Role        | Status   |
|---------------|-------------|----------|
| Muhammad Anas | QA Engineer | ✅ Approved |

