from app.persistence.repository import SQLAlchemyRepository
from app.persistence.user_repository import UserRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.amenity_repo = SQLAlchemyRepository(Amenity)
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)

    # In case anyone is curious about the **
    # https://www.geeksforgeeks.org/what-does-the-double-star-operator-mean-in-python/

    # --- Users ---
    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        self.user_repo.update(user_id, user_data)

    def delete_user(self, user_id):
        self.user_repo.delete(user_id)

    # --- User Relationship methods ---
    def get_user_places(self, user_id):
        owner = self.user_repo.get(user_id)
        return owner.properties_r

    def get_user_reviews(self, user_id):
        owner = self.user_repo.get(user_id)
        return owner.reviews_r


    # --- Amenities ---
    # Used during record insertion to prevent duplicate amenities
    def get_amenity_by_name(self, name):
        return self.amenity_repo.get_by_attribute('name', name)

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        self.amenity_repo.update(amenity_id, amenity_data)

    # --- Amenity Relationship methods ---
    def get_places_with_specific_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)
        return amenity.places_r


    # --- Places ---
    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        self.place_repo.update(place_id, place_data)

    # --- Place Relationship methods ---
    def get_place_amenities(self, place_id):
        place = self.place_repo.get(place_id)
        return place.amenities_r

    def get_place_reviews(self, place_id):
        place = self.place_repo.get(place_id)
        return place.reviews_r

    def get_place_owner(self, place_id):
        place = self.place_repo.get(place_id)
        return place.owner_r


    # --- Reviews ---
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return self.review_repo.get_by_attribute('place_id', place_id)

    def update_review(self, review_id, review_data):
        self.review_repo.update(review_id, review_data)

    def delete_review(self, review_id):
        self.review_repo.delete(review_id)

    # --- Review Relationship methods ---
    def get_review_writer(self, review_id):
        review = self.review_repo.get(review_id)
        return review.user_r

    def get_reviewed_place(self, review_id):
        review = self.review_repo.get(review_id)
        return review.place_r