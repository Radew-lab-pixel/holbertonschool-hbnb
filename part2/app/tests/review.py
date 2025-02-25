import unittest

from app.models.review import Review

class TestReview(unittest.TestCase):
       
    def test_add(self):
        review_data = Review(text = "Review of place 1", rating = 5, place = "Happy Street, Ballarat", user = "Alice")
        
        self.assertEqual(review_data.text, "Review of place 1")
        self.assertEqual(review_data.rating, 5)
        self.assertEqual(review_data.place, "Happy Street, Ballarat")
        self.assertEqual(review_data.user, "Alice")

if __name__ == '__main__':
    unittest.main()