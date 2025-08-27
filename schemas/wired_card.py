# schemas/pci_card.py
from pydantic import BaseModel
from typing import Optional, Union

class PciCardBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    interface: Optional[str] = None
    color: Optional[Union[str, None]] = None  # null değerler için esnek

    class Config:
        populate_by_name = True

class PciCardResponse(PciCardBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
