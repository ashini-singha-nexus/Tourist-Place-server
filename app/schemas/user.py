
from sqlmodel import SQLModel, Field
import uuid

class UserBase(SQLModel):
    username: str = Field(
        min_length=3,
        max_length=20,
        regex="^[a-zA-Z0-9_]+$"
    )
    email: str = Field(
        max_length=50,
        regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    )

class UserCreate(UserBase):
    password: str = Field(min_length=8)

class UserRead(UserBase):
    id: uuid.UUID

class UserUpdate(SQLModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None
