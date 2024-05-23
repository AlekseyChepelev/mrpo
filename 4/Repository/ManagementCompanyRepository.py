import xml.etree.ElementTree as ET
from Class.ManagementCompany import ManagementCompany

class ManagementCompanyRepository:
    def __init__(self):
        self.management_companies = []

    def add_company(self, company: ManagementCompany):
        self.management_companies.append(company)

    def remove_company(self, company: ManagementCompany):
        self.management_companies.remove(company)

    def find_company(self, company_id):
        for company in self.management_companies:
            if company.company_id == company_id:
                return company

    def show_companies(self):
        for company in self.management_companies:
            print(company)

    def save_to_xml(self, filename):
        root = ET.Element("ManagementCompanies")
        for company in self.management_companies:
            company_elem = ET.SubElement(root, "ManagementCompany")
            ET.SubElement(company_elem, "ID").text = str(company.company_id)
            ET.SubElement(company_elem, "Name").text = company.name
        tree = ET.ElementTree(root)
        tree.write(filename)

    def load_from_xml(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        self.management_companies = []
        for company_elem in root.findall("ManagementCompany"):
            company_id = int(company_elem.find("ID").text)
            name = company_elem.find("Name").text
            self.management_companies.append(ManagementCompany(company_id, name))
