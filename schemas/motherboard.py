from pydantic import BaseModel
from typing import Optional

class MotherboardBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    socket: Optional[str] = None
    form_factor: Optional[str] = None
    max_memory: Optional[int] = None
    memory_slots: Optional[int] = None
    color: Optional[str] = None

    class Config:
        populate_by_name = True

class MotherboardResponse(MotherboardBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
