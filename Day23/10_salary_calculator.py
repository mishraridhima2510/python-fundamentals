# Salary Calculator

employees = [
    ("Rahul", 50000),
    ("Aman", 45000),
    ("Priya", 60000)
]

updated_salary = list(
    map(lambda emp: (emp[0], emp[1] + 5000), employees)
)

print(updated_salary)
