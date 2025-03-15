from flask import Flask, request, make_response
from flask_restx import Api
from app.api.v1.users import api as users_nst
from app.api.v1.places import api as places_nst
from app.api.v1.amenities import api as amenities_nst
from app.api.v1.reviews import review_ns
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()

## def create_app(): remove for part 3 task 0
def create_app(config_class="config.DevelopmentConfig"):  # added for part3 task 0
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Register the users namespace
    api.add_namespace(users_nst, path='/api/v1/users')
    api.add_namespace(places_nst, path='/api/v1/places')
    api.add_namespace(amenities_nst, path='/api/v1/amenities')
    api.add_namespace(review_ns, path='/api/v1/reviews')

    bcrypt.init_app(app)  # added for part3 task 1

    return app
