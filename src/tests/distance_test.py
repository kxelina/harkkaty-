import unittest
from entities.distance import Distance


class Testdistance(unittest.TestCase):
    def test_distance(self):
        distance = Distance()
        d = distance.distance("app", "a")  # eka kirjain
        self.assertEqual(d, 2)
        d = distance.distance("app", "ap")  # puuttuu vika kirjain
        self.assertEqual(d, 1)
        d = distance.distance("app", "app")  # oikea sana
        self.assertEqual(d, 0)
        d = distance.distance("app", "appa")  # ylimääräinen kirjain
        self.assertEqual(d, 1)
        d = distance.distance("app", "appab")  # kaks ylimääräistä kirjainta
        self.assertEqual(d, 2)

        d = distance.distance("app", "p")  # vika kirjain
        self.assertEqual(d, 2)
        d = distance.distance("app", "pp")  # kaks vikaa kirjainta
        self.assertEqual(d, 1)
        d = distance.distance("app", "ppa")  # väärinpäin sana
        self.assertEqual(d, 2)
        d = distance.distance("app", "ppab")  # väärinpäin ja lisätty kirjain
        self.assertEqual(d, 3)
        d = distance.distance("bus", "bs")  # keski kirjain otettu pois
        self.assertEqual(d, 1)
        d = distance.distance("apple", "apelp")  # väärin päin kaksi kirjainta
        self.assertEqual(d, 2)
