from flask_restx import Namespace, Resource, fields, marshal_with
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    # @api.marshal_with(place_model, skip_none=True)  # decorator
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        

        """ Curl command
      curl -X POST http://127.0.0.1:5000/api/v1/places/ -H "Content-Type: application/json" -d '{ "title": "Cozy Apartment","description": "A nice place to stay", "price": 100.0,"latitude": 37.7749,"longitude": -122.4194,"owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"}'
    """
        
        # Placeholder for the logic to register a new place                       
             
        place_data = api.payload  # like request.get.json() ( get the data user sent to server in json)
        
        # get user.id for the place
        
        owner_id = place_data.get('owner_id')  # get owner_id value
        
        # print(f"{owner_id}")
        # user = facade.get_user_by_id(str(owner_id))
        
        existing_user = facade.get_user_by_id(place_data['owner_id'])  # existing_user is User dict
        if not existing_user:
            return {'error': 'Owner not found'}, 400
        
        new_dict = {'title': place_data['title'],
                    'description' : place_data['description'],
                    'price': place_data['price'],
                    'latitude': place_data['latitude'],
                    'longitude': place_data['longitude'],
                    'owner': existing_user}  # owner is User class object
        # place_created = facade.create_place(place_data)  # call create_place method in fascade module
        place_created = facade.create_place(new_dict)  # place_created is place object
       
        # return{"message" : "New place registered"}, 201  # has to be {} for return in flask
        # if place_created:
        # return place_created, 201   # for debugging
        print("Break 123")
        
        place_created_dict = {
                                'id': str(place_created.id),
                                'title': place_created.title,
                                'description': place_created.description,
                                'price': place_created.price,
                                'latitude': place_created.latitude,
                                'longitude': place_created.longitude,
                                # 'owner_id' : owner_id
                                'owner' : place_created.owner.id # owner is string attribute of user_id 
                                }  # output not matching the actual database, good for security (obfuscation)
        
        print(place_created_dict)
                                
        return place_created_dict, 201

    @api.response(200, 'List of places retrieved successfully')
    # @api.marshal_with(place_model)  # decorator
    # @api.marshal_with(place_model, skip_none=True)  # for debugging, skip fields / keys if value is None
    def get(self):
        """Retrieve a list of all places"""
        # Placeholder for logic to return a list of all places
        places = facade.get_all_places()  # objects places 

        output_dict = []

        for place in places:   # convert each attribute in places to dict values
            output_dict.append({
            'id': str(place.id),
            'title': place.title,
            'latitude': place.latitude,
            'longitude': place.longitude,
            })

        return output_dict, 200
        #return place_list, 200
    
@api.route('/<place_id>')
class PlaceResource(Resource):
    #@api.marshal_with(place_model)  # decorator
    @api.marshal_with(place_model,skip_none=True)
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        # Placeholder for the logic to retrieve a place by ID, including associated owner and amenities
        place = facade.get_place(place_id)  # place_list is  place object

        owner = place.owner
        
        amenities_list = []
        for amenity in place.amenities:
            amenities_list.append({
                'amenity_id': str(amenity.id),
                'name': amenity.name
            })

        output_dict = {
                        'place_id': str(place.id),
                        'title': place.title,
                        'description': place.description,
                        'latitude': place.latitude,
                        'longitude': place.longitude,
                        'owner': {
                        'owner_id': str(owner.id),
                        'first_name': owner.first_name,
                        'last_name': owner.last_name,
                        'email': owner.email
            },
            'amenities': amenities_list
           
        }
        
        return output_dict, 200
        # return place_list, 200

    @api.expect(place_model)
    # @api.marshal_with(place_model)  # decorator
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        # Placeholder for the logic to update a place by ID
        place_data_update = api.payload    # converted to json string
        place_updated = facade.update_place(place_id, place_data_update)
        print('Place updated successfully')
        return place_updated, 200
        #return {"Message: Place updated successfully"}, 200
        # pass

