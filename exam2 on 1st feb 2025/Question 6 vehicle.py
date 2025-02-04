class Vehicle:
    # Base class 
    def __init__(self, brand):  #constructor
        self.brand = brand
    def display_info(self):
        print(f"Brand: {self.brand}")
# Derived class 
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def display_info(self):   #displaying car(base class)
        super().display_info()
        print(f"Model: {self.model}")
# Derived class representing a bike
class Bike(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type
    def display_info(self):
        super().display_info()
        print(f"Type: {self.type}")
#  ElectricCar inherits from Car
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")
car1 = Car("CarA", "Corolla") #creating object
bike1 = Bike("Bike B", "Sport")  #creating object for bike
electric_car1 = ElectricCar("Benz", "Model S", 100)
print("\nCar Details:")
car1.display_info()
print("\nBike Details:")
bike1.display_info()
print("\nElectric Car Details:")
electric_car1.display_info()
