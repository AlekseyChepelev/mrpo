from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ManagementCompany(Base):
    __tablename__ = "management_companies"

    company_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    services = relationship("Service", back_populates="company")

class Service(Base):
    __tablename__ = "services"

    service_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)

    company_id = Column(Integer, ForeignKey("management_companies.company_id"))
    company = relationship("ManagementCompany", back_populates="services")

class ResidentialBuilding(Base):
    __tablename__ = "residential_buildings"

    building_id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)

    apartments = relationship("Apartment", back_populates="building")

class Apartment(Base):
    __tablename__ = "apartments"

    apartment_id = Column(Integer, primary_key=True, index=True)
    area = Column(Float)
    number_of_rooms = Column(Integer)
    number = Column(Integer)

    building_id = Column(Integer, ForeignKey("residential_buildings.building_id"))
    building = relationship("ResidentialBuilding", back_populates="apartments")

    residents = relationship("Resident", back_populates="apartment")

class Resident(Base):
    __tablename__ = "residents"

    resident_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    phone = Column(String, index=True)

    apartment_id = Column(Integer, ForeignKey("apartments.apartment_id"))
    apartment = relationship("Apartment", back_populates="residents")
