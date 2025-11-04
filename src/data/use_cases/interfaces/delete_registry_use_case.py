from abc import ABC, abstractmethod

class DeleteRegistryUseCase(ABC):

    @abstractmethod
    def delete(self, id: int):
        raise NotImplementedError("'delete' must be implemented")
