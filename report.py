import pandas as pd
import numpy as np
from faker import Faker

TOTAL_STUDENTS = 980
TOTAL_SESSIONS = 40

fake = Faker()

students_data = []

for student_id in range(1, TOTAL_STUDENTS + 1):

    roll_no = f"APSSDC2025{student_id:04d}"
    student_name = fake.name()

    email = (
        student_name.lower()
        .replace(" ", ".")
        .replace("'", "")
        .replace("-", ".")
        + "@gmail.com"
    )

    present_count = 0
    absent_count = 0

    session_attendance = {}

    for session in range(1, TOTAL_SESSIONS + 1):

        # Realistic attendance distribution
        attendance_minutes = np.random.choice(
            [
                np.random.randint(0, 90),
                np.random.randint(90, 121)
            ],
            p=[0.20, 0.80]
        )

        session_attendance[f"Session_{session}"] = attendance_minutes

        if attendance_minutes >= 90:
            present_count += 1
        else:
            absent_count += 1

    attendance_percentage = round(
        (present_count / TOTAL_SESSIONS) * 100,
        2
    )

    certificate_status = (
        "Eligible"
        if attendance_percentage >= 80
        else "Not Eligible"
    )

    student_record = {
        "Roll Number": roll_no,
        "Student Name": student_name,
        "Email ID": email,
        "Present Sessions": present_count,
        "Absent Sessions": absent_count,
        "Attendance Percentage": attendance_percentage,
        "Certificate Status": certificate_status
    }

    student_record.update(session_attendance)

    students_data.append(student_record)

df = pd.DataFrame(students_data)

eligible_students = df[
    df["Certificate Status"] == "Eligible"
]

not_eligible_students = df[
    df["Certificate Status"] == "Not Eligible"
]

summary = pd.DataFrame({
    "Metric": [
        "Total Students",
        "Total Sessions",
        "Eligible Students",
        "Not Eligible Students"
    ],
    "Value": [
        len(df),
        TOTAL_SESSIONS,
        len(eligible_students),
        len(not_eligible_students)
    ]
})

output_file = "APSSDC_Attendance_Certification_Report.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    df.to_excel(writer,
                sheet_name="All Students",
                index=False)

    eligible_students.to_excel(writer,
                               sheet_name="Eligible Students",
                               index=False)

    not_eligible_students.to_excel(writer,
                                   sheet_name="Not Eligible Students",
                                   index=False)

    summary.to_excel(writer,
                     sheet_name="Summary",
                     index=False)

print("\nExcel File Generated Successfully")
print("File Name:", output_file)

print("\nSummary")
print(summary)