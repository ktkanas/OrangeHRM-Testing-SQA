# 🐞 Bug Report – OrangeHRM Manual Testing

**Project:** OrangeHRM Demo Site  
**Module Affected:** Leave Module  
**Reported By:** Muhammad Anas  
**Reported On:** July  20, 2025
**Environment:** Windows 10, Chrome v119, https://opensource-demo.orangehrmlive.com  

---

## 🔖 [BUG-001] Submit button unresponsive on Apply Leave form

**Status:** To Do  
**Priority:** Medium  
**Type:** Bug  
**Component:** Leave > Apply Leave  
**Affects Version:** Demo Version (Nov 2024)  
**Fix Version:** TBD  
**Assignee:** Unassigned  
**Resolution:** Unresolved  
**Labels:** leave-form, ui-bug  

---

### 📋 Description:

The "Apply" button on the Apply Leave form becomes unresponsive if the user fills all fields and clicks "Apply" without focusing out of the date field. No error is shown and no action is taken.

---

### 🔄 Steps to Reproduce:

1. Login with valid Admin credentials  
2. Navigate to Leave → Apply  
3. Select a valid leave type  
4. Select From and To dates but do **not** click outside the date field  
5. Enter a comment  
6. Click "Apply"

---

### ✅ Expected Result:

Leave request is submitted and user is shown confirmation message or redirected to My Leave tab.

---

### ❌ Actual Result:

No action occurs. Button does not respond. No error or feedback message.

---

### 🌐 URL:

`https://opensource-demo.orangehrmlive.com/web/index.php/leave/applyLeave`

---

### 📸 Attachments:

- Screenshot: `bug-001-apply-leave-button.png`  
- Screen recording: `bug-001-apply-leave-loomscreencast.mp4`

---

### ⏱️ Time Estimates:

- Remaining Estimate: 2 days  
- Original Estimate: 1 day  
- Time Spent: 0.5 day  

---

### 📝 Notes:

- Issue occurs inconsistently, depending on how user interacts with calendar widget  
- Might be related to JS event not triggering form validation

---

