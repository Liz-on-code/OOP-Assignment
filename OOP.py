# Base class: Superhero
class Superhero:
    def __init__(self, name, superpower, city):
        self.name = name
        self.superpower = superpower
        self.city = city
        self.__secret_identity = "Unknown"  # Private attribute for secret identity

    # Method to display superhero details
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Superpower: {self.superpower}")
        print(f"City: {self.city}")

    # Encapsulation: Accessor and Mutator methods for secret_identity
    def set_secret_identity(self, identity):
        self.__secret_identity = identity

    def get_secret_identity(self):
        return self.__secret_identity

    # Method to demonstrate the superhero's power (generic)
    def use_power(self):
        print(f"{self.name} is using their power: {self.superpower}!")

# Subclass: FlyingHero inherits from Superhero
class FlyingHero(Superhero):
    def __init__(self, name, superpower, city, wing_span):
        super().__init__(name, superpower, city)
        self.wing_span = wing_span  # Additional attribute for FlyingHero

    # Overriding the use_power method to be specific for FlyingHero
    def use_power(self):
        print(f"{self.name} is flying with a wingspan of {self.wing_span} meters!")

# Create instances of Superhero and FlyingHero
hero1 = Superhero("Captain Speed", "Super Speed", "Nairobi")
hero1.set_secret_identity("Simon Kamau")

hero2 = FlyingHero("Sky Trooper", "Flight", "Mombasa", 20)

# Display superhero details
hero1.show_details()
print(f"Secret Identity: {hero1.get_secret_identity()}")
hero1.use_power()  # Calls base class method

print("\n---")

hero2.show_details()
hero2.use_power()  # Calls overridden method in FlyingHero class
