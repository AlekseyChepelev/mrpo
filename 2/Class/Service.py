class Service:
    def __init__(self, service_id, name, price):
        self.service_id = service_id
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.service_id == other.service_id

    def __str__(self):
        return f"Услуга: {self.name}, Цена: {self.price} (ID: {self.service_id})"