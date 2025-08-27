# schemas/gpu.py
from pydantic import BaseModel
from typing import Optional

class GPUBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    chipset: Optional[str] = None
    memory: Optional[int] = None
    core_clock: Optional[int] = None
    boost_clock: Optional[int] = None
    color: Optional[str] = None
    length: Optional[int] = None

    class Config:
        populate_by_name = True

class GPUResponse(GPUBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
