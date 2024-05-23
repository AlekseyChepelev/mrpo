from sqlalchemy.orm import Session
from models import ManagementCompany, Service, ResidentialBuilding, Apartment, Resident
from repositories.abstract_repository import AbstractRepository

class SQLAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, item):
        self.session.add(item)
        self.session.commit()

    def remove(self, item):
        self.session.delete(item)
        self.session.commit()

    def get(self, item_id, model):
        return self.session.query(model).get(item_id)

    def list(self, model):
        return self.session.query(model).all()

# Специфические репозитории
class ManagementCompanyRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session)

class ServiceRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session)

class ResidentialBuildingRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session)

class ApartmentRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session)

class ResidentRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session)
