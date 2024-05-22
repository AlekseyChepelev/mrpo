class ResidentialBuilding:
    def __init__(self, building_id, address):
        self.building_id = building_id
        self.address = address

    def __eq__(self, other):
        return self.building_id == other.building_id

    def __str__(self):
        return f"Жилой дом: {self.address} (ID: {self.building_id})"