from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from unit_of_work import UnitOfWork
from models import ManagementCompany, Service, ResidentialBuilding, Apartment, Resident
from repositories.sqlalchemy_repository import ManagementCompanyRepository, ServiceRepository, ResidentialBuildingRepository, ApartmentRepository, ResidentRepository
from use_cases import ManagementCompanyService, ApartmentService, ResidentService, BuildingService
from schemas import ManagementCompanyCreate, ManagementCompanyResponse, ServiceCreate, ServiceResponse, ResidentialBuildingCreate, ResidentialBuildingResponse, ApartmentCreate, ApartmentResponse, ResidentCreate, ResidentResponse

app = FastAPI()

@app.post("/companies/", response_model=ManagementCompanyResponse)
def create_company(company: ManagementCompanyCreate):
    with UnitOfWork() as uow:
        company_repo = ManagementCompanyRepository(uow.session)
        new_company = ManagementCompany(name=company.name)
        company_repo.add(new_company)
        return ManagementCompanyResponse.from_orm(new_company)

@app.get("/companies/", response_model=List[ManagementCompanyResponse])
def list_companies():
    with UnitOfWork() as uow:
        company_repo = ManagementCompanyRepository(uow.session)
        companies = company_repo.list(ManagementCompany)
        return [ManagementCompanyResponse.from_orm(company) for company in companies]

@app.get("/companies/{company_id}", response_model=ManagementCompanyResponse)
def get_company(company_id: int):
    with UnitOfWork() as uow:
        company_repo = ManagementCompanyRepository(uow.session)
        company = company_repo.get(company_id, ManagementCompany)
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")
        return ManagementCompanyResponse.from_orm(company)

@app.post("/services/", response_model=ServiceResponse)
def create_service(service: ServiceCreate):
    with UnitOfWork() as uow:
        service_repo = ServiceRepository(uow.session)
        company_repo = ManagementCompanyRepository(uow.session)
        management_company_service = ManagementCompanyService(company_repo, service_repo)
        
        company = company_repo.get(service.company_id, ManagementCompany)
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")

        new_service = Service(name=service.name, price=service.price, company=company)
        management_company_service.add_service_to_company(new_service, company)
        return ServiceResponse.from_orm(new_service)

@app.get("/services/", response_model=List[ServiceResponse])
def list_services():
    with UnitOfWork() as uow:
        service_repo = ServiceRepository(uow.session)
        services = service_repo.list(Service)
        return [ServiceResponse.from_orm(service) for service in services]

@app.get("/services/{service_id}", response_model=ServiceResponse)
def get_service(service_id: int):
    with UnitOfWork() as uow:
        service_repo = ServiceRepository(uow.session)
        service = service_repo.get(service_id, Service)
        if not service:
            raise HTTPException(status_code=404, detail="Service not found")
        return ServiceResponse.from_orm(service)

@app.post("/buildings/", response_model=ResidentialBuildingResponse)
def create_building(building: ResidentialBuildingCreate):
    with UnitOfWork() as uow:
        building_repo = ResidentialBuildingRepository(uow.session)
        new_building = ResidentialBuilding(address=building.address)
        building_repo.add(new_building)
        return ResidentialBuildingResponse.from_orm(new_building)

@app.get("/buildings/", response_model=List[ResidentialBuildingResponse])
def list_buildings():
    with UnitOfWork() as uow:
        building_repo = ResidentialBuildingRepository(uow.session)
        buildings = building_repo.list(ResidentialBuilding)
        return [ResidentialBuildingResponse.from_orm(building) for building in buildings]

@app.get("/buildings/{building_id}", response_model=ResidentialBuildingResponse)
def get_building(building_id: int):
    with UnitOfWork() as uow:
        building_repo = ResidentialBuildingRepository(uow.session)
        building = building_repo.get(building_id, ResidentialBuilding)
        if not building:
            raise HTTPException(status_code=404, detail="Building not found")
        return ResidentialBuildingResponse.from_orm(building)

@app.post("/apartments/", response_model=ApartmentResponse)
def create_apartment(apartment: ApartmentCreate):
    with UnitOfWork() as uow:
        apartment_repo = ApartmentRepository(uow.session)
        building_repo = ResidentialBuildingRepository(uow.session)
        building_service = BuildingService(building_repo, apartment_repo)
        
        building = building_repo.get(apartment.building_id, ResidentialBuilding)
        if not building:
            raise HTTPException(status_code=404, detail="Building not found")

        new_apartment = Apartment(area=apartment.area, number_of_rooms=apartment.number_of_rooms, number=apartment.number, building=building)
        building_service.add_apartment_to_building(new_apartment, building)
        return ApartmentResponse.from_orm(new_apartment)

@app.get("/apartments/", response_model=List[ApartmentResponse])
def list_apartments():
    with UnitOfWork() as uow:
        apartment_repo = ApartmentRepository(uow.session)
        apartments = apartment_repo.list(Apartment)
        return [ApartmentResponse.from_orm(apartment) for apartment in apartments]

@app.get("/apartments/{apartment_id}", response_model=ApartmentResponse)
def get_apartment(apartment_id: int):
    with UnitOfWork() as uow:
        apartment_repo = ApartmentRepository(uow.session)
        apartment = apartment_repo.get(apartment_id, Apartment)
        if not apartment:
            raise HTTPException(status_code=404, detail="Apartment not found")
        return ApartmentResponse.from_orm(apartment)

@app.post("/residents/", response_model=ResidentResponse)
def create_resident(resident: ResidentCreate):
    with UnitOfWork() as uow:
        resident_repo = ResidentRepository(uow.session)
        apartment_repo = ApartmentRepository(uow.session)
        apartment_service = ApartmentService(apartment_repo, resident_repo)
        
        apartment = apartment_repo.get(resident.apartment_id, Apartment)
        if not apartment:
            raise HTTPException(status_code=404, detail="Apartment not found")

        new_resident = Resident(full_name=resident.full_name, phone=resident.phone, apartment=apartment)
        apartment_service.add_resident_to_apartment(new_resident, apartment)
        return ResidentResponse.from_orm(new_resident)

@app.get("/residents/", response_model=List[ResidentResponse])
def list_residents():
    with UnitOfWork() as uow:
        resident_repo = ResidentRepository(uow.session)
        residents = resident_repo.list(Resident)
        return [ResidentResponse.from_orm(resident) for resident in residents]

@app.get("/residents/{resident_id}", response_model=ResidentResponse)
def get_resident(resident_id: int):
    with UnitOfWork() as uow:
        resident_repo = ResidentRepository(uow.session)
        resident = resident_repo.get(resident_id, Resident)
        if not resident:
            raise HTTPException(status_code=404, detail="Resident not found")
        return ResidentResponse.from_orm(resident)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
