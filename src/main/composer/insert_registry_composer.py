from src.data.use_cases.insert_registry_use_case import InsertRegistryUseCase
from src.infra.db.repositories.registry_repository import RegistryRepository

def insert_registry_composer():

    repository = RegistryRepository()
    use_case = InsertRegistryUseCase(repository)

    return use_case.insert
