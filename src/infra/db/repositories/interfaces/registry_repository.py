from abc import ABC, abstractmethod
from datetime import date
from typing import List
from datetime import datetime

from src.domains.models.registry import Registry
from src.infra.db.entities.registry import Registry as RegistryEntity

class RegistryRepository(ABC):

    @abstractmethod
    def insert_registry(self, car_plate:str, proprietor:str, model:str|None, entry_time: datetime):
        pass

    @abstractmethod
    def register_exit(self, registry: RegistryEntity):
        pass

    @abstractmethod
    def delete_registry(self, id: int) -> RegistryEntity:
        pass

    @abstractmethod
    def update_registry(self, id:int, registry: Registry):
        pass

    @abstractmethod
    def get_registries_by_period(self, start_date: date, end_date: date) -> List[RegistryEntity]:
        pass

    @abstractmethod
    def get_registries_specifics(self, start_date: date , end_date: date , plate:str) -> List[RegistryEntity]:
        pass

    @abstractmethod
    def get_opened_registries(self) -> List[RegistryEntity]:
        pass

    @abstractmethod
    def get_open_registries_by_plate(self, plate:str) -> RegistryEntity:
        pass
