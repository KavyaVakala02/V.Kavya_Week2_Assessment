class Employee:
    def __init__(self, name, emp_id, department):  #constructor
        self.name = name
        self.id = emp_id
        self.department = department
    def display(self):                            #function to display output
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.id}")
        print(f"Department: {self.department}")
def main():
    name = input("Enter Employee Name: ")
    id = input("Enter Employee ID: ")
    department = input("Enter Department: ")
    # Creating Employee object
    employee1 = Employee(name, id, department)
    # Displaying employee details
    employee1.display()
main()
        