class Example:
    
    def __init__(self, name):
        self.name = name
        print(f"Constructor called. Object created for {self.name}")

    def __del__(self):
        print(f"Destructor called. Object {self.name} is being deleted")

obj1 = Example("Sample Object")


print(f"Object Name: {obj1.name}")


del obj1


print("End of program")
