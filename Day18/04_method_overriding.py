# Method Overriding

class Animal:

    def sound(self):
        print("Animal Sound")

class Cat(Animal):

    def sound(self):
        print("Meow")

cat = Cat()
cat.sound()
