from pydantic import BaseModel
from typing import Optional

class KeyboardBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    style: Optional[str] = None
    switches: Optional[str] = None
    backlit: Optional[str] = None
    tenkeyless: Optional[bool] = False
    connection_type: Optional[str] = None
    color: Optional[str] = None

    class Config:
        populate_by_name = True

class KeyboardResponse(KeyboardBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
