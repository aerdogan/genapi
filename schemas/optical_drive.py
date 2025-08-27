# schemas/optical_drive.py
from pydantic import BaseModel
from typing import Optional

class OpticalDriveBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    bd: Optional[int] = None
    dvd: Optional[int] = None
    cd: Optional[int] = None
    bd_write: Optional[str] = None
    dvd_write: Optional[str] = None
    cd_write: Optional[str] = None

    class Config:
        populate_by_name = True

class OpticalDriveResponse(OpticalDriveBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
