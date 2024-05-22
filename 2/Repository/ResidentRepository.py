import xml.etree.ElementTree as ET
from Class.Resident import Resident

class ResidentRepository:
    def __init__(self):
        self.residents = []

    def add_resident(self, resident: Resident):
        self.residents.append(resident)

    def remove_resident(self, resident: Resident):
        self.residents.remove(resident)

    def find_resident(self, resident_id):
        for resident in self.residents:
            if resident.resident_id == resident_id:
                return resident

    def show_residents(self):
        for resident in self.residents:
            print(resident)

    def save_to_xml(self, filename):
        root = ET.Element("Residents")
        for resident in self.residents:
            resident_elem = ET.SubElement(root, "Resident")
            ET.SubElement(resident_elem, "ID").text = str(resident.resident_id)
            ET.SubElement(resident_elem, "FullName").text = resident.full_name
            ET.SubElement(resident_elem, "Phone").text = resident.phone
        tree = ET.ElementTree(root)
        tree.write(filename)

    def load_from_xml(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        self.residents = []
        for resident_elem in root.findall("Resident"):
            resident_id = int(resident_elem.find("ID").text)
            full_name = resident_elem.find("FullName").text
            phone = resident_elem.find("Phone").text
            self.residents.append(Resident(resident_id, full_name, phone))
