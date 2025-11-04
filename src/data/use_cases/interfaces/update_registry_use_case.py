from abc import ABC, abstractmethod

from src.domains.models.registry import Registry

class UpdateRegistryUseCase(ABC):

    @abstractmethod
    def update(self, id: int, registry: Registry):
        raise NotImplementedError("'update' must be implemented")
