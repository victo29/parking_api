from datetime import timedelta

from sqlalchemy import Column, String, Integer, Float, TIMESTAMP
from src.infra.db.settings.base import Base

class Registry(Base):
    __tablename__ = "registry"

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_plate = Column(String(7), nullable=False)
    proprietor = Column(String(255), nullable=False)
    model = Column(String(255))
    entry_time = Column(TIMESTAMP)
    exit_time = Column(TIMESTAMP)
    value = Column(Float)


    def to_dict(self):
        return {
            'id': self.id,
            'car_plate': self.car_plate,
            'proprietor': self.proprietor,
            'model': self.model,
            'entry_time': ((self.entry_time - timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S")) if self.entry_time else None,
            'exit_time': ((self.exit_time - timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S")) if self.exit_time else None,
            'value': self.value
        }
