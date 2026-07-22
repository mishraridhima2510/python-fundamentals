# Student Information

class Student:

    def __init__(self, name, course):

        self.name = name
        self.course = course

    def show(self):

        print("Name:", self.name)
        print("Course:", self.course)

student1 = Student("Ridhima", "B.Tech CSE")

student1.show()
