from abc import ABC, abstractmethod

class AbstractRepository(ABC):
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def remove(self, item):
        pass

    @abstractmethod
    def get(self, item_id):
        pass

    @abstractmethod
    def list(self):
        pass
