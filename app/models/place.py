
from sqlmodel import Field, SQLModel, Relationship
import uuid
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

class Place(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str
    description: str
    location: str
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    owner_id: uuid.UUID = Field(foreign_key="user.id")

    owner: "User" = Relationship(back_populates="places")
