class Satelite:
    def __init__(self, name, mass, radius, distance):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.distance = distance

    def __str__(self):
        return (
            f"Satelite {self.name} with mass {self.mass} kg, radius "
            f"{self.radius} meters, and distance {self.distance} meters."
        )

def satelite():
    name = input("Enter the name of the satelite: ")
    mass = float(input("Enter the mass of the satelite in kg: "))
    radius = float(input("Enter the radius of the satelite in meters: "))
    distance = float(input("Enter the distance of the satelite in meters: "))
    s = Satelite(name, mass, radius, distance)
    print(s)
    return s