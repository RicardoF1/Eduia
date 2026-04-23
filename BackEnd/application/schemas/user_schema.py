from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    rol: str

class UserLogin(BaseModel):
    email: str
    password: str