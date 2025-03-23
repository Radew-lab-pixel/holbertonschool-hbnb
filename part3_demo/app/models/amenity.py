from app.models.base_model import BaseModel
import uuid
from datetime import datetime
from flask import make_response
from sqlalchemy import Column, String, Boolean, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Amenity(BaseModel):
    # mapping
    __tablename__ = 'amenities'
    # id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4())) not need as in Base_Model
    __name = Column("name", String[50], nullable=False)
    # place_id = Column("place_id", String(36), ForeignKey('amenities.id'), nullable=False)
    __place_id = Column("place_id", String(36), ForeignKey('places.id'), nullable=False)

    # place_r = relationship('Place', backref='amenities_r') 
    # place_r = relationship('Place', back_populates='amenities_r')  typo error 
    # place_r = relationship('Place',back_populates='amenities_r')
    place_r = relationship('Place', back_populates='amenities_r')
    
    def __init__(self, name, place_id):
        super().__init__()
        self.__name = name
        self.__place_id = place_id

        """include due to self._storage[obj.id] = obj error"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def delete(self):
        """Delete amenity"""
        # pass
        if self.name is None:
            response = make_response ("Amenity not found")
            response.status_code = 401
            return response
        else: 
            """Delete amenity from storage"""
            self.delete

    """name"""
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name_input):
        # self.__name = name_input
        self.__name = name_input.strip()  # remove leading and trailing space

    @property
    def place_id(self):
        return self.__place_id
    
    @place_id.setter
    def place_id(self, place_id):
        self.__place_id = place_id.strip()
    