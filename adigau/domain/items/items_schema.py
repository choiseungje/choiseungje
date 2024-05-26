from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    id: int
    title: str
    time: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None

    class Config:
        from_attributes = True