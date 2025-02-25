from app.models.base_model import BaseModel

class User(BaseModel):
    
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def delete(self):
        """Delete amenity"""
        pass