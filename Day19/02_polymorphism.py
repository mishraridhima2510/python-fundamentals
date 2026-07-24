# Polymorphism

class Bird:

    def fly(self):
        print("Bird can fly.")

class Airplane:

    def fly(self):
        print("Airplane can fly.")

def display(obj):
    obj.fly()

bird = Bird()
plane = Airplane()

display(bird)
display(plane)
