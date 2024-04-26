from planet import planet
from satelite import satelite
from orbit import orbital_period

def main():
    s = satelite()
    p = planet()
    print(f"The satelite will orbit at {orbital_period(s.mass, s.distance)} meters.")
    print(f"The planet will orbit at {orbital_period(p.mass, p.distance)} meters.")

if __name__ == "__main__":
    main()