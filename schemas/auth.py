from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    username: str
    full_name: str | None = None

class UserResponse(UserBase):
    id: int
    email: str
    username: str
    full_name: str | None
    is_active: bool
    is_verified: bool
    created_at: datetime
    # roles: list[str]
    
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    full_name: str | None = None
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    resp: str