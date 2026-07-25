# Protected Variable

class Student:

    def __init__(self):
        self._course = "B.Tech CSE"

student = Student()

print(student._course)
