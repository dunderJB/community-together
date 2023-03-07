from pydantic import BaseModel


class CustomerRequest(BaseModel):
    username: str
    email: str


class CustomerResponse(BaseModel):
    id: int
    username: str
    email: str

