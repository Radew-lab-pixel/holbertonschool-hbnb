from app.models.base_model import BaseModel
# from app.models.user import User  # Circular import issue 
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, Float, Integer
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey;


class Place(BaseModel):
    # Mapping Added for part 3 task 7
    __tablename__ = "places"
    # id , created_at , updated_at inherited from BaseModel
    # id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    __title = Column("title", String[50], nullable=False)
    __description = Column("description", String[128], nullable=False)
    __price = Column("price", Float, nullable=False)
    __latitude = Column("latitude", Float, nullable=False)
    __longitude = Column("longitude", Float, nullable=False)
    # user_id = Column(String(36), ForeignKey("users.id"))
    __owner_id = Column("owner_id", String(36), ForeignKey('users.id'), nullable=False)

    # example from internet ?
    # amenities_r = relationship('Amenity', secondary=place_amenity, back_populates='places_r')
    # user_r = relationship('User', backref="place")
    # reviews_r = relationship('Review', backref='place')
    # amenities_r = relationship('Amenity', backref='place')
    user_r = relationship('User', back_populates='place_r')
    # reviews_r = relationship('Review', back_populates='placse_r')
    amenities_r = relationship('Amenity', back_populates='place_r')
    reviews_r = relationship('Review', back_populates='place_r')
    

    def __init__(self, title, description, price, latitude, longitude, owner_id):
    # def __init__(self, title, description, price, latitude, longitude):
        super().__init__()
        
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id   # has to be owner object 
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    """Add getter and setter for each instances"""
    """title"""
    @property
    def title(self):
        return self.__title
        # return self._title

    @title.setter
    def title(self, title_input):
        self.__title = title_input
        # self._title = title_input
        # return self.__title  # not needed in setter

    """description"""
    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, description_input):
        self.__description = description_input

    """price"""
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price_input):
        self.__price = price_input
    
    """latitude"""
    @property
    def latitude(self):
        return self.__latitude
    
    @latitude.setter
    def latitude(self, latitude_input):
        self.__latitude = latitude_input

    """longitude """
    @property
    def longitude(self):
        return self.__longitude
    
    @longitude.setter
    def longitude(self, longitude_input):
        self.__longitude = longitude_input
    
    """owner"""
    @property
    def owner_id(self):
        return self.__owner_id
    
    @owner_id.setter
    def owner_id(self, owner_input):
        self.__owner_id = owner_input

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)
        
    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
        
