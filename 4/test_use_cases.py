import unittest
from Class.Service import Service
from Class.ManagementCompany import ManagementCompany
from Class.ResidentialBuilding import ResidentialBuilding
from Class.Apartment import Apartment
from Class.Resident import Resident
from Class.Invoice import Invoice

from Repository.ServiceRepository import ServiceRepository
from Repository.ManagementCompanyRepository import ManagementCompanyRepository
from Repository.ResidentialBuildingRepository import ResidentialBuildingRepository
from Repository.ApartmentRepository import ApartmentRepository
from Repository.ResidentRepository import ResidentRepository
from Repository.InvoiceRepository import InvoiceRepository

from use_cases import ManagementCompanyService, ApartmentService, ResidentService, BuildingService

class TestUseCases(unittest.TestCase):

    def setUp(self):
        self.service_repo = ServiceRepository()
        self.company_repo = ManagementCompanyRepository()
        self.building_repo = ResidentialBuildingRepository()
        self.apartment_repo = ApartmentRepository()
        self.resident_repo = ResidentRepository()
        self.invoice_repo = InvoiceRepository()

        self.company = ManagementCompany(1, "УК ЖилСервис")
        self.company_repo.add_company(self.company)

        self.building = ResidentialBuilding(1, "ул. Ленина, 10")
        self.building_repo.add_building(self.building)

        self.apartment = Apartment(1, 50.5, 2, 101, 1)
        self.apartment_repo.add_apartment(self.apartment)

        self.resident = Resident(1, "Иванов Иван Иванович", "+79161234567")
        self.resident_repo.add_resident(self.resident)

        self.management_company_service = ManagementCompanyService(self.company_repo, self.service_repo)
        self.apartment_service = ApartmentService(self.apartment_repo, self.resident_repo)
        self.resident_service = ResidentService(self.resident_repo, self.invoice_repo)
        self.building_service = BuildingService(self.building_repo, self.apartment_repo)

    def test_add_service_to_company(self):
        service = Service(1, "Водоснабжение", 500)
        self.management_company_service.add_service_to_company(service, self.company)
        self.assertIn(service, self.service_repo.services)

    def test_add_resident_to_apartment(self):
        resident = Resident(2, "Петров Петр Петрович", "+79169876543")
        self.apartment_service.add_resident_to_apartment(resident, self.apartment)
        self.assertIn(resident, self.apartment_repo.find_apartment(1).residents)

    def test_add_invoice_to_resident(self):
        invoice = Invoice(1, 1, 1, 500)
        self.resident_service.add_invoice_to_resident(invoice, self.resident)
        self.assertIn(invoice, self.invoice_repo.invoices)

    def test_add_apartment_to_building(self):
        apartment = Apartment(2, 65.0, 3, 102, 1)
        self.building_service.add_apartment_to_building(apartment, self.building)
        self.assertIn(apartment, self.apartment_repo.apartments)

if __name__ == '__main__':
    unittest.main()
