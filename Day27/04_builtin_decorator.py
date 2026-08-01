# Built-in Property Decorator

class Student:

    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

student = Student(95)

print(student.marks)
