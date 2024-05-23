class ManagementCompanyService:
    def __init__(self, company_repo, service_repo):
        self.company_repo = company_repo
        self.service_repo = service_repo

    def add_service_to_company(self, service, company):
        for existing_service in self.service_repo.services:
            if existing_service.service_id == service.service_id:
                raise ValueError("Service already exists in the repository")
        self.service_repo.add_service(service)
        self.company_repo.find_company(company.company_id).services.append(service)


class ApartmentService:
    def __init__(self, apartment_repo, resident_repo):
        self.apartment_repo = apartment_repo
        self.resident_repo = resident_repo

    def add_resident_to_apartment(self, resident, apartment):
        apartment_obj = self.apartment_repo.find_apartment(apartment.apartment_id)
        if apartment_obj is None:
            raise ValueError("Apartment not found")
        apartment_obj.residents.append(resident)
        self.resident_repo.add_resident(resident)


class ResidentService:
    def __init__(self, resident_repo, invoice_repo):
        self.resident_repo = resident_repo
        self.invoice_repo = invoice_repo

    def add_invoice_to_resident(self, invoice, resident):
        self.invoice_repo.add_invoice(invoice)
        self.resident_repo.find_resident(resident.resident_id).invoices.append(invoice)


class BuildingService:
    def __init__(self, building_repo, apartment_repo):
        self.building_repo = building_repo
        self.apartment_repo = apartment_repo

    def add_apartment_to_building(self, apartment, building):
        for existing_apartment in self.apartment_repo.apartments:
            if existing_apartment.apartment_id == apartment.apartment_id:
                raise ValueError("Apartment already exists in the repository")
        self.apartment_repo.add_apartment(apartment)
        self.building_repo.find_building(building.building_id).apartments.append(
            apartment
        )
