
from sqlmodel import Field, SQLModel, Relationship
import uuid
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .place import Place

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str

    places: List["Place"] = Relationship(back_populates="owner")
