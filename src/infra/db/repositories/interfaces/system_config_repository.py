from abc import ABC, abstractmethod

from src.infra.db.entities.system_config import SystemConfig

class SystemConfigRepository(ABC):

    @abstractmethod
    def get_config(self, key: str) -> SystemConfig:
        pass
