from pydantic import BaseModel, EmailStr
from typing import Optional

class CustomerBase(BaseModel):
    first_name: str
    middle_name: Optional[str]
    last_name: str
    email: EmailStr
    phone_number: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: str

    class Config:
        orm_mode = True