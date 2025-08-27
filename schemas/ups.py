# schemas/ups.py
from pydantic import BaseModel
from typing import Optional

class UPSBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    capacity_w: Optional[int] = None
    capacity_va: Optional[int] = None

    class Config:
        populate_by_name = True

class UPSResponse(UPSBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
