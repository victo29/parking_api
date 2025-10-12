from datetime import date, datetime, time
from zoneinfo import ZoneInfo
from typing import List, Optional

from src.domains.models.registry import Registry
from src.infra.db.settings.connection import DBconnectionHandler
from src.infra.db.entities.registry import Registry as RegistryEntity
from src.infra.db.repositories.interfaces.registry_repository import RegistryRepository as IRegistryRepository
from src.errors.types.not_found_error import NotFoundError

class RegistryRepository(IRegistryRepository):


    def insert_registry(self, plate_car:str, proprietor:str, model:str|None, entry_time: datetime):
        with DBconnectionHandler() as database:
            try:

                new_registry = RegistryEntity(
                    plate_car = plate_car,
                    proprietor = proprietor,
                    model = model,
                    entry_time = entry_time
                )

                database.session.add(new_registry)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception

    def register_exit(self, registry: RegistryEntity):
        with DBconnectionHandler() as database:
            try:

                database.session.merge(registry)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_registry(self, id:int) -> RegistryEntity:
        with DBconnectionHandler() as database:
            try:

                registry = database.session.query(RegistryEntity).filter(RegistryEntity.id == id).first()
                if not registry:
                    raise NotFoundError(f"Registry with id {id} not found")

                database.session.delete(registry)
                database.session.commit()

                return registry

            except Exception as exception:
                database.session.rollback()
                raise exception

    def update_registry(self, id:int, registry: Registry):
        with DBconnectionHandler() as database:
            try:
                existing = database.session.get(RegistryEntity, id)

                if not existing:
                    raise NotFoundError(f"Registry with id {id} not founded")

                existing.plate_car = registry.plate_car
                existing.proprietor = registry.proprietor
                existing.model = registry.model

                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_registries_by_period(self, start_date: date, end_date: date) -> List[RegistryEntity]:
        with DBconnectionHandler() as database:
            try:

                start_utc = self.__transform_date(start_date, 'start')
                end_utc = self.__transform_date(end_date, 'end')


                registries = (
                    database.session.query(RegistryEntity)
                    .filter(RegistryEntity.entry_time >= start_utc)
                    .filter(RegistryEntity.entry_time <= end_utc)
                    .all()
                )

                return registries

            except Exception as exception:
                raise exception

    def get_registries_specifics(self, start_date: Optional[date], end_date: Optional[date], plate: str) -> List[RegistryEntity]:
        with DBconnectionHandler() as database:
            try:
                query = database.session.query(RegistryEntity).filter(RegistryEntity.plate_car == plate)

                if start_date and end_date:
                    start_datetime = self.__transform_date(start_date, 'start')
                    end_datetime = self.__transform_date(end_date, 'end')

                    query = query.filter(
                        RegistryEntity.entry_time >= start_datetime,
                        RegistryEntity.entry_time <= end_datetime
                    )

                registries = query.all()
                return registries

            except Exception as exception:
                raise exception

    def get_opened_registries(self) -> List[RegistryEntity]:
        with DBconnectionHandler() as database:
            try:

                registries = (
                    database.session.query(RegistryEntity)
                    .filter(RegistryEntity.exit_time.is_(None))
                    .all()
                )

                return registries

            except Exception as exception:
                raise exception

    def get_open_registries_by_plate(self, plate:str) -> RegistryEntity:
        with DBconnectionHandler() as database:
            try:
                registry = (
                    database.session.query(RegistryEntity)
                    .filter(RegistryEntity.plate_car == plate)
                    .filter(RegistryEntity.exit_time.is_(None))
                    .first()
                )

                return registry

            except Exception as exception:
                raise exception

    def __transform_date(self, date:date, type: str):
                tz_local = ZoneInfo("America/Sao_Paulo")
                tz_utc = ZoneInfo("UTC")

                if type == 'start':
                    start_local = datetime.combine(date, time.min).replace(tzinfo=tz_local)
                    start_utc = start_local.astimezone(tz_utc).replace(tzinfo=None)
                    return start_utc
                else:
                    end_local = datetime.combine(date, time.max).replace(tzinfo=tz_local)
                    end_utc = end_local.astimezone(tz_utc).replace(tzinfo=None)

                    return end_utc
