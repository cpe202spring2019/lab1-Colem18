import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_eq(self):
        loc1 = Location("Somewhere", 25.7, 56.2)
        loc2 = Location("Somewhere", 25.7, 56.2)
        loc3 = Location("Somewhere else", -19.4, 177.9)
        self.assertTrue(loc1 == loc2)
        self.assertFalse(loc1 == loc3)

if __name__ == "__main__":
        unittest.main()
