from Repository.ManagementCompanyRepository import ManagementCompanyRepository
from Repository.ServiceRepository import ServiceRepository
from Repository.ResidentialBuildingRepository import ResidentialBuildingRepository
from Repository.ApartmentRepository import ApartmentRepository
from Repository.ResidentRepository import ResidentRepository
from Repository.InvoiceRepository import InvoiceRepository

from Class.ManagementCompany import ManagementCompany
from Class.Service import Service
from Class.ResidentialBuilding import ResidentialBuilding
from Class.Apartment import Apartment
from Class.Resident import Resident
from Class.Invoice import Invoice

# Создание репозиториев
company_repo = ManagementCompanyRepository()
service_repo = ServiceRepository()
building_repo = ResidentialBuildingRepository()
apartment_repo = ApartmentRepository()
resident_repo = ResidentRepository()
invoice_repo = InvoiceRepository()

# Создание управляющих компаний
company1 = ManagementCompany(1, "УК ЖилСервис")
company2 = ManagementCompany(2, "УК ДомКомфорт")

company_repo.add_company(company1)
company_repo.add_company(company2)

# Создание услуг
service1 = Service(1, "Водоснабжение", 500)
service2 = Service(2, "Электроснабжение", 700)

service_repo.add_service(service1)
service_repo.add_service(service2)

# Создание жилого дома
building1 = ResidentialBuilding(1, "ул. Ленина, 10")
building_repo.add_building(building1)

# Создание квартир
apartment1 = Apartment(1, 50.5, 2, 101, 1)
apartment2 = Apartment(2, 65.0, 3, 102, 1)

apartment_repo.add_apartment(apartment1)
apartment_repo.add_apartment(apartment2)

# Добавление жильцов
resident1 = Resident(1, "Иванов Иван Иванович", "+79161234567")
resident2 = Resident(2, "Петров Петр Петрович", "+79169876543")

resident_repo.add_resident(resident1)
resident_repo.add_resident(resident2)

# Выписка квитанций
invoice1 = Invoice(1, 1, 1, 500)
invoice2 = Invoice(2, 2, 2, 700)

invoice_repo.add_invoice(invoice1)
invoice_repo.add_invoice(invoice2)

# Сохранение данных в XML
company_repo.save_to_xml("data/management_companies.xml")
service_repo.save_to_xml("data/services.xml")
building_repo.save_to_xml("data/buildings.xml")
apartment_repo.save_to_xml("data/apartments.xml")
resident_repo.save_to_xml("data/residents.xml")
invoice_repo.save_to_xml("data/invoices.xml")

# Загрузка данных из XML
company_repo.load_from_xml("data/management_companies.xml")
service_repo.load_from_xml("data/services.xml")
building_repo.load_from_xml("data/buildings.xml")
apartment_repo.load_from_xml("data/apartments.xml")
resident_repo.load_from_xml("data/residents.xml")
invoice_repo.load_from_xml("data/invoices.xml")

# Вывод данных
print("Управляющие компании:")
company_repo.show_companies()

print("\nУслуги:")
service_repo.show_services()

print("\nЖилые дома:")
building_repo.show_buildings()

print("\nКвартиры:")
apartment_repo.show_apartments()

print("\nЖильцы:")
resident_repo.show_residents()

print("\nКвитанции:")
invoice_repo.show_invoices()
