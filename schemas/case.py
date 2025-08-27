# schemas/case.py
from pydantic import BaseModel
from typing import Optional, Union

class CaseBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    type: Optional[str] = None
    color: Optional[str] = None
    psu: Optional[Union[str, int]] = None
    side_panel: Optional[str] = None
    external_525_bays: Optional[int] = 0
    internal_35_bays: Optional[int] = 0

    class Config:
        populate_by_name = True

class CaseResponse(CaseBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
