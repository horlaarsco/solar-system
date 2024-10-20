import tkinter as tk
from tkinter import ttk, messagebox
import re

from planet_data import planet_data
from planet import Planet


class SolarSystemApp:
    def __init__(self, root, planets):
        self.root = root
        self.root.title("Solar System")
        self.planets = planets

        self.create_widgets()

    def create_widgets(self):

        tk.Label(
            self.root, text="Welcome to the Solar System", font=("Arial", 20)
        ).pack(padx=10, pady=10)

        instruction = (
            "Ask a question about the planets in our solar system.\n\n"
            "Examples:\n"
            "- Tell me everything about Saturn?\n"
            "- How massive is Neptune?\n"
            "- Is Pluto in the list of planets?\n"
            "- How many moons does Earth have?"
        )

        tk.Label(self.root, text=instruction, justify="left").pack(padx=10, pady=10)

        self.query_entry = tk.Entry(self.root, width=50)
        self.query_entry.bind("<KeyPress>", self.handle_enter_press)
        self.query_entry.pack(padx=10, pady=5)

        # TODO - remove this
        self.query_entry.insert(0, "How many moons does Earth have")

        tk.Button(self.root, text="Submit", command=self.process_query).pack(
            padx=10, pady=5
        )

    def process_query(self):
        query = self.query_entry.get().strip()
        if not query:
            messagebox.showwarning("Input Error", "Please enter a question.")
            return

        response = self.handle_query(query)
        messagebox.showinfo("Answer", response)

    def find_planet(self, name):
        for planet in self.planets:
            if planet["name"].lower() == name.lower():
                return Planet(
                    name=planet["name"],
                    mass=planet["mass_in_kg"],
                    distance_from_sun=planet["distance_from_sun_in_km"],
                    moons=planet["moons"],
                )

        return None

    def handle_query(self, query):
        query = query.lower()
        planet_names = [planet["name"].lower() for planet in self.planets]

        patterns = [
            (r"tell me everything about (\w+)", self.get_all_info),
            (r"how massive is (\w+)", self.get_mass),
            (r"is (\w+) in the list of planets", self.is_planet_in_list),
            (r"how many moons does (\w+) have", self.get_moon_count),
            (r"how far is (\w+) from the sun", self.get_distance_from_sun),
        ]

        for pattern, func in patterns:
            match = re.search(pattern, query)
            if match:
                planet_name = match.group(1)
                return func(planet_name)

        return "Invalid query, follow the sample instruction."

    def get_all_info(self, planet_name):
        planet = self.find_planet(planet_name)
        if planet:
            return planet
        else:
            return f"Planet {planet_name.capitalize()} not found."

    def get_mass(self, planet_name):
        planet = self.find_planet(planet_name)
        if planet:
            return planet.get_mass()
        else:
            return f"Planet {planet_name.capitalize()} not found."

    def get_distance_from_sun(self, planet_name):
        planet = self.find_planet(planet_name)
        if planet:
            return planet.get_distance_from_sun()
        else:
            return f"Planet {planet_name.capitalize()} not found."

    def is_planet_in_list(self, planet_name):
        planet = self.find_planet(planet_name)
        if planet:
            return f"Yes, {planet_name.capitalize()} is in the list of planets."
        else:
            return f"No, {planet_name.capitalize()} is not in the list of planets."

    def get_moon_count(self, planet_name):
        planet = self.find_planet(planet_name)
        if planet:
            return planet.get_moon_count()
        else:
            return f"Planet {planet_name.capitalize()} not found."

    def handle_enter_press(self, event):
        if event.keysym == "Return":
            self.process_query()


def main():
    root = tk.Tk()
    app = SolarSystemApp(root, planet_data)
    root.mainloop()


if __name__ == "__main__":
    main()


# References
# https://www.youtube.com/watch?v=ibf5cx221hk Tkinter Beginner Course - Python GUI Development
# https://www.geeksforgeeks.org/python-tkinter-messagebox-widget/
