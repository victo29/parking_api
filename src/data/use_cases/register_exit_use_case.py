from datetime import datetime, timezone

from src.utils.parking_service_helper import ParkingServiceHelper
from src.data.use_cases.interfaces.register_exit_use_case import RegisterExitUseCase as UseCaseInterface
from src.infra.db.repositories.interfaces.registry_repository import RegistryRepository
from src.infra.db.repositories.interfaces.system_config_repository import SystemConfigRepository
from src.decorator.handle_exceptions import Exceptions
from src.errors.types import NotFoundError, NotFoundConfig

helpers = ParkingServiceHelper()

class RegisterExitUseCase(UseCaseInterface):

    def __init__(self, registry_repository: RegistryRepository, configs_repository: SystemConfigRepository):
        self.__registry_repository = registry_repository
        self.__configs_repository =  configs_repository


    @Exceptions
    def register(self, car_plate: str):

        exit_time = datetime.now(timezone.utc)
        car_plate = helpers.validate_car_plate(car_plate)
        registry = self.__registry_repository.get_open_registries_by_plate(car_plate)

        if not registry:
            print(registry)
            raise NotFoundError(f"{car_plate} does not have an open registration")
        registry.exit_time = exit_time
        registry.value = self.__calculate_payment(registry.entry_time, exit_time)

        self.__registry_repository.register_exit(registry)


        return {
            "status": 200,
            "data": {
                'success':'exit time successfully registered',
                'registry': registry.to_dict()
            }
        }

    def __calculate_payment(self, entry_time: datetime, exit_time: datetime) -> float:

        value_peer_hour = self.__configs_repository.get_config('value_peer_hour')

        if not value_peer_hour:
            raise NotFoundConfig('the hourly rate has not been set')

        if entry_time.tzinfo is None:
            entry_time = entry_time.replace(tzinfo=timezone.utc)
        if exit_time.tzinfo is None:
            exit_time = exit_time.replace(tzinfo=timezone.utc)

        length_of_stay = exit_time - entry_time

        hours = length_of_stay.total_seconds() / 3600

        payment = round(hours * value_peer_hour.value , 2)

        return payment
