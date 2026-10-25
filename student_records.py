"""
Student Records Manager
A beginner-friendly Python program to process student records.
"""

students = [
    {
        "name": "Dass",
        "age": 20, 
        "department": "CSE",
        "marks": [78, 85, 72],
        "attendance": 91,
    },
    {
        "name": "Chandra",
        "age": 21,  
        "department": "CSE",
        "marks": [65, 71, 68],
        "attendance": 84,
    },
    {
        "name": "Parvathi",
        "age": 20, 
        "department": "ECE",
        "marks": [45, 52, 48],
        "attendance": 72,
    },
]

PASS_MARK = 40
ATTENDANCE_THRESHOLD = 75
MARKS_THRESHOLD = 50


def average_mark(student):
    """Return the average of a student's marks."""
    marks = student["marks"]
    return sum(marks) / len(marks) if marks else 0


def get_result(student):
    """A student passes if every subject mark is at least PASS_MARK."""
    if student["marks"] and all(mark >= PASS_MARK for mark in student["marks"]):
        return "PASS"
    return "FAIL"


def display_all_students(records):
    """Display basic information for every student."""
    print("\nSTUDENT RECORDS")
    print("-" * 60)
    for student in records:
        print(
            f"Name: {student['name']} | Age: {student['age']} | "
            f"Department: {student['department']} | "
            f"Marks: {student['marks']} | Attendance: {student['attendance']}%"
        )


def display_student_averages(records):
    """Display each student's average mark."""
    print("\nSTUDENT AVERAGES")
    print("-" * 40)
    for student in records:
        print(f"{student['name']}: {average_mark(student):.1f}%")


def display_results(records):
    """Display pass/fail results."""
    print("\nSTUDENT RESULTS")
    print("-" * 40)
    for student in records:
        print(f"{student['name']} - {get_result(student)}")


def find_top_performer(records):
    """Return the student with the highest average, or None for no records."""
    return max(records, key=average_mark, default=None)


def filter_by_attendance(records, minimum_attendance):
    """Return students whose attendance is below the supplied percentage."""
    return [
        student for student in records
        if student["attendance"] < minimum_attendance
    ]


def filter_by_average_mark(records, minimum_average):
    """Return students whose average mark meets or exceeds the threshold."""
    return [
        student for student in records
        if average_mark(student) >= minimum_average
    ]


def display_class_summary(records):
    """Display totals, overall average, top performer, and low attendance."""
    print("\nCLASS SUMMARY")
    print("-" * 40)

    if not records:
        print("Total Students: 0")
        print("No student records available.")
        return

    all_marks = [
        mark
        for student in records
        for mark in student["marks"]
    ]
    class_average = sum(all_marks) / len(all_marks) if all_marks else 0
    top_student = find_top_performer(records)

    print(f"Total Students: {len(records)}")
    print(f"Average Class Mark: {class_average:.1f}")

    if top_student:
        print("Top Performer:")
        print(
            f"{top_student['name']} - "
            f"Average: {average_mark(top_student):.1f}%"
        )

    low_attendance = filter_by_attendance(records, ATTENDANCE_THRESHOLD)
    print(f"\nAttendance Below {ATTENDANCE_THRESHOLD}%:")
    if low_attendance:
        for student in low_attendance:
            print(f"{student['name']} - {student['attendance']}%")
    else:
        print("None")


def main():
    """Run all required student-record operations."""
    display_all_students(students)
    display_student_averages(students)
    display_results(students)
    display_class_summary(students)

    print(f"\nSTUDENTS WITH AVERAGE MARK >= {MARKS_THRESHOLD}%")
    print("-" * 40)
    qualifying_students = filter_by_average_mark(students, MARKS_THRESHOLD)
    if qualifying_students:
        for student in qualifying_students:
            print(f"{student['name']} - {average_mark(student):.1f}%")
    else:
        print("None")


if __name__ == "__main__":
    main()
