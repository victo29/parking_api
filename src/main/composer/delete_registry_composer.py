from src.data.use_cases.delete_registry_use_case import DeleteRegistryUseCase
from src.infra.db.repositories.registry_repository import RegistryRepository

def delete_registry_composer():

    repository = RegistryRepository()
    use_case = DeleteRegistryUseCase(repository)

    return use_case.delete
