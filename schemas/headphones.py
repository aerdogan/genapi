from pydantic import BaseModel
from typing import Optional, List

class HeadphonesBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    type: Optional[str] = None
    frequency_response: Optional[List[float]] = []  # örn: [6, 75]
    microphone: Optional[bool] = False
    wireless: Optional[bool] = False
    enclosure_type: Optional[str] = None
    color: Optional[str] = None

    class Config:
        populate_by_name = True

class HeadphonesResponse(HeadphonesBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True

