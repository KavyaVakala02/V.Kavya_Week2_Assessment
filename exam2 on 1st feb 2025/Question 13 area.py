class Shape:
    def area(self):
        raise NotImplementedError("Subclass not implement this method")
class Square(Shape):   #shape class
    def __init__(self, side_length):
        self.side_length = side_length
    def area(self):
        return self.side_length ** 2
class Triangle(Shape): #triangle class
    def __init__(self, base, height):    
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
# Creating instances of both classes
square = Square(4)
triangle = Triangle(5, 3)
# Calculate areas
print(f"Area of Square: {square.area()}")  # Square with side length 4
print(f"Area of Triangle: {triangle.area()}")  # Triangle with base 5 and height 3
