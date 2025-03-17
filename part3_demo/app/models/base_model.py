import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime

from app.persistence import Base

class BaseModel(Base):
    __abstract__ = True

    #def __init__(self):
    # self.id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    # self.created_at = Column(DateTime, default=datetime.now)
    # self.updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self):
        # Call parent constructor (SQLAlchemy model init)
        super().__init__()


    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Update the updated_at timestamp