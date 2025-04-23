#!/usr/bin/python3
""" Unittests for HBnB Evolution v2 Part 4 - Review Model """

import unittest
from models.review import Review
from models.place import Place
from models.user import User
from app.persistence import db_session
from app.services.facade import HBnBFacade

class TestReview(unittest.TestCase):
    """Test that the Review model works as expected"""

    def setUp(self):
        """Set up test environment before each test"""
        self.facade = HBnBFacade()
        # Create a user and place for testing
        self.user = User(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            password="test1234"
        )
        self.place = Place(
            title="Test Apartment",
            description="A cozy place",
            price=100.0,
            latitude=37.7749,
            longitude=-122.4194,
            owner_id=self.user.id
        )
        # Save to database
        db_session.add(self.user)
        db_session.add(self.place)
        db_session.commit()

    def tearDown(self):
        """Clean up test environment after each test"""
        # Delete test data
        db_session.query(Review).delete()
        db_session.query(Place).delete()
        db_session.query(User).delete()
        db_session.commit()
        db_session.remove()

    def test_create_review(self):
        """Test creation of Review instances"""
        review = Review(
            text="Amazing stay!",
            rating=5,
            place_id=self.place.id,
            user_id=self.user.id
        )

        # Save review using facade
        self.facade.review_repo.add(review)

        # Check attributes
        self.assertEqual(review.text, "Amazing stay!")
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.place_id, self.place.id)
        self.assertEqual(review.user_id, self.user.id)
        print("Review creation test passed!")

    def test_review_validation(self):
        """Test validation of Review attributes"""
        # Test invalid rating
        with self.assertRaises(ValueError):
            Review(
                text="Invalid rating",
                rating=6,  # Should be 1-5
                place_id=self.place.id,
                user_id=self.user.id
            )

        # Test missing required fields
        with self.assertRaises(ValueError):
            Review(
                text=None,
                rating=4,
                place_id=self.place.id,
                user_id=self.user.id
            )

        print("Review validation test passed!")

    def test_review_relationships(self):
        """Test relationships between Review, Place, and User"""
        review = Review(
            text="Great location!",
            rating=4,
            place_id=self.place.id,
            user_id=self.user.id
        )
        self.facade.review_repo.add(review)

        # Check place relationship
        self.assertIn(review, self.place.reviews_r)
        # Check user relationship
        self.assertIn(review, self.user.reviews_r)
        print("Review relationships test passed!")

    def test_create_review_via_facade(self):
        """Test creating a review using the facade"""
        review_data = {
            "text": "Wonderful experience!",
            "rating": 5,
            "place_id": self.place.id,
            "user_id": self.user.id
        }
        new_review = self.facade.create_review(review_data)

        # Check if review was created
        self.assertEqual(new_review.text, "Wonderful experience!")
        self.assertEqual(new_review.rating, 5)
        # Check database
        db_review = db_session.query(Review).filter_by(id=new_review.id).first()
        self.assertIsNotNone(db_review)
        print("Review creation via facade test passed!")

if __name__ == '__main__':
    unittest.main()
