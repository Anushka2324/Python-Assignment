class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print(f"Employee ID: {self.emp_id}, Salary: {self.salary}")


class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary, department):
        
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        self.department = department

    def display(self):
        
        Person.display(self)
        Employee.display(self)
        print(f"Department: {self.department}")

manager = Manager("Alice", 35, "E001", 75000, "IT")


manager.display()
