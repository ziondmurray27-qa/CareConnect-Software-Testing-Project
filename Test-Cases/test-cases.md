# CareConnect Test Cases

## TC-LOGIN-001 — Successful Login

**Preconditions**
- User is on the CareConnect login screen
- A valid test account exists

**Steps**
1. Enter a valid username
2. Enter the corresponding valid password
3. Click Login

**Expected Result**
- User is successfully authenticated
- User is redirected to the main dashboard

---

## TC-LOGIN-002 — Invalid Password

**Preconditions**
- User is on the CareConnect login screen
- A valid test account exists

**Steps**
1. Enter a valid username
2. Enter an incorrect password
3. Click Login

**Expected Result**
- Login is rejected
- An appropriate error message is displayed
- User remains on the login screen

---

## TC-SCHED-001 — Prevent Double Booking

**Preconditions**
- Patient already has an appointment at 2:00 PM

**Steps**
1. Select the patient
2. Select the already occupied 2:00 PM time slot
3. Click Schedule Appointment

**Expected Result**
- The appointment is not created
- A conflict message is displayed
- User must select another available time

---

## TC-MSG-001 — Message Character Boundary

**Requirement**
- Messages have a maximum length of 500 characters

**Test Data**
- 499 characters
- 500 characters
- 501 characters

**Expected Results**
- 499 characters: accepted
- 500 characters: accepted
- 501 characters: prevented or rejected
