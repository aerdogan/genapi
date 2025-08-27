from pydantic import BaseModel
from typing import Optional

class MouseBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    tracking_method: Optional[str] = None
    connection_type: Optional[str] = None
    max_dpi: Optional[int] = None
    hand_orientation: Optional[str] = None
    color: Optional[str] = None

    class Config:
        populate_by_name = True

class MouseResponse(MouseBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
