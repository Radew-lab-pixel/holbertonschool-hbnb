from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()  # ducktyping
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        # Logic will be implemented in later tasks
        return self.user_repo.add(user_data)

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        return self.place_repo.get(place_id)


    def create_amenity(self, amenity_data):
        # Placeholder for logic to create an amenity
        return self.amenity_repo.add(amenity_data)

    def get_amenity(self, amenity_id):
        # Placeholder for logic to retrieve an amenity by ID
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        # Placeholder for logic to retrieve all amenities
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        # Placeholder for logic to update an amenity
        return self.amenity_repo.update(amenity_id, amenity_data)