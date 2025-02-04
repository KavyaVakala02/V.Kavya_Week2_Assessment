class Student: 
    def __init__(self, name, roll_no):   # Constructor
        self.name = name
        self.roll_no = roll_no
    def get_details(self): #method to return student details
        return f"Student Name: {self.name}, Roll Number: {self.roll_no}"
stu1 = Student("Raju", "12")  #object created
print(stu1.get_details())
