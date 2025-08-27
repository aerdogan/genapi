# schemas/sound_card.py
from pydantic import BaseModel
from typing import Optional

class SoundCardBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    channels: Optional[float] = None
    digital_audio: Optional[int] = None
    snr: Optional[int] = None
    sample_rate: Optional[int] = None
    chipset: Optional[str] = None
    interface: Optional[str] = None

    class Config:
        populate_by_name = True

class SoundCardResponse(SoundCardBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
