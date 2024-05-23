import xml.etree.ElementTree as ET
from Class.Invoice import Invoice

class InvoiceRepository:
    def __init__(self):
        self.invoices = []

    def add_invoice(self, invoice: Invoice):
        self.invoices.append(invoice)

    def remove_invoice(self, invoice: Invoice):
        self.invoices.remove(invoice)

    def find_invoice(self, invoice_id):
        for invoice in self.invoices:
            if invoice.invoice_id == invoice_id:
                return invoice

    def show_invoices(self):
        for invoice in self.invoices:
            print(invoice)

    def save_to_xml(self, filename):
        root = ET.Element("Invoices")
        for invoice in self.invoices:
            invoice_elem = ET.SubElement(root, "Invoice")
            ET.SubElement(invoice_elem, "ID").text = str(invoice.invoice_id)
            ET.SubElement(invoice_elem, "ApartmentID").text = str(invoice.apartment_id)
            ET.SubElement(invoice_elem, "ServiceID").text = str(invoice.service_id)
            ET.SubElement(invoice_elem, "Price").text = str(invoice.price)
        tree = ET.ElementTree(root)
        tree.write(filename)

    def load_from_xml(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        self.invoices = []
        for invoice_elem in root.findall("Invoice"):
            invoice_id = int(invoice_elem.find("ID").text)
            apartment_id = int(invoice_elem.find("ApartmentID").text)
            service_id = int(invoice_elem.find("ServiceID").text)
            price = float(invoice_elem.find("Price").text)
            self.invoices.append(Invoice(invoice_id, apartment_id, service_id, price))
