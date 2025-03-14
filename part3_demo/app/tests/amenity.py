import unittest

from app.models.place import Place
from app.models.amenity import Amenity

class TestPlace(unittest.TestCase):
    
    def test_amenity_creation(self):
        amenity = Amenity(name="Wi-Fi")
        self.assertEqual(amenity.name, "Wi-Fi")


if __name__ == '__main__':
    unittest.main()