from abc import ABC, abstractmethod

class GetByPeriod(ABC):

    @abstractmethod
    def get(self, start_date: str, end_date: str):
        raise NotImplementedError("'get' must be implemented")
