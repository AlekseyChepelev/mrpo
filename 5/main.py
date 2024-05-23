from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import ManagementCompany, Service, ResidentialBuilding, Apartment, Resident
from repositories.sqlalchemy_repository import ManagementCompanyRepository, ServiceRepository, ResidentialBuildingRepository, ApartmentRepository, ResidentRepository

# Создание таблиц
Base.metadata.create_all(bind=engine)

def main():
    session: Session = SessionLocal()

    company_repo = ManagementCompanyRepository(session)
    service_repo = ServiceRepository(session)
    building_repo = ResidentialBuildingRepository(session)
    apartment_repo = ApartmentRepository(session)
    resident_repo = ResidentRepository(session)

    # Пример использования
    company = ManagementCompany(name="УК ЖилСервис")
    company_repo.add(company)

    service = Service(name="Водоснабжение", price=500, company=company)
    service_repo.add(service)

    building = ResidentialBuilding(address="ул. Ленина, 10")
    building_repo.add(building)

    apartment = Apartment(area=50.5, number_of_rooms=2, number=101, building=building)
    apartment_repo.add(apartment)

    resident = Resident(full_name="Иванов Иван Иванович", phone="+79161234567", apartment=apartment)
    resident_repo.add(resident)

    # Пример чтения данных
    companies = company_repo.list(ManagementCompany)
    for company in companies:
        print(company)

    services = service_repo.list(Service)
    for service in services:
        print(service)

if __name__ == "__main__":
    main()
