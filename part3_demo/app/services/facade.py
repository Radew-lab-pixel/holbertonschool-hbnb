from typing import Union, List
from app.persistence.repository import SQLAlchemyRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.persistence.repository import UserRepository

class HBnBFacade:
    """Facade class to manage interactions between business logic entities and repositories.

    Attributes:
        user_repo (SQLAlchemyRepository): Repository for User objects.
        place_repo (SQLAlchemyRepository): Repository for Place objects.
        review_repo (SQLAlchemyRepository): Repository for Review objects.
        amenity_repo (SQLAlchemyRepository): Repository for Amenity objects.
    """

    def __init__(self):
        """Initialize the Facade with in-memory repositories for each entity."""
        # self.user_repo = SQLAlchemyRepository(User)
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)
        self.amenity_repo = SQLAlchemyRepository(Amenity)
        self.user_repo = UserRepository()
        

    '''Users'''
    def create_user(self, user_data) -> User:
        """Create a new user and store it in the repository."""
        user = User(**user_data)
        self.user_repo.add(user)
        return user
    
    def get_user_by_id(self, id) -> Union[User, None]:
        """Retrieve a user by their ID."""
        # return self.user_repo.get(id)
        return self.user_repo.get_by_id(id)
    """
    def get_user_by_email(self, email) -> Union[User, None]:
        # Retrieve a user by their email.
        # return self.user_repo.get_by_attribute("email", email)
        return self.user_repo.get_by_attribute("email", email)
    """    
    def get_user_by_email(self, email):
        """Retrieve a user by their email."""
        # return self.user_repo.get_by_attribute("email", email)
        # return self.user_repo.get_by_attribute("email", email)
        return self.user_repo.get_by_email(email)
        # return self.user_repo.get_user_by_email(email)

    def get_all_users(self) -> List[User]:
        """Retrieve all users."""
        return self.user_repo.get_all()

    def update_user(self, _id, data) -> User:
        """Update an existing user's attributes."""
        if "email" in data:
            user_with_email = self.get_user_by_email(data["email"])
            if user_with_email and user_with_email.id != _id:
                raise ValueError('Email must be unique')
        self.user_repo.update(_id, data)
        return self.get_user_by_id(_id)
    
    def get_user(self, user_id):
        return self.user_repo.get(user_id)
    
    '''Places'''
    def create_place(self, place_data) -> Place:
        """Create a new place and store it in the repository."""
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id) -> Union[Place, None]:
        """Retrieve a place by its ID."""
        return self.place_repo.get(place_id)
    
    def get_all_places(self) -> List[Place]:
        """Retrieve all places."""
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
    # Placeholder for logic to update a place
        return self.place_repo.update(place_id, place_data)

    def create_amenity(self, amenity_data) -> Amenity:
        """Create a new amenity and store it in the repository."""
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id) -> Union[Amenity, None]:
        """Retrieve an amenity by its ID."""
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self) -> List[Amenity]:
        """Retrieve all amenities."""
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data) -> Amenity:
        """Update an existing amenity's attributes."""
        self.amenity_repo.update(amenity_id, amenity_data)
        return self.get_amenity(amenity_id)

    def create_review(self, text: str, rating: int, place_id: str, user_id: str) -> Review:
        """Create a new review and associate it with a place and user."""
        place = self.place_repo.get(place_id)
        user = self.user_repo.get(user_id)
        if not place:
            raise ValueError("Place not found")
        if not user:
            raise ValueError("User not found")
        
        review = Review(text, rating, place, user)
        self.review_repo.add(review)
        place.add_review(review)
        user.reviews.append(review)
        self.place_repo.update(place_id, {"reviews": place.reviews})
        self.user_repo.update(user_id, {"reviews": user.reviews})
        return review

    def get_review(self, review_id: str) -> Union[Review, None]:
        """Retrieve a review by its ID."""
        return self.review_repo.get(review_id)

    def get_all_reviews(self) -> List[Review]:
        """Retrieve all reviews."""
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id: str) -> List[Review]:
        """Retrieve all reviews for a specific place."""
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found")
        return place.reviews

    def update_review(self, review_id: str, text: str, rating: int) -> Review:
        """Update an existing review's text and rating."""
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found")
        data = {"text": text, "rating": rating}
        self.review_repo.update(review_id, data)
        return self.review_repo.get(review_id)

    def delete_review(self, review_id: str) -> None:
        """Delete a review and remove it from associated place and user."""
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found")
        self.review_repo.delete(review_id)
        review.place.reviews.remove(review)
        review.user.reviews.remove(review)
        self.place_repo.update(review.place.id, {"reviews": review.place.reviews})
        self.user_repo.update(review.user.id, {"reviews": review.user.reviews})
        