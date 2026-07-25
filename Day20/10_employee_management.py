# Employee Management System

class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def increment(self, amount):
        self.__salary += amount

    def display(self):
        print("Employee:", self.__name)
        print("Salary:", self.__salary)

employee = Employee("Rahul", 50000)

employee.increment(5000)

employee.display()
