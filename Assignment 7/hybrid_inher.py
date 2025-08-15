
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


class Bird(Animal):
    def __init__(self, name, wing_span):
        super().__init__(name)
        self.wing_span = wing_span

    def describe(self):
        print(f"{self.name} is a bird with a wingspan of {self.wing_span} cm.")


class Bat(Mammal, Bird):
    def __init__(self, name, fur_color, wing_span, nocturnal):
        Mammal.__init__(self, name, fur_color)
        Bird.__init__(self, name, wing_span)
        self.nocturnal = nocturnal

    def display(self):
        print(f"{self.name} is a {'nocturnal' if self.nocturnal else 'diurnal'} bat.")
        print(f"It has {self.fur_color} fur and a wingspan of {self.wing_span} cm.")


bat = Bat("Fruit Bat", "black", 120, True)


bat.sound()     
bat.describe()   
bat.display()    

