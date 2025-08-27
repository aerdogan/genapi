from pydantic import BaseModel
from typing import Optional, List, Union

class MemoryBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    speed: Optional[Union[int, List[int]] ] = []  # örn: [4, 3200]
    modules: Optional[List[int]] = []  # örn: [2, 8]
    price_per_gb: Optional[float] = None
    color: Optional[str] = None
    first_word_latency: Optional[int] = None
    cas_latency: Optional[int] = None

    class Config:
        populate_by_name = True

class MemoryResponse(MemoryBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
