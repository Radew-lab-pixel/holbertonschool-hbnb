from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity'),
    'place_id': fields.String(required=True, description='Id of place')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    # @api.marshal_with(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        
        # Test this endpoint
        # curl -X POST http://localhost:5000/api/v1/amenities/ -H "Content-Type: application/json" -d '{"name": "Wi-Fi"}'
        
        amenity_data = api.payload
        place_id = amenity_data.get('place_id')
        print (str(place_id))

        try:
            new_amenity = facade.create_amenity(amenity_data)
            
            # print("id", new_amenity.id)
            print ("testing")
            return {
                "id": str(new_amenity.id),
                "name": new_amenity.name,
                "place_id": str(place_id)
            }, 201

        except ValueError:
            return {'error': 'User data not valid'}, 400    

    @api.response(200, 'List of amenities retrieved successfully')
    # @api.marshal_with(amenity_model)
    def get(self):
        """Retrieve a list of all amenities"""

        # Test this endpoint
        # curl -X GET http://localhost:5000/api/v1/amenities/ -H "Content-Type: application/json"
        
        all_amenities = facade.get_all_amenities()
        
        # convert Amenity objects to python dictionaries
        data = []

        for amenity in all_amenities:
            data.append({
                "id": str(amenity.id),
                "name": amenity.name,
            })

        return data, 200


@api.route('/<amenity_id>')
class AmenityResource(Resource):
    # @api.marshal_with(amenity_model)
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        
        # Test this endpoint
        # curl -X GET http://localhost:5000/api/v1/amenities/<amenity_id> -H "Content-Type: application/json"

        amenity = facade.get_amenity(amenity_id)

        if not amenity:
            return {'error': 'Amenity not found'}, 404

        return {
            'id': amenity.id,
            'name': amenity.name
        }, 200

    @api.expect(amenity_model)
    # @api.marshal_with(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        
        # Test this endpoint
        # curl -X POST http://localhost:5000/api/v1/amenities/<amenity_id> -H "Content-Type: application/json" -d '{"name": "Sauna"}'
        
        data = api.payload
        
        # check if amenity exists
        amenity = facade.get_amenity(amenity_id)

        if amenity is None:
            return {'error': 'Amenity not found'}, 404

        try:
            facade.update_amenity(amenity_id, data)

            return {"message": "Amenity updated successfully"}, 200

        except ValueError:
            return {'error': 'Invalid input data'}, 400
            