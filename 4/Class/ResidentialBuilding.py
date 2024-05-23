class ResidentialBuilding:
    def __init__(self, building_id, address):
        self.building_id = building_id
        self.address = address
        self.apartments = []

    def __eq__(self, other):
        if isinstance(other, ResidentialBuilding):
            return self.building_id == other.building_id and self.address == other.address
        return False

    def __str__(self):
        return f"Жилой дом: {self.address} (ID: {self.building_id})"

    @staticmethod
    def add_apartment_to_building(apartment, building, apartment_repo, building_repo):
        for existing_apartment in apartment_repo.apartments:
            if existing_apartment.apartment_id == apartment.apartment_id:
                raise ValueError("Apartment already exists in the repository")
        apartment_repo.add_apartment(apartment)
        building_repo.find_building(building.building_id).apartments.append(apartment)
