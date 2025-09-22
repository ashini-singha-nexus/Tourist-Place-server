
from sqlmodel import SQLModel, Field
import uuid
from datetime import datetime

class PlaceBase(SQLModel):
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=10, max_length=500)
    location: str = Field(min_length=3, max_length=100)

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
