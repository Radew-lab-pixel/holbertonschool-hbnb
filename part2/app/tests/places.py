import unittest

from app.models.user import User
from app.models.place import Place

class TestPlace(unittest.TestCase):
    
    def test_place_creation(self):
        owner = User(first_name="John", last_name="Smith", email="john.smith@email.com")
        place = Place(
            title="Area 51",
            description="Alien residence",
            price=1000,
            latitude=123,
            longitude=456,
            owner=owner
        )
        self.assertEqual(place.title, "Area 51")
        self.assertEqual(place.description, "Alien residence")
        self.assertEqual(place.price, 1000)
        self.assertEqual(place.latitude, 123)
        self.assertEqual(place.longitude, 456)
        self.assertEqual(place.owner, owner)


if __name__ == '__main__':
    unittest.main()