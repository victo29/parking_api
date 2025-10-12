from sqlalchemy import Column, String, Integer, Float, TIMESTAMP
from src.infra.db.settings.base import Base

class SystemConfig(Base):
    __tablename__ = "system_config"

    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(50))
    value = Column(Float)
