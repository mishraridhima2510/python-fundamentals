# Student System

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} - {self.marks}"

student = Student("Ridhima", 95)

print(student)
