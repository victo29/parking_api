from abc import ABC, abstractmethod

class GetOpenedUseCase(ABC):

    @abstractmethod
    def get(self):
        raise NotImplementedError("'get' must be implemented")
