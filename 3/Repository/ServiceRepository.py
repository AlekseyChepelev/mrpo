import xml.etree.ElementTree as ET
from Class.Service import Service

class ServiceRepository:
    def __init__(self):
        self.services = []

    def add_service(self, service: Service):
        self.services.append(service)

    def remove_service(self, service: Service):
        self.services.remove(service)

    def find_service(self, service_id):
        for service in self.services:
            if service.service_id == service_id:
                return service

    def show_services(self):
        for service in self.services:
            print(service)

    def save_to_xml(self, filename):
        root = ET.Element("Services")
        for service in self.services:
            service_elem = ET.SubElement(root, "Service")
            ET.SubElement(service_elem, "ID").text = str(service.service_id)
            ET.SubElement(service_elem, "Name").text = service.name
            ET.SubElement(service_elem, "Price").text = str(service.price)
        tree = ET.ElementTree(root)
        tree.write(filename)

    def load_from_xml(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        self.services = []
        for service_elem in root.findall("Service"):
            service_id = int(service_elem.find("ID").text)
            name = service_elem.find("Name").text
            price = float(service_elem.find("Price").text)
            self.services.append(Service(service_id, name, price))
