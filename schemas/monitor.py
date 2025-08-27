from pydantic import BaseModel
from typing import Optional, List

class MonitorBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    screen_size: Optional[float] = None
    resolution: Optional[List[int]] = []  # örn: [2560, 1440]
    refresh_rate: Optional[int] = None
    response_time: Optional[int] = None
    panel_type: Optional[str] = None
    aspect_ratio: Optional[str] = None

    class Config:
        populate_by_name = True

class MonitorResponse(MonitorBase):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True
