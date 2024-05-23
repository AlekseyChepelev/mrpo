import json
from abc import ABC, abstractmethod
from typing import List, Type, TypeVar

T = TypeVar('T')

class JSONRepository(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def serialize(self, item: T) -> dict:
        pass

    @abstractmethod
    def deserialize(self, data: dict) -> T:
        pass

    def add(self, item: T):
        items = self._load_all()
        items.append(self.serialize(item))
        self._save_all(items)

    def remove(self, item: T):
        items = self._load_all()
        items = [i for i in items if self.serialize(item) != i]
        self._save_all(items)

    def get(self, item_id: int, model: Type[T]) -> T:
        items = self._load_all()
        for item in items:
            if item["id"] == item_id:
                return self.deserialize(item)
        return None

    def list(self, model: Type[T]) -> List[T]:
        items = self._load_all()
        return [self.deserialize(item) for item in items]

    def _load_all(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_all(self, items):
        with open(self.file_path, 'w') as file:
            json.dump(items, file, indent=4)
