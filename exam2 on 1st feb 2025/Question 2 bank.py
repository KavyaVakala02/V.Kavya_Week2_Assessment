class Employee:
    def __init__(self, name, emp_id, department): #constructor
        self.name = name
        self.id = emp_id
        self.department = department
    def display(self):
        print("\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Department: {self.department}")
def main():
    # Taking user input 
    name = input("Enter Employee Name: ")
    emp_id = input("Enter Employee ID: ")
    department = input("Enter Department: ")
    # Creating Employee object
    emp1 = Employee(name, emp_id, department)
    # Displaying employee details
    emp1.display()
main()
