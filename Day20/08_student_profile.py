# Student Profile

class Student:

    def __init__(self, name, cgpa):
        self.__name = name
        self.__cgpa = cgpa

    def display(self):
        print("Name:", self.__name)
        print("CGPA:", self.__cgpa)

student = Student("Ridhima", 8.81)

student.display()
