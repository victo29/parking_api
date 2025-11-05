from datetime import datetime, timezone

from src.utils.parking_service_helper import ParkingServiceHelper
from src.data.use_cases.interfaces.insert_registry_use_case import InsertRegistryUseCase as UseCaseInterface
from src.infra.db.repositories.interfaces.registry_repository import RegistryRepository
from src.decorator.handle_exceptions import Exceptions
from src.domains.models.registry import Registry
from src.errors.types import ExistingRegistry

helpers = ParkingServiceHelper()

class InsertRegistryUseCase(UseCaseInterface):

    def __init__(self, registry_repository: RegistryRepository):
        self.__registry_repository = registry_repository

    @Exceptions
    def insert(self, registry: Registry):

        entry_time = datetime.now(timezone.utc)
        car_plate = helpers.validate_car_plate(registry.car_plate)
        registry_open = self.__registry_repository.get_open_registries_by_plate(car_plate)
        proprietor = helpers.validate_name_proprietor(registry.proprietor)
        model = helpers.validate_model(registry.model)

        if registry_open:
            raise ExistingRegistry("there is already an open registration for this car")

        self.__registry_repository.insert_registry(
            entry_time = entry_time,
            proprietor =proprietor,
            car_plate = car_plate,
            model = model
        )

        return {"status": 201, "data": {'success':"registry added successfully"}}
