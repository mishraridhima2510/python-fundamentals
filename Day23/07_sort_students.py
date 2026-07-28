# Sort Students

students = [
    ("Rahul", 85),
    ("Aman", 92),
    ("Priya", 78)
]

students.sort(key=lambda student: student[1])

print(students)
