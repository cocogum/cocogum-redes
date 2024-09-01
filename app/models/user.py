from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

# Tabla intermedia para la relación muchos a muchos
user_roles_table = Table(
    "user_roles",
    SQLModel.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True)
)

class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column("name", String, unique=True, nullable=False))

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(sa_column=Column("first_name", String(120), nullable=False))
    last_name: str = Field(sa_column=Column("last_name", String(255), nullable=False))
    username: str = Field(sa_column=Column("username", String(50), unique=True))
    email: str = Field(sa_column=Column("email", String(100), unique=True))
    phone: str = Field(sa_column=Column("phone", String(20), unique=True))
    password: str
    roles: List["Role"] = Relationship(back_populates="users", link_model=user_roles_table)

Role.users = Relationship(back_populates="roles", link_model=user_roles_table)