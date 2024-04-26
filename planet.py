class Planet:
    def __init__(self, name, mass, radius, distance):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.distance = distance

    def __str__(self):
        return f"Name: {self.name}\nMass: {self.mass}\nRadius: {self.radius}\nDistance: {self.distance}"

    def orbit(self):
        return 4.0 * 3.14159**2 * self.distance**3 / (6.67e-11 * self.mass)

def planet():
    name = input("Enter the name of the planet: ")
    mass = float(input("Enter the mass of the planet in kg: "))
    radius = float(input("Enter the radius of the planet in meters: "))
    distance = float(input("Enter the distance of the planet in meters: "))
    p = Planet(name, mass, radius, distance)
    print(p)
    print(f"The planet will orbit at {p.orbit()} meters.")
    return p