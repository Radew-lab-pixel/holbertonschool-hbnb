#!/usr/bin/python3


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
    def __init__(self, id, text, rating, place, user, created_at, updated_at):
    super(),__init__()
    self.id = id
    self.text = text
    self.rating = rating
    self.place = place
    self.user = user
    self.created_at = created_at
    self.updated_at = updated_at
    
def create_review(self):
    pass

def update_reviw(self):
    pass
    
def delete_review(self):
    pass

def list_review(self):
    pass