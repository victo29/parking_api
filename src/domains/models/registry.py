from typing import Optional

from pydantic import BaseModel

class Registry (BaseModel):
    car_plate: str
    proprietor: str
    model: Optional[str] = None
