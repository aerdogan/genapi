# schemas/webcam.py
from pydantic import BaseModel
from typing import Optional, List

class WebcamBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    resolutions: Optional[List[str]] = None
    connection: Optional[str] = None
    focus_type: Optional[str] = None
    os: Optional[List[str]] = None
    fov: Optional[int] = None

    class Config:
        populate_by_name = True

class WebcamResponse(WebcamBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
