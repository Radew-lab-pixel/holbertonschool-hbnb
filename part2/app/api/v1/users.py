from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})


@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')  # not meant for us for this project, use in swagger
    @api.response(400, 'Email already registered')  # but just follow the format 
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        
        # Test add user
        # curl -X POST http://localhost:5000/api/v1/users/ -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}'
        
        user_data = api.payload

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201


    @api.response(200, 'Users successfully retrieved')
    def get(self):
        """Get list of users"""
        all_users = facade.get_all_users()

        # convert User objects to python dictionaries
        data = []

        for user in all_users:
            data.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email
            })

        return data, 200


@api.route('/<user_id>')
class UserResource(Resource):  # this is special as instead of def , class is used
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user_by_id(user_id)

        if not user:
            return {'error': 'User not found'}, 404

        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200


    @api.response(200, 'User successfully updated')
    @api.response(404, 'User not found')
    @api.response(400, 'User data not valid')
    def put(self, user_id):
        """Update a user's data"""
        
        # Test this endpoint
        # curl -X PUT http://localhost:5000/api/v1/users/<user_id> -H "Content-Type: application/json" -d '{"first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com"}'

        data = api.payload
        
        # get User object with id user_id
        user = facade.get_user_by_id(user_id)
        
        if user is None:
            return {'error': 'User not found'}, 404
        
        try:
            updated_user = facade.update_user(user_id, data)

            return {
                'id': updated_user.id,
                'first_name': updated_user.first_name,
                'last_name': updated_user.last_name,
                'email': updated_user.email,
            }, 200

        except ValueError:
            return {'error': 'User data not valid'}, 400
