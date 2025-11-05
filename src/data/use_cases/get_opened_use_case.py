from datetime import datetime, timezone

from src.data.use_cases.interfaces.get_opened_use_case import GetOpenedUseCase as UseCaseInterface
from src.infra.db.repositories.interfaces.registry_repository import RegistryRepository
from src.decorator.handle_exceptions import Exceptions

class GetOpenedUseCase(UseCaseInterface):

    def __init__(self, registry_repository: RegistryRepository):
        self.__registry_repository = registry_repository

    @Exceptions
    def get(self):

        regristries = self.__registry_repository.get_opened_registries()
        regristries = [registry.to_dict() for registry  in regristries]

        return {
            "status": 200,
            "data": {
                'total_regristries' : len(regristries),
                'regristries': regristries,
            }}
