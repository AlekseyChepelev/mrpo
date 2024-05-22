import xml.etree.ElementTree as ET
from Class.Apartment import Apartment

class ApartmentRepository:
    def __init__(self):
        self.apartments = []

    def add_apartment(self, apartment: Apartment):
        self.apartments.append(apartment)

    def remove_apartment(self, apartment: Apartment):
        self.apartments.remove(apartment)

    def find_apartment(self, apartment_id):
        for apartment in self.apartments:
            if apartment.apartment_id == apartment_id:
                return apartment

    def show_apartments(self):
        for apartment in self.apartments:
            print(apartment)

    def save_to_xml(self, filename):
        root = ET.Element("Apartments")
        for apartment in self.apartments:
            apartment_elem = ET.SubElement(root, "Apartment")
            ET.SubElement(apartment_elem, "ID").text = str(apartment.apartment_id)
            ET.SubElement(apartment_elem, "Area").text = str(apartment.area)
            ET.SubElement(apartment_elem, "NumberOfRooms").text = str(apartment.number_of_rooms)
            ET.SubElement(apartment_elem, "Number").text = str(apartment.number)
            ET.SubElement(apartment_elem, "BuildingID").text = str(apartment.building_id)
        tree = ET.ElementTree(root)
        tree.write(filename)

    def load_from_xml(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        self.apartments = []
        for apartment_elem in root.findall("Apartment"):
            apartment_id = int(apartment_elem.find("ID").text)
            area = float(apartment_elem.find("Area").text)
            number_of_rooms = int(apartment_elem.find("NumberOfRooms").text)
            number = int(apartment_elem.find("Number").text)
            building_id = int(apartment_elem.find("BuildingID").text)
            self.apartments.append(Apartment(apartment_id, area, number_of_rooms, number, building_id))
