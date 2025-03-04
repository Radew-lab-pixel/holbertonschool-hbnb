from app.models.base_model import BaseModel
import uuid
from datetime import datetime
from flask import make_response

class Amenity(BaseModel):
    
    def __init__(self, name):
        super().__init__()
        self.name = name

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

    

    