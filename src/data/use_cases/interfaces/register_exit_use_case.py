from abc import ABC, abstractmethod

class RegisterExitUseCase(ABC):

    @abstractmethod
    def register(self, car_plate: str):
        raise NotImplementedError("'register' must be implemented")
