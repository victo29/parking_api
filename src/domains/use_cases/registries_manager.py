from abc import ABC, abstractmethod
from datetime import date

from src.domains.models.registry import Registry

class RegistriesManager(ABC):

    @abstractmethod
    def insert_registry(self, registry: Registry):
        pass

    @abstractmethod
    def register_exit(self, car_plate: str):
        pass

    @abstractmethod
    def delete_registry(self, id: int):
        pass

    @abstractmethod
    def update_registry(self, id: int, registry: Registry):
        pass

    @abstractmethod
    def get_registries_by_period(self, start_date: str, end_date: str):
        pass

    @abstractmethod
    def get_registries_specifics(self, start_date: str , end_date: str , plate:str):
        pass

    @abstractmethod
    def get_opened_registries(self):
        pass
