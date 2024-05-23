from pydantic import BaseModel
from typing import List

class ManagementCompanyCreate(BaseModel):
    name: str

class ManagementCompanyResponse(BaseModel):
    company_id: int
    name: str

    class Config:
        orm_mode = True
        from_attributes = True

class ServiceCreate(BaseModel):
    name: str
    price: float
    company_id: int

class ServiceResponse(BaseModel):
    service_id: int
    name: str
    price: float
    company_id: int

    class Config:
        orm_mode = True
        from_attributes = True

class ResidentialBuildingCreate(BaseModel):
    address: str

class ResidentialBuildingResponse(BaseModel):
    building_id: int
    address: str

    class Config:
        orm_mode = True
        from_attributes = True

class ApartmentCreate(BaseModel):
    area: float
    number_of_rooms: int
    number: int
    building_id: int

class ApartmentResponse(BaseModel):
    apartment_id: int
    area: float
    number_of_rooms: int
    number: int
    building_id: int

    class Config:
        orm_mode = True
        from_attributes = True

class ResidentCreate(BaseModel):
    full_name: str
    phone: str
    apartment_id: int

class ResidentResponse(BaseModel):
    resident_id: int
    full_name: str
    phone: str
    apartment_id: int

    class Config:
        orm_mode = True
        from_attributes = True
