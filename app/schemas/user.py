
from sqlmodel import SQLModel
import uuid

class UserBase(SQLModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: uuid.UUID

class UserUpdate(SQLModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None
