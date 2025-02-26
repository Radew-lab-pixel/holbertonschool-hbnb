from app.models.base_model import BaseModel

class User(BaseModel):
    
    def __init__(self, first_name, last_name, email, is_admin = False):
        super().__init__()
        self.first_name = first_name  # actually calling the setter
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = [] # List of places owned by user
        self.reviews = [] # List of reviews posted by user

    def register(self):
        """Register a user to the application"""
        pass

    def delete(self):
        """Delete user from application"""
        pass

    @property
    def first_name(self):
        return self._first_name
    
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
    
    

    