from app.models.base_model import BaseModel

class Amenity(BaseModel):
    
    def __init__(self, name):
        super().__init__()
        self.name = name
    
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