import uuid

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email_address: str = Field(unique=True)
    external_id: str = Field(unique=True)
    created_at: int
