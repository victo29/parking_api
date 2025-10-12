from src.domains.use_cases.registries_manager import RegistriesManager as IRegistriesManager
from src.data.use_cases.registries_manager import RegistriesManager
from src.infra.db.repositories.registry_repository import RegistryRepository
from src.infra.db.repositories.system_config_repository import SystemConfigRepository

def registries_manager_composer() -> IRegistriesManager:

    configs_repository = SystemConfigRepository()
    registry_repository = RegistryRepository()
    use_case = RegistriesManager(
        registry_repository = registry_repository,
        configs_repository = configs_repository
    )

    return use_case
