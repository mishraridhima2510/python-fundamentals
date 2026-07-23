# Single Inheritance

class Animal:

    def sound(self):
        print("Animals make sounds.")

class Dog(Animal):
    pass

dog = Dog()
dog.sound()
