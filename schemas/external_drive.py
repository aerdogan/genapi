# schemas/external_drive.py
from pydantic import BaseModel
from typing import Optional

class ExternalDriveBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    type: Optional[str] = None
    interface: Optional[str] = None
    capacity: Optional[int] = None
    price_per_gb: Optional[float] = None
    color: Optional[str] = None

    class Config:
        populate_by_name = True

class ExternalDriveResponse(ExternalDriveBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
