class Resident:
    def __init__(self, resident_id, full_name, phone):
        self.resident_id = resident_id
        self.full_name = full_name
        self.phone = phone
        self.invoices = []

    def __eq__(self, other):
        if isinstance(other, Resident):
            return self.resident_id == other.resident_id and self.full_name == other.full_name and self.phone == other.phone
        return False

    def __str__(self):
        return f"Жилец: {self.full_name}, Телефон: {self.phone} (ID: {self.resident_id})"

    @staticmethod
    def add_invoice_to_resident(invoice, resident, invoice_repo, resident_repo):
        invoice_repo.add_invoice(invoice)
        resident_repo.find_resident(resident.resident_id).invoices.append(invoice)
