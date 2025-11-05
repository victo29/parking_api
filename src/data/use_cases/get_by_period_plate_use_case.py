
from src.utils.parking_service_helper import ParkingServiceHelper
from src.data.use_cases.interfaces.get_by_period_plate_use_case import GetByPeriodPlateUseCase as UseCaseInterface
from src.infra.db.repositories.interfaces.registry_repository import RegistryRepository
from src.decorator.handle_exceptions import Exceptions

helpers = ParkingServiceHelper()

class GetByPeriodPlateUseCase(UseCaseInterface):

    def __init__(self, registry_repository: RegistryRepository):
        self.__registry_repository = registry_repository

    @Exceptions
    def get (self, start_date: str | None , end_date: str | None , plate:str):

        start_date, end_date = helpers.convert_datas(start_date, end_date)
        helpers.validate_date_range(start_date,end_date)

        plate = helpers.validate_car_plate(plate)

        regristries = self.__registry_repository.get_registries_specifics(start_date, end_date, plate)
        regristries = [registry.to_dict() for registry  in regristries]
        total_recived = helpers.calculate_total_recived(regristries)

        return {
            "status": 200,
            "data": {
                'total_recived' : total_recived,
                'total_regristries' : len(regristries),
                'regristries': regristries,
            }}
