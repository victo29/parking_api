from src.data.use_cases.update_registry_use_case import UpdateRegistryUseCase
from src.infra.db.repositories.registry_repository import RegistryRepository

def upadate_registry_composer():

    repository = RegistryRepository()
    use_case = UpdateRegistryUseCase(repository)

    return use_case.update
