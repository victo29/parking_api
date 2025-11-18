from src.data.use_cases.get_by_period_use_case import GetByPeriodUseCase
from src.infra.db.repositories.registry_repository import RegistryRepository

def get_by_period_composer():

    repository = RegistryRepository()
    use_case = GetByPeriodUseCase(repository)

    return use_case.get
