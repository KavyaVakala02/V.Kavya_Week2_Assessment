class Person:
    # Base class 
    def __init__(self, name, age): # constructor representing person
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
# Derived class 
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}")
# Manager inherits from Employee
class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department
    def display(self):
        super().display()
        print(f"Department: {self.department}")
    def leave(self, emp_name):
        print(f"Manager {self.name} has approved leave for {emp_name}.")
m1 = Manager("Surya", 50, "1290", "Networking")
print("\nManager Details:")
m1.display()
print()
m1.leave("Hari")
