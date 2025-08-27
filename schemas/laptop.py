from pydantic import BaseModel
from typing import Optional

class LaptopBase(BaseModel):
    model_name: Optional[str] = None
    brand: Optional[str] = None
    processor_name: Optional[str] = None
    ram: Optional[int] = None
    ssd: Optional[int] = None
    hdd: Optional[int] = None
    operating_system: Optional[str] = None
    graphics: Optional[str] = None
    screen_size: Optional[float] = None
    resolution: Optional[str] = None
    core_count: Optional[int] = None

    class Config:
        populate_by_name = True

class LaptopResponse(LaptopBase):
    id: str       

    class Config:
        from_attributes = True
        populate_by_name = True
