from src.infra.db.repositories.interfaces.system_config_repository import SystemConfigRepository as ISystemConfigRepository

from src.infra.db.settings.connection import DBconnectionHandler
from src.infra.db.entities.system_config import SystemConfig

class SystemConfigRepository(ISystemConfigRepository):

    def get_config(self, key: str) -> SystemConfig:
        with DBconnectionHandler() as database:
            try:

                config = (
                    database.session.query(SystemConfig)
                    .filter(SystemConfig.key == key)
                    .first()
                )

                return config

            except Exception as exception:
                database.session.rollback()
                raise exception
