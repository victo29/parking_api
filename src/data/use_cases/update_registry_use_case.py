from src.utils.parking_service_helper import ParkingServiceHelper
from src.data.use_cases.interfaces.update_registry_use_case import UpdateRegistryUseCase as UseCaseInterface
from src.infra.db.repositories.interfaces.registry_repository import RegistryRepository
from src.decorator.handle_exceptions import Exceptions
from src.domains.models.registry import Registry

helpers = ParkingServiceHelper()

class UpdateRegistryUseCase(UseCaseInterface):

    def __init__(self, registry_repository: RegistryRepository):
        self.__registry_repository = registry_repository

    @Exceptions
    def update(self, id: int, registry: Registry):

        registry.car_plate = helpers.validate_car_plate(registry.car_plate)
        registry.proprietor = helpers.validate_name_proprietor(registry.proprietor)
        registry.model = helpers.validate_model(registry.model)

        self.__registry_repository.update_registry(id=int(id), registry=registry)

        return {"status": 200, "data": {"success":"registry updated successfully"}}
