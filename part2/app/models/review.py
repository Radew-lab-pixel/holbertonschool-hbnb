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
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
   
    def create_review(self):
        # if id in self.id:
        pass

        # return (f"Review {self.id} created")

    def update_review(self):
        return 
    
    def delete_review(self):
        pass

    def list_review(self):
        pass