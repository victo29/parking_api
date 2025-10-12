from typing import Optional

from pydantic import BaseModel

class Registry (BaseModel):
    plate_car: str
    proprietor: str
    model: Optional[str] = None
