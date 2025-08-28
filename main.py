# ============================================
# Assignment 1: Design Your Own Class
# ============================================

class Smartphone:
    # Constructor to initialize attributes
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.is_on = False
    
    # Method to power on the phone
    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")
    
    # Method to power off the phone
    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")
    
    # Method to display phone info
    def phone_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")


# Inheritance Example: GamingSmartphone inherits from Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu  # extra attribute for gaming phone
    
    # Override phone_info method (Polymorphism)
    def phone_info(self):
        print(f"🎮 Gaming Phone -> Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, GPU: {self.gpu}")


# Demo Assignment 1
print("===== Assignment 1: Smartphone Demo =====")
phone1 = Smartphone("Apple", "iPhone 15", 256)
phone2 = GamingSmartphone("Asus", "ROG Phone 7", 512, "Adreno 730")

phone1.power_on()
phone1.phone_info()
phone2.power_on()
phone2.phone_info()

print("\n")


# ============================================
# 🎭 Activity 2: Polymorphism Challenge
# ============================================

class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on the water.")


# Demo Activity 2
print("===== Activity 2: Polymorphism Demo =====")
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
