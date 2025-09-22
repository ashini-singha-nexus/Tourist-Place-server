
from sqlmodel import Field, SQLModel, Relationship
import uuid
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .place import Place

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(
        unique=True, 
        index=True,
        min_length=3,
        max_length=20,
        regex="^[a-zA-Z0-9_]+$"
    )
    email: str = Field(
        unique=True, 
        index=True,
        max_length=50,
        regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    )
    hashed_password: str

    places: List["Place"] = Relationship(back_populates="owner")
