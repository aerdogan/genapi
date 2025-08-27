# schemas/psu.py
from pydantic import BaseModel
from typing import Optional, Union

class PSUBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    type: Optional[str] = None
    efficiency: Optional[str] = None
    wattage: Optional[int] = None
    modular: Optional[Union[str, bool]] = None
    color: Optional[str] = None

    class Config:
        populate_by_name = True

class PSUResponse(PSUBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
