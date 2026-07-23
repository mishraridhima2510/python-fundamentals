# Multilevel Inheritance

class Grandparent:

    def family(self):
        print("Grandparent Class")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

child = Child()
child.family()
