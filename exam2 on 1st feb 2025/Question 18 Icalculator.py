from abc import ABC, abstractmethod
class ICalculator(ABC):
    @abstractmethod
    def add(self, a, b):
        pass
    @abstractmethod
    def subtract(self, a, b):
        pass
    @abstractmethod
    def multiply(self, a, b):
        pass
    @abstractmethod
    def divide(self, a, b):
        pass
# Implement the Basic Calculator class
class BasicCalculator(ICalculator):
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
# Create an instance of BasicCalculator
calculator = BasicCalculator()
# Perform calculations
print("Addition:", calculator.add(5, 9))       
print("Subtraction:", calculator.subtract(78,8)) 
print("Multiplication:", calculator.multiply(5, 23)) 
print("Division:", calculator.divide(8,9))     
print("Division by zero:", calculator.divide(5, 0)) 
