from pydantic import BaseModel, EmailStr


class CreateCustomer(BaseModel):
    email: EmailStr
    name: str
    password: str