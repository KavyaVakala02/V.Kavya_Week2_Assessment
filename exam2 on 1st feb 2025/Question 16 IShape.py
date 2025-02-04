from abc import ABC, abstractmethod
# Define the IShape interface using ABC
class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(IShape):
    def __init__(self, width, height): 
        self.width = width
        self.height = height
    def calculate_area(self): #to calculate the area of rectangle
        return self.width * self.height
class Circle(IShape):   
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):  #to calculate area of circle
        return 3.14 * (self.radius ** 2)
rectangle = Rectangle(5, 3) #creating instances
circle = Circle(4)
print(f"Area of Rectangle: {rectangle.calculate_area()}")  # Rectangle area
print(f"Area of Circle: {circle.calculate_area()}")        # Circle area
