# Multiple Inheritance

class Father:

    def skills(self):
        print("Programming")

class Mother:

    def hobby(self):
        print("Painting")

class Child(Father, Mother):
    pass

child = Child()

child.skills()
child.hobby()
