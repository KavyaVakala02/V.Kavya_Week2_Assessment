class Electronics:  #base class
    def __init__(self, brand, model):  
        self.brand = brand
        self.model = model
    def power_on(self):
        return f"{self.brand} {self.model} powered on."
class MobileDevice(Electronics):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)
        self.os = os
    def install_app(self, app_name):
        return f"Installing {app_name} on {self.os}."
class SmartPhone(MobileDevice):
    def __init__(self, brand, model, os, camera_quality):
        super().__init__(brand, model, os)
        self.camera_quality = camera_quality
    def power_on(self):
        return f"SmartPhone {self.brand} {self.model} is powered on."
    def take_photo(self):
        return f"Taking a photo with {self.camera_quality} camera."
# Create a SmartPhone object
phone = SmartPhone("Samsung", "Model 1", "iOS", "15 MP")
# Use the methods
print(phone.power_on())  # Overridden method
print(phone.install_app("Instagram"))  # Reused method
print(phone.take_photo())  # New method
