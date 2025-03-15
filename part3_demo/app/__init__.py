from flask import Flask
from flask_restx import Api

from flask_bcrypt import Bcrypt

from app.api.v1.users import api as users_nst
from app.api.v1.places import api as places_nst
from app.api.v1.amenities import api as amenities_nst
from app.api.v1.reviews import review_ns

bcrypt = Bcrypt()

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Register the users namespace
    api.add_namespace(users_nst, path='/api/v1/users')
    api.add_namespace(places_nst, path='/api/v1/places')
    api.add_namespace(amenities_nst, path='/api/v1/amenities')
    api.add_namespace(review_ns, path='/api/v1/reviews')

    bcrypt.init_app(app) # Part 3 task 1

    return app
