class Resident:
    def __init__(self, resident_id, full_name, phone):
        self.resident_id = resident_id
        self.full_name = full_name
        self.phone = phone

    def __eq__(self, other):
        return self.resident_id == other.resident_id

    def __str__(self):
        return f"Жилец: {self.full_name}, Телефон: {self.phone} (ID: {self.resident_id})"