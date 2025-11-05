from src.data.use_cases.interfaces.delete_registry_use_case import DeleteRegistryUseCase as UseCaseInterface
from src.infra.db.repositories.interfaces.registry_repository import RegistryRepository
from src.decorator.handle_exceptions import Exceptions
from src.errors.types import NotFoundError

class DeleteRegistryUseCase(UseCaseInterface):

    def __init__(self, registry_repository: RegistryRepository):
        self.__registry_repository = registry_repository

    @Exceptions
    def delete(self, id: int):
        registry = self.__registry_repository.delete_registry(int(id))

        if not registry:
            raise NotFoundError(f'not was founded a registry with id {id}')

        return {
            "status": 200,
            "data": {
                'success':'exit time successfully registered',
                'registry': registry.to_dict()
            }
        }
