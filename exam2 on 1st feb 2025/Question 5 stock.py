class Product:
    # Constructor to initialize 
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    # Method to check availability 
    def check_availability(self, quantity):
        return quantity <= self.stock
product1 = Product("Laptop", 1000, 5)
requested_quantity = 3
print(f"Availability: {product1.check_availability(requested_quantity)}")
