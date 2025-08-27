# schemas/tablet.py
from pydantic import BaseModel
from typing import Optional

class TabletBase(BaseModel):
    name: Optional[str] = None
    sim: Optional[str] = None
    battery: Optional[str] = None
    ram: Optional[str] = None
    networks: Optional[str] = None
    processor: Optional[str] = None
    screen_size: Optional[str] = None
    os: Optional[str] = None
    camera: Optional[str] = None

    class Config:
        populate_by_name = True

class TabletResponse(TabletBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
