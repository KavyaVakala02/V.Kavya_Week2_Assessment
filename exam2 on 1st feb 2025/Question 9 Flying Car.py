class Car:
    def move(self):
        return "Driving on road"
class Airplane:
    def move(self):
        return "Flying in air."
class FlyingCar(Car, Airplane):
    def move(self):
        road = Car.move(self)
        sky = Airplane.move(self)
        return f"FlyingCar: {road} and {sky}"
# Create an instance of FlyingCar
flying_car = FlyingCar()
# Call the move method
print(flying_car.move())
