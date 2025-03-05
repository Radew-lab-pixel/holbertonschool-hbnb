from typing import Union, List

from app.persistence.repository import InMemoryRepository

from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()  # ducktyping
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
    
    '''Users'''

    def create_user(self, user_data) -> User:
        # create user object
        user = User(**user_data)

        # add user to in-memory repo before returning
        self.user_repo.add(user)

        return user
    
    def get_user_by_id(self, _id) -> Union[User, None]:
        return self.user_repo.get(_id)

    def get_user_by_email(self, email) -> Union[User, None]:
        return self.user_repo.get_by_attribute("email", email)

    def get_all_users(self) -> List[User]:
        return self.user_repo.get_all()

    def update_user(self, _id, data) -> User:
        self.user_repo.update(_id, data)
        
        # check if trying to change email to one already in use
        if "email" in data:
            user_with_email = self.get_user_by_email(data["email"])
            if user_with_email and user_with_email.id != _id:
                raise ValueError('Email must be unique')

        # fetch user after update
        updated_user = self.get_user_by_id(_id)
        return updated_user

    # Placeholder method for fetching a place by ID
    # def get_place(self, place_id):
        # Logic will be implemented in later tasks
    #    return self.place_repo.get(place_id)

    '''Amenity'''
    def create_amenity(self, amenity_data) -> Amenity:
        amenity = Amenity(**amenity_data)

        self.amenity_repo.add(amenity)

        return amenity

    def get_amenity(self, amenity_id) -> Union[Amenity, None]:
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self) -> List[Amenity]:
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data) -> Amenity:
        self.amenity_repo.update(amenity_id, amenity_data)
        
        updated_amenity = self.amenity_repo.get(amenity_id)
        return updated_amenity
    
    '''Place'''
    def create_place(self, place_data):
    # Placeholder for logic to create a place, including validation for price, latitude, and longitude
        # user = User(**user_data)
        place = Place(**place_data)
        # return self.place_repo.add(place_data)
        self.place_repo.add(place)  # this object has to be in repo
        
        return place

    def get_place(self, place_id):
    # Placeholder for logic to retrieve a place by ID, including associated owner and amenities
        return self.place_repo.get(place_id)

    def get_all_places(self):
        # Placeholder for logic to retrieve all places
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
    # Placeholder for logic to update a place
        return self.place_repo.update(place_id, place_data)
    
    """Review"""
    
    def create_review(self, review_data):
    # Placeholder for logic to create a review, including validation for user_id, place_id, and rating
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
    # Placeholder for logic to retrieve a review by ID
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
    # Placeholder for logic to retrieve all reviews
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
    # Placeholder for logic to retrieve all reviews for a specific place
        return self.review_repo.get_all()

    def update_review(self, review_id, review_data):
    # Placeholder for logic to update a review
        return self.review_repo.update(review_id, review_data)

    def delete_review(self, review_id):
    # Placeholder for logic to delete a review
        return self.review_repo.delete(review_id)
