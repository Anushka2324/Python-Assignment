class Display:
    def show(self, value):
        if isinstance(value, int):
            print(f"Integer: {value}")
        elif isinstance(value, str):
            print(f"String: {value}")
        else:
            print(f"Unknown type: {value}")


obj = Display()


obj.show(100)           
obj.show("Hello")         
obj.show([1, 2, 3])       
