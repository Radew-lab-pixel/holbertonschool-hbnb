from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.marshal_with(amenity_model)  # decorator
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        # Placeholder for the logic to register a new amenity
        amenity_data = api.payload
        amenity_created = facade.create_amenity(amenity_data)
        return amenity_created, 201        

    @api.response(200, 'List of amenities retrieved successfully')
    @api.marshal_with(amenity_model)  # decorator
    def get(self):
        """Retrieve a list of all amenities"""
        # Placeholder for logic to return a list of all amenities
        amenity_list = facade.get_all_amenities()
        return amenity_list, 200
        

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.marshal_with(amenity_model)  # decorator
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        # Placeholder for the logic to retrieve an amenity by ID
        # amenity_data = api.payload
        amenity_list = facade.get_amenity(amenity_id)

        return amenity_list, 200


    @api.expect(amenity_model)
    @api.marshal_with(amenity_model)  # decorator
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        # Placeholder for the logic to update an amenity by ID
        pass