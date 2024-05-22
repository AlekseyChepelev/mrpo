class ManagementCompany:
    def __init__(self, company_id, name):
        self.company_id = company_id
        self.name = name
        self.services = []

    def __eq__(self, other):
        if isinstance(other, ManagementCompany):
            return self.company_id == other.company_id and self.name == other.name
        return False

    def __str__(self):
        return f"Управляющая компания: {self.name} (ID: {self.company_id})"

    @staticmethod
    def add_service_to_company(service, company, service_repo, company_repo):
        for existing_service in service_repo.services:
            if existing_service.service_id == service.service_id:
                raise ValueError("Service already exists in the repository")
        service_repo.add_service(service)
        company_repo.find_company(company.company_id).services.append(service)
