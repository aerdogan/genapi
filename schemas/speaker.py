# schemas/speaker.py
from pydantic import BaseModel
from typing import Optional, List

class SpeakerBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    configuration: Optional[int] = None
    wattage: Optional[float] = None
    frequency_response: Optional[List[int]] = None
    color: Optional[str] = None

    class Config:
        populate_by_name = True

class SpeakerResponse(SpeakerBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
