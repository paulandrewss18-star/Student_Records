Student Records Manager

A simple Python program that stores student records and generates useful class information using dictionaries, lists, and reusable functions.

Features

Stores each student's name, age, department, marks, and attendance.

Displays all student records.

Calculates each student's average mark.

Identifies PASS/FAIL students.

Finds the highest-performing student based on average marks.

Filters students by attendance and average-mark thresholds.

Displays a class summary, including total students and overall class average.

Handles an empty student list when generating the class summary.

Requirements

Python 3.8 or later

No external libraries required

How to Run

Download or clone this repository.

Open a terminal in the project folder.

Run:

python student_records.py

Sample Data

The program includes three example records: Dass, Chandra, and Parvathi. The ages are illustrative because ages were not provided in the task example. Replace them with accurate values if needed.

Pass/Fail Rule

A student passes when every subject mark is at least 40. You can change PASS_MARK near the top of the file if your institution uses a different rule.

Customizing the Data

Add another dictionary to the students list using the same fields:

{
    "name": "Example Student",
    "age": 20,
    "department": "CSE",
    "marks": [70, 80, 75],
    "attendance": 88,
}

The functions process the records dynamically, so you do not need to write separate calculations for each student.

Project Structure

Student-Records/
├── student_records.py
└── README.md