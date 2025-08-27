# schemas/wifi_card.py
from pydantic import BaseModel
from typing import Optional, Union

class WifiCardBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    protocol: Optional[str] = None
    interface: Optional[str] = None
    color: Optional[str] = None

    class Config:
        populate_by_name = True

class WifiCardResponse(WifiCardBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
