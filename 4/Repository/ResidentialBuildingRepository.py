import xml.etree.ElementTree as ET
from Class.ResidentialBuilding import ResidentialBuilding

class ResidentialBuildingRepository:
    def __init__(self):
        self.buildings = []

    def add_building(self, building: ResidentialBuilding):
        self.buildings.append(building)

    def remove_building(self, building: ResidentialBuilding):
        self.buildings.remove(building)

    def find_building(self, building_id):
        for building in self.buildings:
            if building.building_id == building_id:
                return building

    def show_buildings(self):
        for building in self.buildings:
            print(building)

    def save_to_xml(self, filename):
        root = ET.Element("ResidentialBuildings")
        for building in self.buildings:
            building_elem = ET.SubElement(root, "ResidentialBuilding")
            ET.SubElement(building_elem, "ID").text = str(building.building_id)
            ET.SubElement(building_elem, "Address").text = building.address
        tree = ET.ElementTree(root)
        tree.write(filename)

    def load_from_xml(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        self.buildings = []
        for building_elem in root.findall("ResidentialBuilding"):
            building_id = int(building_elem.find("ID").text)
            address = building_elem.find("Address").text
            self.buildings.append(ResidentialBuilding(building_id, address))
