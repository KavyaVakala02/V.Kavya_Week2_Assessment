class Animal:
    # Base class
    def speak(self):
        pass  
class Dog(Animal):
    # Dog subclass
    def speak(self):
        return "Bark!"
class Cat(Animal):
    # Cat subclass
    def speak(self):
        return "Meow!"
# Creating instances
dog = Dog()
cat = Cat()
print(dog.speak())  # Bark!
print(cat.speak())  # Meow!
