from pydantic import BaseModel, ConfigDict


class RoleBase(BaseModel):
    name: str


class RoleCreate(RoleBase):
    pass


class RoleUpdate(BaseModel):
    name: str = None


class RoleDelete(BaseModel):
    id: int


class Role(RoleBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
