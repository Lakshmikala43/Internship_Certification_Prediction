APSSDC Milestone Project: Student Attendance Certification System
📌 Project Overview

This project was developed as part of the APSSDC Machine Learning Internship Program. The system automates attendance tracking and certificate eligibility determination for students attending online internship sessions.

The project simulates attendance data for 980 students across 40 online sessions and generates an Excel-based report containing attendance records, attendance percentages, and certificate eligibility status.

🎯 Problem Statement

Managing attendance records manually for a large number of students is time-consuming and error-prone. This project provides an automated solution to:

Track student attendance across multiple sessions.
Calculate attendance percentages.
Determine certificate eligibility based on predefined criteria.
Generate comprehensive reports in Excel format.
📋 Project Requirements
Attendance Rules
Total Students: 980+
Total Sessions: 40
Duration of Each Session: 120 Minutes
Attendance Status
Present: Attendance Duration ≥ 90 Minutes
Absent: Attendance Duration < 90 Minutes
Certificate Eligibility

Students are eligible for certification if:

Attendance Percentage ≥ 80%

Attendance Percentage Calculation:

Attendance Percentage =
(Present Sessions / Total Sessions) × 100
🛠️ Technologies Used
Python
Pandas
NumPy
Faker
OpenPyXL
📂 Project Structure
Student-Attendance-Certification-System/
│
├── report.py
├── APSSDC_Attendance_Certification_Report.xlsx
├── README.md
└── requirements.txt
🚀 Features

✅ Automated student data generation

✅ Attendance simulation for 40 sessions

✅ Attendance percentage calculation

✅ Certificate eligibility evaluation

✅ Excel report generation

✅ Separate reports for eligible and non-eligible students

✅ Summary statistics generation

📊 Generated Dataset Fields
Field	Description
Roll Number	Unique Student ID
Student Name	Student Full Name
Email ID	Student Email Address
Session 1 - Session 40	Attendance Duration
Present Sessions	Total Present Sessions
Absent Sessions	Total Absent Sessions
Attendance Percentage	Attendance Percentage
Certificate Status	Eligible / Not Eligible
📈 Output Reports

The system generates an Excel file containing four sheets:

1. All Students

Contains attendance records for all students.

2. Eligible Students

Students with attendance percentage greater than or equal to 80%.

3. Not Eligible Students

Students with attendance percentage less than 80%.

4. Summary

Provides an overview of:

Total Students
Total Sessions
Eligible Students
Not Eligible Students
⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/student-attendance-certification-system.git

Navigate to the project directory:

cd student-attendance-certification-system

Install dependencies:

pip install pandas numpy faker openpyxl
▶️ Run the Project

Execute the Python script:

python report.py

After execution, the Excel report will be generated automatically:

APSSDC_Attendance_Certification_Report.xlsx
📊 Sample Output
============================================================
Attendance Certification Report Generated Successfully
============================================================

Total Students       : 980
Total Sessions       : 40
Eligible Students    : 250+
Not Eligible Students: Remaining Students
🎓 Learning Outcomes

Through this project, I gained practical experience in:

Data Generation and Simulation
Data Analysis using Pandas
Excel Automation with Python
Attendance Management Systems
Data Processing and Reporting
Real-world Problem Solving
