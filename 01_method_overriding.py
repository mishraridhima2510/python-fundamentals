# Method Overriding

class Animal:

    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):

    def sound(self):
        print("Dog barks.")

dog = Dog()
dog.sound()
