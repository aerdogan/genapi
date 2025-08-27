# schemas/operating_system.py
from pydantic import BaseModel
from typing import List, Optional, Union

class OperatingSystemBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    mode: Optional[Union[int, List[int]]] = None
    max_memory: Optional[int] = None

    class Config:
        populate_by_name = True

class OperatingSystemResponse(OperatingSystemBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
