class Invoice:
    def __init__(self, invoice_id, apartment_id, service_id, price):
        self.invoice_id = invoice_id
        self.apartment_id = apartment_id
        self.service_id = service_id
        self.price = price

    def __eq__(self, other):
        return self.invoice_id == other.invoice_id

    def __str__(self):
        return f"Квитанция: Квартира ID {self.apartment_id}, Услуга ID {self.service_id}, Цена: {self.price} (ID: {self.invoice_id})"