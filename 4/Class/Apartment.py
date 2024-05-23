class Apartment:
    def __init__(self, apartment_id, area, number_of_rooms, number, building_id):
        self.apartment_id = apartment_id
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.number = number
        self.building_id = building_id
        self.residents = []

    def __eq__(self, other):
        if isinstance(other, Apartment):
            return (self.apartment_id == other.apartment_id and self.area == other.area and 
                    self.number_of_rooms == other.number_of_rooms and self.number == other.number and 
                    self.building_id == other.building_id)
        return False

    def __str__(self):
        return f"Квартира: Номер {self.number}, Площадь: {self.area} м², Кол-во комнат: {self.number_of_rooms} (ID: {self.apartment_id})"

    @staticmethod
    def add_resident_to_apartment(resident, apartment, resident_repo, apartment_repo):
        apartment_repo.find_apartment(apartment.apartment_id).residents.append(resident)
        resident_repo.add_resident(resident)
