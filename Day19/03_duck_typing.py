# Duck Typing

class Cat:

    def speak(self):
        print("Meow")

class Dog:

    def speak(self):
        print("Bark")

def make_sound(animal):
    animal.speak()

cat = Cat()
dog = Dog()

make_sound(cat)
make_sound(dog)
