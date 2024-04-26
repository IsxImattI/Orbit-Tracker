def orbital_period(mass, radius):
    """Calculate the orbital period using the formula for a circular orbit."""
    import math
    G = 6.67430e-11  # gravitational constant
    return 2 * math.pi * math.sqrt(radius**3 / (G * mass))