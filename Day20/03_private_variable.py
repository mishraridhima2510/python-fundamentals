# Private Variable

class Student:

    def __init__(self):
        self.__cgpa = 8.81

    def display(self):
        print("CGPA:", self.__cgpa)

student = Student()

student.display()
