from pydantic import BaseModel
from typing import Optional, Union

class InternalHardDriveBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    capacity: Optional[int] = None  # GB
    price_per_gb: Optional[float] = None
    type: Optional[Union[str, int, float]] = None
    cache: Optional[int] = None
    form_factor: Optional[Union[str, int, float]] = None
    interface: Optional[str] = None

    class Config:
        populate_by_name = True

class InternalHardDriveResponse(InternalHardDriveBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
