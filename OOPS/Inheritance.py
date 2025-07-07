#  For example, a Car is a type of Vehicle, so it inherits features like engine and model 
#  from the Vehicle class, but also has extra features like an air conditioner. 
#  This promotes code reuse and modularity.


# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model}: Engine started.")

    def stop_engine(self):
        print(f"{self.brand} {self.model}: Engine stopped.")


# Child class - Car
class Car(Vehicle):
    def __init__(self, brand, model, ac_enabled):
        super().__init__(brand, model)
        self.ac_enabled = ac_enabled

    def turn_on_ac(self):
        print(f"{self.brand} {self.model}: AC turned ON.")


# Child class - Bike
class Bike(Vehicle):
    def __init__(self, brand, model, gear_type):
        super().__init__(brand, model)
        self.gear_type = gear_type

    def show_gear_type(self):
        print(f"{self.brand} {self.model}: Gear Type - {self.gear_type}")


# Create a Car object
car1 = Car("Toyota", "Fortuner", True)
car1.start_engine()
car1.turn_on_ac()
car1.stop_engine()

print("\n----------------------\n")

# Create a Bike object
bike1 = Bike("Yamaha", "R15", "Manual")
bike1.start_engine()
bike1.show_gear_type()
bike1.stop_engine()


# OUT PUT:- 

# Toyota Fortuner: Engine started.
# Toyota Fortuner: AC turned ON.
# Toyota Fortuner: Engine stopped.

# ----------------------

# Yamaha R15: Engine started.
# Yamaha R15: Gear Type - Manual
# Yamaha R15: Engine stopped.
        