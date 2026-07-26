# __del__ Method

class Student:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(self.name, "object deleted")

student = Student("Ridhima")

del student
