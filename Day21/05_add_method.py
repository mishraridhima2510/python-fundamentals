# __add__ Method

class Marks:

    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

m1 = Marks(80)
m2 = Marks(90)

print(m1 + m2)
