from app.models.base_model import BaseModel
from flask_bcrypt import Bcrypt  # for part 3 task 1

"""User model aka User data layer"""

bcrypt = Bcrypt()  # for part 3 task 1

class User(BaseModel):
    
    def __init__(self, first_name, last_name, email, password,
                    is_admin = False): # password added for part 3 task 1
        super().__init__()
        self.first_name = first_name  # actually calling the setter
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = [] # List of places owned by user
        self.reviews = [] # List of reviews posted by user
        self.password = password  # Added for part 3 need parameter to be declared
        # ? self.password = db.Column(db.String(128), nullable=False) # store the hash

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
        return self.password

    def hash_password(self, password):
        """ For part 3 task 1 - Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def verify_password(self, password):
        """ For part 3 task 1- Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)


    