
from sqlmodel import SQLModel
import uuid
from datetime import datetime

class PlaceBase(SQLModel):
    title: str
    description: str
    location: str

class PlaceCreate(PlaceBase):
    pass

class PlaceRead(PlaceBase):
    id: uuid.UUID
    created_at: datetime
    owner_id: uuid.UUID

class PlaceUpdate(SQLModel):
    title: str | None = None
    description: str | None = None
    location: str | None = None
