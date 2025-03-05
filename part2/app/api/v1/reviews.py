from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        # Placeholder for the logic to register a new review
        review_data = api.payload  # json list

        """check if reviewer is the owner"""
        #reviewer_user_id = review_data['user_id']  # get reviewer user id value from data parse in
        
        """disabled temporary for debugging
        # reviewer_user_id = review_data.get('user_id')
        # reviewer_place_id = review_data.get('place_id')
        
        existing_user = facade.get_user_by_id(review_data['user_id'])
        existing_place = facade.get_place(review_data['place_id'])

        # existing_place_owner_id = existing_place['owner_id']
        existing_place_owner_id = existing_place.owner.id  # read owner (owner id string) from existing place object
        if existing_place_owner_id is reviewer_user_id: # reviewer is the owner
            return {'error' : 'Reviewer is the owner'}, 400
        else:
            new_dict = {'text' : review_data['text'],
                        'rating' : review_data['rating'],
                        #'user_id' : reviewer_user_id,
                        #'place_id' : reviewer_place_id } 
                        'user_id' : review_data['user_id'],
                        'place_id': review_data['place_id']}
            print(new_dict)
               
        print(new_dict)
        review_created = facade.create_review(new_dict)
            #review_created = facade.create_review(review_data)
        return review_created, 201
        #return new_dict, 201
        """
        owner_id = review_data.get('owner_id')  # get owner_id value
              
        existing_user = facade.get_user_by_id(review_data['owner_id'])  # existing_user is User dict
        if not existing_user:
            return {'error': 'Owner not found'}, 400
        
        new_dict = {'text': review_data['text'],
                    'rating' : review_data['rating'],
                    'user_id': review_data['user_id'],
                    'place_id': review_data['place_id'] 
                    }  # owner is User class object
      
        review_created = facade.create_review(new_dict)  # place_created is place object
       
        # return{"message" : "New place registered"}, 201  # has to be {} for return in flask
        # if place_created:
        # return place_created, 201   # for debugging
        print("Break 123")
        
        place_created_dict = {
                                'id': str(review_created.id),
                                'text': review_created.,
                                'rating': review_created.rating,
                                'user_id': review_created.user_id,
                                'place_id': review_created.place_id
                                # 'owner_id' : owner_id
                                }
        
        print(place_created_dict)
       


    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        # Placeholder for logic to return a list of all reviews
        pass

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        # Placeholder for the logic to retrieve a review by ID
        pass

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        # Placeholder for the logic to update a review by ID
        pass

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        # Placeholder for the logic to delete a review
        pass

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        # Placeholder for logic to return a list of reviews for a place
        pass