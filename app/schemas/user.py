from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    first_name: str = Field(..., min_length=1, max_length=120)
    last_name: str = Field(..., min_length=1, max_length=255)
    phone: str = Field(..., pattern=r'^\+?1?\d{9,15}$')  # Validación teléfono


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    email: EmailStr = None
    first_name: str = Field(None, min_length=1, max_length=120)
    last_name: str = Field(None, min_length=1, max_length=255)
    phone: str = Field(None, pattern=r'^\+?1?\d{9,15}$')  # Validación teléfono
    password: str = Field(None, min_length=8)


class UserDelete(BaseModel):
    id: int


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
