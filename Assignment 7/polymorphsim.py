class Dog:
    def sound(self):
        print("Dog barks.")

class Cat:
    def sound(self):
        print("Cat meows.")

def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()


make_sound(dog)  
make_sound(cat)  
