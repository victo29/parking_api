from src.data.use_cases.register_exit_use_case import RegisterExitUseCase
from src.infra.db.repositories.registry_repository import RegistryRepository
from src.infra.db.repositories.system_config_repository import SystemConfigRepository

def register_exit_composer():

    registry_repository = RegistryRepository()
    system_repository = SystemConfigRepository()
    use_case = RegisterExitUseCase(registry_repository=registry_repository,
                                   configs_repository= system_repository)

    return use_case.register
