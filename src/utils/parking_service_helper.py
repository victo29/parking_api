from datetime import datetime
from typing import List, Dict
import re

from src.errors.types import  DateError

class ParkingServiceHelper():

    def validate_car_plate(self, car_plate: str):
        car_plate_formatted = car_plate.strip().replace("-", "")

        if len(car_plate_formatted) != 7:
            raise ValueError("'car_plate' is invalid")

        self.__validate_special_characters(car_plate, 'car_plate')

        return car_plate_formatted.upper()

    def validate_model(self, model: str | None):
        if model:
            self.__validate_special_characters(model,'model')
        return model.upper() if model else model

    @classmethod
    def validate_name_proprietor(cls, proprietor: str):

        name_formatted = proprietor.strip()
        if not name_formatted.isalpha():

            raise ValueError("'proprietor' name is invalid")

        return name_formatted.upper()

    @classmethod
    def convert_datas(cls, start_date, end_date):
        try:
            if start_date and end_date:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                end_date = datetime.strptime(end_date, "%Y-%m-%d")

                return (start_date, end_date)
            return (None, None)
        except Exception:
            raise DateError('start_date or end_date are not in the correct pattern (YYYY-MM-DD)')

    @classmethod
    def validate_date_range(cls, start_date, end_date):
        if not (start_date and end_date):
            return

        if start_date > end_date:
            raise DateError("start_date must be earlier than end_date")

    @classmethod
    def __validate_special_characters(cls, text, atribute):
        if not re.match(r'^[A-Za-z0-9]+$', text):
            raise ValueError(f"'{atribute}' must contain only letters and numbers")

        return text

    @classmethod
    def calculate_total_recived(cls, registries: List[Dict]) -> float:
        total_recived = 0
        for registry in registries:
            if registry.get('value', 0):
                total_recived += registry.get('value', 0)

        return total_recived
