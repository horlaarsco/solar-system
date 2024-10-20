import unittest

from planet import Planet


class TestPlanet(unittest.TestCase):
    def setUp(self):
        self.earth = Planet(
            name="Earth", mass=5.97e24, distance_from_sun=150000000.0, moons=["Moon"]
        )
        self.mars = Planet(
            name="Mars",
            mass=6.41e23,
            distance_from_sun=230000000.0,
            moons=["Phobos", "Deimos"],
        )
        self.mercury = Planet(
            name="Mercury", mass=3.30e23, distance_from_sun=70000000, moons=[]
        )

    def test_init(self):
        self.assertEqual(self.earth.name, "Earth")
        self.assertEqual(self.earth.mass, 5.97e24)
        self.assertEqual(self.earth.distance_from_sun, 150000000)
        self.assertEqual(self.earth.moons, ["Moon"])

    def test_str(self):
        expected_output = (
            "Name: Earth\n"
            "Mass: 5.97e+24 kg\n"
            "Distance from Sun: 150000000.0 km\n"
            "Moons: Moon"
        )
        self.assertEqual(str(self.earth), expected_output)

    def test_get_mass(self):
        expected_output = "Earth has a mass of 5.97e+24 kg."
        self.assertEqual(self.earth.get_mass(), expected_output)

    def test_get_distance_from_sun(self):
        expected_output = "Earth is 150000000.0 km from the sun."
        self.assertEqual(self.earth.get_distance_from_sun(), expected_output)

    def test_get_moon_count_single(self):
        expected_output = "Earth has 1 moon: Moon"
        self.assertEqual(self.earth.get_moon_count(), expected_output)

    def test_get_moon_count_multiple(self):
        expected_output = "Mars has 2 moons: Phobos, Deimos"
        self.assertEqual(self.mars.get_moon_count(), expected_output)

    def test_get_moon_count_none(self):
        expected_output = "Mercury has 0 moons"
        self.assertEqual(self.mercury.get_moon_count(), expected_output)


if __name__ == "__main__":
    unittest.main()
