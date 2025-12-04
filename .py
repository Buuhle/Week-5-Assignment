class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, protector of {self.city}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")


class FlyingHero(Superhero):
    def __init__(self, name, power, city, altitude):
        super().__init__(name, power, city)
        self.altitude = altitude

    def use_power(self):
        print(f"{self.name} flies at {self.altitude} meters using {self.power}!")


class Vehicle:
