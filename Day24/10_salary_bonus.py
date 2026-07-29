# Salary Bonus Calculator

employees = {
    "Rahul": 50000,
    "Aman": 45000,
    "Priya": 60000,
    "Riya": 55000
}

updated_salary = {
    name: salary + 5000
    for name, salary in employees.items()
}

print(updated_salary)
