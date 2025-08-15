
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")


class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def describe(self):
        print(f"{self.name} is a mammal with {self.fur_color} fur.")


class Dog(Mammal):
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed

    def display(self):
        print(f"This is a {self.breed} named {self.name} with {self.fur_color} fur.")


dog = Dog("Buddy", "golden", "Golden Retriever")


dog.sound()      
dog.describe()   
dog.display()    
