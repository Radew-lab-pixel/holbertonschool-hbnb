from app.models.base_model import BaseModel
from app.models.user import User
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, Float, Integer
from sqlalchemy.orm import relationship


class Place(BaseModel):
    # Mapping Added for part 3 task 7
    __tablename__ = "places"
    # id , created_at , updated_at inherited from BaseModel
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    __title = Column(String[50], nullable=False)
    __description = Column(String[128], nullable=False)
    __price = Column(Float, nullable=False)
    __latitude = Column(Float, nullable=False)
    __longitude = Column(Float, nullable=False)
    __user_id = Column("user_id", )
    # example from internet ?
    # amenities_r = relationship('Amenity', secondary=place_amenity, back_populates='places_r')
    user_r = relationship("User", backref="place_r")
    reviews_r = relationship('Review', backref='place_r')
    amenities_r = relationship('Amenity', backref='place_r')

    def __init__(self, title, description, price, latitude, longitude, owner):
    # def __init__(self, title, description, price, latitude, longitude):
        super().__init__()
        
        # self.id = str(uuid.uuid4())
       
        """ Added due to 
        """
        # File "/home/oem/holbertonschool-hbnb/part2/app/persistence/repository.py", line 34, in add
        # self._storage[obj.id] = obj
        #           ^^^^^^^^^^^^^
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner   # has to be owner object 
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
    def owner(self):
        return self.__owner
    
    def owner(self, owner_input):
        self.__owner = owner_input

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
        
