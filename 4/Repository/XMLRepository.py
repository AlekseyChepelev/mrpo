import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

from Class.Apartment import Apartment
from Class.ManagementCompany import ManagementCompany
from Class.Resident import Resident
from Class.ResidentialBuilding import ResidentialBuilding
from Class.Service import Service


class XMLRepository(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self):
        pass


class ManagementCompanyXMLRepository(XMLRepository):
    def save(self, data):
        root = ET.Element("ManagementCompanies")
        for company in data:
            company_elem = ET.SubElement(root, "ManagementCompany")
            ET.SubElement(company_elem, "ID").text = str(company.company_id)
            ET.SubElement(company_elem, "Name").text = company.name
        tree = ET.ElementTree(root)
        tree.write(self.file_path)

    def load(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        companies = []
        for company_elem in root.findall("ManagementCompany"):
            company_id = int(company_elem.find("ID").text)
            name = company_elem.find("Name").text
            companies.append(ManagementCompany(company_id, name))
        return companies


class ServiceXMLRepository(XMLRepository):
    def save(self, data):
        root = ET.Element("Services")
        for service in data:
            service_elem = ET.SubElement(root, "Service")
            ET.SubElement(service_elem, "ID").text = str(service.service_id)
            ET.SubElement(service_elem, "Name").text = service.name
            ET.SubElement(service_elem, "Price").text = str(service.price)
        tree = ET.ElementTree(root)
        tree.write(self.file_path)

    def load(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        services = []
        for service_elem in root.findall("Service"):
            service_id = int(service_elem.find("ID").text)
            name = service_elem.find("Name").text
            price = float(service_elem.find("Price").text)
            services.append(Service(service_id, name, price))
        return services


class ResidentialBuildingXMLRepository(XMLRepository):
    def save(self, data):
        root = ET.Element("ResidentialBuildings")
        for building in data:
            building_elem = ET.SubElement(root, "ResidentialBuilding")
            ET.SubElement(building_elem, "ID").text = str(building.building_id)
            ET.SubElement(building_elem, "Address").text = building.address
        tree = ET.ElementTree(root)
        tree.write(self.file_path)

    def load(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        buildings = []
        for building_elem in root.findall("ResidentialBuilding"):
            building_id = int(building_elem.find("ID").text)
            address = building_elem.find("Address").text
            buildings.append(ResidentialBuilding(building_id, address))
        return buildings


class ApartmentXMLRepository(XMLRepository):
    def save(self, data):
        root = ET.Element("Apartments")
        for apartment in data:
            apartment_elem = ET.SubElement(root, "Apartment")
            ET.SubElement(apartment_elem, "ID").text = str(apartment.apartment_id)
            ET.SubElement(apartment_elem, "Area").text = str(apartment.area)
            ET.SubElement(apartment_elem, "NumberOfRooms").text = str(apartment.number_of_rooms)
            ET.SubElement(apartment_elem, "Number").text = str(apartment.number)
            ET.SubElement(apartment_elem, "BuildingID").text = str(apartment.building_id)
        tree = ET.ElementTree(root)
        tree.write(self.file_path)

    def load(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        apartments = []
        for apartment_elem in root.findall("Apartment"):
            apartment_id = int(apartment_elem.find("ID").text)
            area = float(apartment_elem.find("Area").text)
            number_of_rooms = int(apartment_elem.find("NumberOfRooms").text)
            number = int(apartment_elem.find("Number").text)
            building_id = int(apartment_elem.find("BuildingID").text)
            apartments.append(Apartment(apartment_id, area, number_of_rooms, number, building_id))
        return apartments


class ResidentXMLRepository(XMLRepository):
    def save(self, data):
        root = ET.Element("Residents")
        for resident in data:
            resident_elem = ET.SubElement(root, "Resident")
            ET.SubElement(resident_elem, "ID").text = str(resident.resident_id)
            ET.SubElement(resident_elem, "FullName").text = resident.full_name
            ET.SubElement(resident_elem, "Phone").text = resident.phone
        tree = ET.ElementTree(root)
        tree.write(self.file_path)

    def load(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        residents = []
        for resident_elem in root.findall("Resident"):
            resident_id = int(resident_elem.find("ID").text)
            full_name = resident_elem.find("FullName").text
            phone = resident_elem.find("Phone").text
            residents.append(Resident(resident_id, full_name, phone))
        return residents
