from app.models.base_model import BaseModel
from app.models.place import Place
from app.models.user import User
from sqlalchemy import Column, String, Boolean, Float, Integer
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
import uuid

class Review(BaseModel):
    """Represents a review of a place by a user in the HBnB Evolution application."""
    # mapping
    __tablename__ = 'reviews'
        
    # id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    # __text = Column(String(128), nullable=False)
    # __rating = Column(Integer, nullable=False)

    text = Column("text", String(128), nullable=False)
    rating = Column("rating", Integer, nullable=False)
    # place_id = Column(String(36), ForeignKey('place_id')) i an idiot
    place_id = Column("place_id", String(36), ForeignKey('places.id'))
    user_id = Column("user_id", String(36), ForeignKey('users.id'))
    # place_id = Column(String(36), ForeignKey('places.id'))
    # user_id = Column(String(36), ForeignKey('users.id'))
    
    # user_r = relationship('User', backref='reviews_r')   # still needed as handled by backref in Place and User
    # place_r = relationship('Place', backref='reviews_r') # still needed as handled by backref in Place

    user_r = relationship('User', back_populates='reviews_r')   # still needed as handled by backref in Place and User
    place_r = relationship('Place', back_populates='reviews_r')
   
    def __init__(self, text, rating, place, user):
        super().__init__()
        if not text or not isinstance(text, str):
            raise ValueError("Text is required and must be a string")
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError("Rating must be an integer between 1 and 5")
        if not isinstance(place, Place):
            raise ValueError("A valid Place instance is required")
        if not isinstance(user, User):
            raise ValueError("A valid User instance is required")
        
        self.text = text
        self.rating = rating
        self.place_id = place.id
        self.user_id = user.id

    def to_dict(self):
        """Convert the Review instance to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "text": self.text,
            "rating": self.rating,
            # "place_id": self.place.id,
            # "user_id": self.user.id,
            "place_id": self.place_id,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
