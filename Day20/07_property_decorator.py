# Property Decorator

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

rectangle = Rectangle(10, 5)

print("Area:", rectangle.area)
