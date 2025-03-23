from abc import ABC, abstractmethod
from app.persistence import db_session
import logging
from app.models.user import User
from app.models.amenity import Amenity


class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass

class SQLAlchemyRepository(Repository):
    def __init__(self, model):
        self.model = model

    def add(self, obj):
        db_session.add(obj)
        db_session.commit()

    def get(self, obj_id):
        return db_session.get(self.model, obj_id)

    def get_all(self):
        return db_session.query(self.model).all()

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            db_session.commit()

    def delete(self, obj_id):
        obj = self.get(obj_id)
        if obj:
            db_session.delete(obj)
            db_session.commit()
    
    def get_by_attribute(self, attr_name, attr_value):
        return db_session.query(self.model).filter(getattr(self.model, attr_name) == attr_value).first()
    
    """
    def get_by_attribute(self, attr_name, attr_value):
        # Ensure that attr_name corresponds to a valid attribute in the model
        if not hasattr(self.model, attr_name):
            raise ValueError(f"Attribute {attr_name} does not exist in model {self.model.__name__}")
    
        # Perform the query using getattr to dynamically access the model's attribute
        # logging.info(f"Querying for {attr_name} = {attr_value}")
        return db_session.query(self.model).filter(getattr(self.model, attr_name) == attr_value).first()
    """
    """
    def get_by_attribute(self, attr_name, attr_value):
        query = db_session.query(self.model).filter(getattr(self.model, attr_name) == attr_value)
        print("Generated SQL:", str(query.statement.compile(compile_kwargs={"literal_binds": True})))
        return query.first()
    """

"""
class UserRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(User)

    def get_by_email(self, email):
        # return super().get_by_attribute("email", email)
        
        return self.model.query.filter_by(email=email).first()
"""

class UserRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(User)
    
    def get_by_email(self, email):
        # return self.model.query.filter_by(__email=email).first()  # never use due to db_session.query(self.model)
        return super().get_by_attribute("email", email)
    
    def get_by_id(self, id):
        return super().get_by_attribute("id", id)
    
class AmenityRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Amenity)

    def get_by_place_id(self, place_id):
        return super().get_by_attribute("place_id", place_id)
