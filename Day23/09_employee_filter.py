# Employee Filter

employees = [
    ("Rahul", 50000),
    ("Aman", 30000),
    ("Priya", 70000)
]

high_salary = list(filter(lambda emp: emp[1] >= 50000, employees))

print(high_salary)
