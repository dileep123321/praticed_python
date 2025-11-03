class Dog:
    def sound(self):
        return "Woof"
class Cat:
    def sound(self):
        return "Meow"
for animal in (Dog(), Cat()):
    print(animal.sound())