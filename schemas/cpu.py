# schemas/cpu.py
from pydantic import BaseModel
from typing import Optional

class CPUBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    core_count: Optional[int] = None
    core_clock: Optional[float] = None
    boost_clock: Optional[float] = None
    tdp: Optional[int] = None
    graphics: Optional[str] = None
    smt: Optional[bool] = None

    class Config:
        populate_by_name = True

class CPUResponse(CPUBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
