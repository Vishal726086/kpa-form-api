from pydantic import BaseModel

class FormDataBase(BaseModel):
    name: str
    phone_number: str
    district: str | None = None
    block: str | None = None
    village: str | None = None
    address: str | None = None
    category: str | None = None
    sub_category: str | None = None
    occupation: str | None = None
    organization: str | None = None

class FormDataCreate(FormDataBase):
    pass

class FormDataOut(FormDataBase):
    id: int

    class Config:
        orm_mode = True
