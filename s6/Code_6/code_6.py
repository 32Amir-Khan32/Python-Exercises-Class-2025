class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Moving...")
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors
    
    def honk(self):
        print("Beep beep!")
    
    def display_info(self):
        super().display_info()
        print(f"Doors: {self.num_doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, has_sidecar):
        super().__init__(brand, model)
        self.has_sidecar = has_sidecar
    
    def wheelie(self):
        print("Doing a wheelie!")
    
    def display_info(self):
        super().display_info()
        sidecar_status = "with sidecar" if self.has_sidecar else "without sidecar"
        print(f"Type: Motorcycle {sidecar_status}")

# Create objects
car1 = Car("Toyota", "Camry", 4)
bike1 = Motorcycle("Harley", "Davidson", False)

car1.display_info()
car1.honk()
car1.move()

print()

bike1.display_info()
bike1.wheelie()
bike1.move()