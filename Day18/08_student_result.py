# Student Result

class Student:

    def __init__(self, name):
        self.name = name

class Result(Student):

    def __init__(self, name, marks):

        super().__init__(name)
        self.marks = marks

    def display(self):

        print("Name:", self.name)
        print("Marks:", self.marks)

student = Result("Ridhima", 95)

student.display()
