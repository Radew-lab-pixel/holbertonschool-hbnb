#!/usr/bin/python3
from app.models.base_model import BaseModel
import uuid
from datetime import datetime


"""
    id (String): Unique identifier for each review.
    text (String): The content of the review. Required.
    rating (Integer): Rating given to the place, must be between 1 and 5.
    place (Place): Place instance being reviewed. Must be validated to ensure the place exists.
    user (User): User instance of who wrote the review. Must be validated to ensure the user exists.
    created_at (DateTime): Timestamp when the review is created.
    updated_at (DateTime): Timestamp when the review is last updated.
"""
class Review(BaseModel): 
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
   

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value
       
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    
    @property
    def place_id(self):
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        self._place_id = value
        

    def create_review(self):
        # if id in self.id:
        pass

        # return (f"Review {self.id} created")

    def update_review(self):
        pass 
    
    def delete_review(self):
        pass

    def list_review(self):
        pass