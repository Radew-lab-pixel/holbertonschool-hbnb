"""API endpoints for managing reviews in the HBnB application."""

from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

review_ns = Namespace("reviews", description="Operations related to reviews")
facade = HBnBFacade()

review_model = review_ns.model("Review", {
    "id": fields.String(readonly=True, description="Unique review ID"),
    "text": fields.String(required=True, description="Review content"),
    "rating": fields.Integer(required=True, min=1, max=5, description="Rating (1-5)"),
    "place_id": fields.String(required=True, description="ID of the place"),
    "user_id": fields.String(required=True, description="ID of the user"),
    "created_at": fields.String(readonly=True, description="Creation timestamp"),
    "updated_at": fields.String(readonly=True, description="Last update timestamp")
})

@review_ns.route("")
class ReviewList(Resource):
    """Handles listing and creating reviews."""

    @review_ns.doc("list_reviews")
    @review_ns.marshal_list_with(review_model)
    def get(self):
        """Retrieve a list of all reviews."""
        reviews = facade.get_all_reviews()
        return [r.to_dict() for r in reviews], 200

    @review_ns.doc("create_review")
    @review_ns.expect(review_model)
    @review_ns.marshal_with(review_model, code=201)
    def post(self):
        """Create a new review."""
        data = review_ns.payload
        try:
            review = facade.create_review(
                data["text"],
                data["rating"],
                data["place_id"],
                data["user_id"]
            )
            return review.to_dict(), 201
        except ValueError as e:
            review_ns.abort(400, str(e))

@review_ns.route("/<string:review_id>")
class Review(Resource):
    """Handles operations on a single review."""

    @review_ns.doc("get_review")
    @review_ns.marshal_with(review_model)
    def get(self, review_id):
        """Retrieve a specific review by ID."""
        review = facade.get_review(review_id)
        if not review:
            review_ns.abort(404, "Review not found")
        return review.to_dict(), 200

    @review_ns.doc("update_review")
    @review_ns.expect(review_model)
    @review_ns.marshal_with(review_model)
    def put(self, review_id):
        """Update an existing review."""
        data = review_ns.payload
        try:
            review = facade.update_review(review_id, data["text"], data["rating"])
            return review.to_dict(), 200
        except ValueError as e:
            review_ns.abort(404, str(e))

    @review_ns.doc("delete_review")
    @review_ns.marshal_with(review_model, code=204)
    def delete(self, review_id):
        """Delete a review by ID."""
        try:
            facade.delete_review(review_id)
            return {"message": "Review deleted"}, 204
        except ValueError as e:
            review_ns.abort(404, str(e))

@review_ns.route("/place/<string:place_id>")
class PlaceReviews(Resource):
    """Handles retrieving reviews for a specific place."""

    @review_ns.doc("get_place_reviews")
    @review_ns.marshal_list_with(review_model)
    def get(self, place_id):
        """Retrieve all reviews for a specific place."""
        try:
            reviews = facade.get_reviews_by_place(place_id)
            return [r.to_dict() for r in reviews], 200
        except ValueError as e:
            review_ns.abort(404, str(e))
