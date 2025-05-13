# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Subclasses with different implementations of move()
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water 🚢")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the path 🚴")

# Polymorphism in action
def vehicle_movement(vehicle):
    vehicle.move()

# Create a list of different vehicles
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Loop through and demonstrate polymorphism
for v in vehicles:
    vehicle_movement(v)
