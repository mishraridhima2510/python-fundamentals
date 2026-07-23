# Employee Salary

class Employee:

    def __init__(self, salary):
        self.salary = salary

class Manager(Employee):

    def display(self):
        print("Salary:", self.salary)

manager = Manager(50000)

manager.display()
