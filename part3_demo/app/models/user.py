from app.models.base_model import BaseModel
import uuid

# from flask_bcrypt import Bcrypt

from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

bcrypt = Bcrypt()

class User(BaseModel):

    __tablename__ = 'users'
    # id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    # id inherited from BaseModel
    __first_name = Column(String(50), nullable=False)
    __last_name = Column(String(50), nullable=False)
    __email = Column(String(120), nullable=False)
    __password = Column(String(128), nullable=False)
    __is_admin = Column(Boolean, nullable=False)
    reviews_r = relationship("Review", backref="user_r")
    places_r = relationship("Place", backref="user_r")
    
    
    def __init__(self, first_name, last_name, email, password=None, is_admin = False):
        super().__init__()
        self.first_name = first_name  # actually calling the setter
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = [] # List of places owned by user
        self.reviews = [] # List of reviews posted by user
        self.password = password # Added to part 3 task 1

    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name_input):
        if not isinstance(first_name_input, str):
            raise TypeError('First name must be string')
        else:
            self.__first_name = first_name_input

    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, last_name_input):
        if not isinstance(last_name_input, str):
            raise TypeError('Last name must be string')
        else:
            self.__last_name = last_name_input

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email_input):
        if not isinstance(email_input, str):
            raise TypeError('Email must be string')
        else:
            self.__email = email_input

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, is_admin_input):
        if not isinstance(is_admin_input, bool):
            raise TypeError('Admin has to be True or False')
        else:
            self.__is_admin = is_admin_input

    """ Added for part 3 task 1"""  
    @property
    def password(self):
        """For testing only not to be deployed"""
        return self.__password

    @password.setter
    def password(self, password):
        """For testing only not to be deployed"""
        self.__password = password

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.__password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.__password, password)
