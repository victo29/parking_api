from src.data.use_cases.get_by_period_plate_use_case import GetByPeriodPlateUseCase
from src.infra.db.repositories.registry_repository import RegistryRepository

def get_by_period_plate_composer():

    repository = RegistryRepository()
    use_case = GetByPeriodPlateUseCase(repository)

    return use_case.get
