
from sqlmodel import Field, SQLModel, Relationship
import uuid
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

class Place(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=10, max_length=500)
    location: str = Field(min_length=3, max_length=100)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    owner_id: uuid.UUID = Field(foreign_key="user.id")

    owner: "User" = Relationship(back_populates="places")
