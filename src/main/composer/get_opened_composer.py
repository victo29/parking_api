from src.data.use_cases.get_opened_use_case import GetOpenedUseCase
from src.infra.db.repositories.registry_repository import RegistryRepository

def get_opened_composer():

    repository = RegistryRepository()
    use_case = GetOpenedUseCase(repository)

    return use_case.get
