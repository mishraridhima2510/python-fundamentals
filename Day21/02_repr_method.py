# __repr__ Method

class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student('{self.name}')"

student = Student("Ridhima")

print(repr(student))
