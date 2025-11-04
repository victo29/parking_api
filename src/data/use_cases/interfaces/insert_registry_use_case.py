from abc import ABC, abstractmethod

from src.domains.models.registry import Registry

class InsertRegistryUseCase(ABC):

    @abstractmethod
    def insert(self, registry: Registry):
        raise NotImplementedError("'insert' must be implemented")
