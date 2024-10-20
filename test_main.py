import unittest
import tkinter as tk

from main import SolarSystemApp
from planet_data import planet_data
from planet import Planet


class TestSolarSystemApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.app = SolarSystemApp(self.root, planet_data)

    def test_find_planet(self):
        planet = self.app.find_planet("Earth")
        self.assertIsNotNone(planet)
        self.assertEqual(planet.name, "Earth")

        planet = self.app.find_planet("Pluto")
        self.assertIsNone(planet)

    def test_get_all_info(self):
        result = self.app.get_all_info("Earth")
        expected = (
            "Name: Earth\n"
            "Mass: 5.97e+24 kg\n"
            "Distance from Sun: 150000000.0 km\n"
            "Moons: Moon"
        )
        self.assertEqual(str(result), expected)

        result = self.app.get_all_info("Pluto")
        self.assertEqual(result, "Planet Pluto not found.")

    def test_get_mass(self):
        result = self.app.get_mass("Jupiter")
        expected = f"Jupiter has a mass of 1.9e+27 kg."
        self.assertEqual(result, expected)

        result = self.app.get_mass("Pluto")
        self.assertEqual(result, "Planet Pluto not found.")

    def test_get_distance_from_sun(self):
        result = self.app.get_distance_from_sun("Saturn")
        expected = f"Saturn is 1430000000.0 km from the sun."
        self.assertEqual(result, expected)

        result = self.app.get_distance_from_sun("Pluto")
        self.assertEqual(result, "Planet Pluto not found.")

    def test_get_moon_count(self):
        result = self.app.get_moon_count("Earth")
        expected = "Earth has 1 moon: Moon"
        self.assertEqual(result, expected)

        result = self.app.get_moon_count("Pluto")
        self.assertEqual(result, "Planet Pluto not found.")

    def test_is_planet_in_list(self):
        result = self.app.is_planet_in_list("Venus")
        expected = "Yes, Venus is in the list of planets."
        self.assertEqual(result, expected)

        result = self.app.is_planet_in_list("Pluto")
        expected = "No, Pluto is not in the list of planets."
        self.assertEqual(result, expected)

    def test_handle_query(self):
        result = self.app.handle_query("Tell me everything about Mars")
        expected = (
            "Name: Mars\n"
            "Mass: 6.41e+23 kg\n"
            "Distance from Sun: 230000000.0 km\n"
            "Moons: Phobos, Deimos"
        )
        self.assertEqual(str(result), expected)

        result = self.app.handle_query("How massive is Earth")
        expected = f"Earth has a mass of 5.97e+24 kg."
        self.assertEqual(result, expected)

        result = self.app.handle_query("Is Neptune in the list of planets")
        expected = "Yes, Neptune is in the list of planets."
        self.assertEqual(result, expected)

        result = self.app.handle_query("How many moons does Jupiter have")
        expected = "Jupiter has 4 moons: Io, Europa, Ganymede, Callisto"
        self.assertEqual(result, expected)

        result = self.app.handle_query("How far is Venus from the sun")
        expected = f"Venus is 108000000.0 km from the sun."
        self.assertEqual(result, expected)

        result = self.app.handle_query("What is the color of Mars")
        expected = "Invalid query, follow the sample instruction."
        self.assertEqual(result, expected)

    def test_handle_query_case_insensitivity(self):
        result = self.app.handle_query("tell me everything about earth")
        expected = (
            "Name: Earth\n"
            "Mass: 5.97e+24 kg\n"
            "Distance from Sun: 150000000.0 km\n"
            "Moons: Moon"
        )
        self.assertEqual(str(result), expected)

    def test_handle_query_nonexistent_planet(self):
        result = self.app.handle_query("Tell me everything about Pluto")
        expected = "Planet Pluto not found."
        self.assertEqual(result, expected)

    def tearDown(self):
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()
