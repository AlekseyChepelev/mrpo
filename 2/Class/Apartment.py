class Apartment:
    def __init__(self, apartment_id, area, number_of_rooms, number, building_id):
        self.apartment_id = apartment_id
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.number = number
        self.building_id = building_id

    def __eq__(self, other):
        return self.apartment_id == other.apartment_id

    def __str__(self):
        return f"Квартира: Номер {self.number}, Площадь: {self.area} м², Кол-во комнат: {self.number_of_rooms} (ID: {self.apartment_id})"
