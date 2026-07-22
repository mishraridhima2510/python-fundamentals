# Instance Method

class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

student1 = Student("Ridhima")

student1.display()
