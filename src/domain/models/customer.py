from pydantic import BaseModel, Field


class CustomerRequest(BaseModel):
    username: str = Field(alias='username')
    email: str = Field(alias='email')
    about: str = Field(alias='about', default=None)


class CustomerResponse(BaseModel):
    id: int = Field(alias='id')
    username: str = Field(alias='username')
    email: str = Field(alias='email')
    about: str = Field(alias='about', default=None)

