class Planet:
    def __init__(self, name, mass, distance_from_sun, moons):
        self.name = name
        self.mass = mass
        self.distance_from_sun = distance_from_sun
        self.moons = moons

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Mass: {self.mass} kg\n"
            f"Distance from Sun: {self.distance_from_sun} km\n"
            f"Moons: {', '.join(self.moons) if self.moons else 'None'}"
        )

    def get_mass(self):
        return f"{self.name} has a mass of {self.mass} kg."

    def get_distance_from_sun(self):
        return f"{self.name} is {self.distance_from_sun} km from the sun."

    def get_moon_count(self):
        num_moons = len(self.moons)
        moon_list = ", ".join(self.moons) if self.moons else ""
        moon_word = "moon" if num_moons == 1 else "moons"
        separator = ": " if num_moons > 0 else ""

        return f"{self.name} has {num_moons} {moon_word}{separator}{moon_list}"
