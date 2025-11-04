from abc import ABC, abstractmethod

class GetByPeriodPlateUseCase(ABC):

    @abstractmethod
    def get(self, start_date: str | None , end_date: str | None , plate:str):
        raise NotImplementedError("'get' must be implemented")
