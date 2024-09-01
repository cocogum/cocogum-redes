from typing import List, Optional
from pydantic import BaseModel

class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    phone: str

class UserCreate(UserBase):
    password: str
    roles: List[RoleCreate] = []

class User(UserBase):
    id: int
    roles: List[Role] = []

    class Config:
        orm_mode = True