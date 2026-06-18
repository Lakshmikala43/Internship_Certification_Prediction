# Student Attendance Certification System

## APSSDC Machine Learning Internship - Milestone Project

### Project Overview

This project was developed as part of the APSSDC Machine Learning Internship Program. The system automates attendance tracking and certificate eligibility determination for students attending online internship sessions.

The application processes attendance data for 980 students across 40 online sessions and generates a comprehensive Excel report containing attendance statistics and certification status.

---

## Project Requirements

- Total Students: 980+
- Total Sessions: 40
- Session Duration: 120 Minutes

### Attendance Criteria

- Present: Attendance Duration ≥ 90 Minutes
- Absent: Attendance Duration < 90 Minutes

### Certificate Eligibility

Students are eligible for certification if their attendance percentage is greater than or equal to 80%.

Attendance Percentage = (Present Sessions / Total Sessions) × 100

---

## Technologies Used

- Python
- Pandas
- NumPy
- Faker
- OpenPyXL

---

## Features

✔ Automated student dataset generation

✔ Attendance tracking across 40 sessions

✔ Attendance percentage calculation

✔ Certificate eligibility determination

✔ Excel report generation

✔ Summary statistics generation

---

## Generated Reports

The system generates an Excel workbook containing:

- All Students
- Eligible Students
- Not Eligible Students
- Summary Report

---

## How to Run

```bash
pip install pandas numpy faker openpyxl
python report.py
