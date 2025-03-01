from typing import Union, List

from app.persistence.repository import InMemoryRepository

from app.models.user import User

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()  # ducktyping
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

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

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def create_amenity(self, amenity_data):
        return self.amenity_repo.add(amenity_data)

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        return self.amenity_repo.update(amenity_id, amenity_data)