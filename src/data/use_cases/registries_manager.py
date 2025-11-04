from datetime import datetime, timezone
from typing import List, Dict
import re

from src.domains.use_cases.registries_manager import RegistriesManager as IRegistriesManager
from src.infra.db.repositories.interfaces.registry_repository import RegistryRepository
from src.infra.db.repositories.interfaces.system_config_repository import SystemConfigRepository
from src.domains.models.registry import Registry
from src.decorator.handle_exceptions import Exceptions
from src.errors.types import NotFoundConfig, NotFoundError, ExistingRegistry, DateError, ValueError

"""
    UNDER UPDATE, APPLYING THE SINGLE RESPONSBILITY CONCEPTS OF SOLID
"""

class RegistriesManager(IRegistriesManager):

    def __init__(self, registry_repository: RegistryRepository, configs_repository: SystemConfigRepository):
        self.__registry_repository = registry_repository
        self.__configs_repository =  configs_repository

    @Exceptions
    def insert_registry(self, registry: Registry):

        entry_time = datetime.now(timezone.utc)
        car_plate = self.__validate_car_plate(registry.car_plate)
        registry_open = self.__registry_repository.get_open_registries_by_plate(car_plate)
        proprietor = self.__validate_name_proprietor(registry.proprietor)
        model = self.__validate_model(registry.model)

        if registry_open:
            raise ExistingRegistry("there is already an open registration for this car")

        self.__registry_repository.insert_registry(
            entry_time = entry_time,
            proprietor =proprietor,
            car_plate = car_plate,
            model = model
        )

        return {"status": 201, "data": {'success':"registry added successfully"}}

    @Exceptions
    def register_exit(self, car_plate: str):

        exit_time = datetime.now(timezone.utc)
        car_plate = self.__validate_car_plate(car_plate)
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

    @Exceptions
    def delete_registry(self, id: int):
        registry = self.__registry_repository.delete_registry(int(id))

        if not registry:
            raise NotFoundError(f'not was founded a registry with id {id}')

        return {
            "status": 200,
            "data": {
                'success':'exit time successfully registered',
                'registry': registry.to_dict()
            }
        }

    @Exceptions
    def update_registry(self, id: int, registry: Registry):

        registry.car_plate = self.__validate_car_plate(registry.car_plate)
        registry.proprietor = self.__validate_name_proprietor(registry.proprietor)
        registry.model = self.__validate_model(registry.model)

        self.__registry_repository.update_registry(id=int(id), registry=registry)

        return {"status": 200, "data": {"success":"registry updated successfully"}}

    @Exceptions
    def get_registries_by_period(self, start_date: str, end_date: str):


        start_date, end_date = self.__convert_datas(start_date, end_date)
        self.__validate_date_range(start_date,end_date)

        regristries = self.__registry_repository.get_registries_by_period(start_date, end_date)
        regristries = [registry.to_dict() for registry  in regristries]
        total_recived = self.__calculate_total_recived(regristries)

        return {
            "status": 200,
            "data": {
                'total_recived' : total_recived,
                'total_regristries' : len(regristries),
                'regristries': regristries,
            }}

    @Exceptions
    def get_registries_specifics(self, start_date: str | None , end_date: str | None , plate:str):

        start_date, end_date = self.__convert_datas(start_date, end_date)
        self.__validate_date_range(start_date,end_date)

        plate = self.__validate_car_plate(plate)

        regristries = self.__registry_repository.get_registries_specifics(start_date, end_date, plate)
        regristries = [registry.to_dict() for registry  in regristries]
        total_recived = self.__calculate_total_recived(regristries)

        return {
            "status": 200,
            "data": {
                'total_recived' : total_recived,
                'total_regristries' : len(regristries),
                'regristries': regristries,
            }}

    @Exceptions
    def get_opened_registries(self):

        regristries = self.__registry_repository.get_opened_registries()
        regristries = [registry.to_dict() for registry  in regristries]

        return {
            "status": 200,
            "data": {
                'total_regristries' : len(regristries),
                'regristries': regristries,
            }}

    def __validate_car_plate(self, car_plate: str):
        car_plate_formatted = car_plate.strip().replace("-", "")

        if len(car_plate_formatted) != 7:
            raise ValueError("'car_plate' is invalid")

        self.__validate_special_characters(car_plate, 'car_plate')

        return car_plate_formatted.upper()

    def __validate_name_proprietor(self, proprietor: str):

        name_formatted = proprietor.strip()
        if not name_formatted.isalpha():

            raise ValueError("'proprietor' name is invalid")

        return name_formatted.upper()

    def __validate_model(self, model: str | None):
        if model:
            self.__validate_special_characters(model,'model')
        return model.upper() if model else model

    def __validate_special_characters(self, text, atribute):
        if not re.match(r'^[A-Za-z0-9]+$', text):
            raise ValueError(f"'{atribute}' must contain only letters and numbers")

        return text

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

    def __calculate_total_recived(self, registries: List[Dict]) -> float:
        total_recived = 0
        for registry in registries:
            if registry.get('value', 0):
                total_recived += registry.get('value', 0)

        return total_recived

    def __convert_datas(self, start_date, end_date):
        try:
            if start_date and end_date:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                end_date = datetime.strptime(end_date, "%Y-%m-%d")

                return (start_date, end_date)
            return (None, None)
        except Exception:
            raise DateError('start_date or end_date are not in the correct pattern (YYYY-MM-DD)')

    def __validate_date_range(self, start_date, end_date):
        if not (start_date and end_date):
            return

        if start_date > end_date:
            raise DateError("start_date must be earlier than end_date")
