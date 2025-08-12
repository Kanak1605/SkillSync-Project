from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
class TokenData(BaseModel):
    email: Optional[EmailStr] = None
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None
class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str]
    class Config:
        orm_mode = True
class ResumeOut(BaseModel):
    id: int
    filename: str
    raw_text: Optional[str]
    parsed_json: Optional[str]
    owner_id: int
    created_at: datetime
    class Config:
        orm_mode = True
class JobCreate(BaseModel):
    title: str
    description: str
    requirements: Optional[str] = None
class JobOut(BaseModel):
    id: int
    title: str
    description: str
    requirements: Optional[str]
    created_at: datetime
    class Config:
        orm_mode = True
