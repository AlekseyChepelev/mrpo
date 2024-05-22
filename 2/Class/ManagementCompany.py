class ManagementCompany:
    def __init__(self, company_id, name):
        self.company_id = company_id
        self.name = name

    def __eq__(self, other):
        return self.company_id == other.company_id

    def __str__(self):
        return f"Управляющая компания: {self.name} (ID: {self.company_id})"