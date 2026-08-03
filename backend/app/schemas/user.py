"""Pydantic request/response models for users and auth."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator


class UserRegister(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

    @field_validator("password")
    @classmethod
    def password_strength(cls, v: str) -> str:
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")
        if not any(c.isalpha() for c in v):
            raise ValueError("Password must contain at least one letter")
        return v


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshRequest(BaseModel):
    refresh_token: str


class UserProfileUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2, max_length=80)
    age: Optional[int] = Field(default=None, ge=10, le=100)
    education: Optional[str] = None
    stream: Optional[str] = None
    percentage: Optional[float] = Field(default=None, ge=0, le=100)
    dream_career: Optional[str] = None
    bio: Optional[str] = Field(default=None, max_length=500)
    location: Optional[str] = None


class UserOut(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: str = "user"
    age: Optional[int] = None
    education: Optional[str] = None
    stream: Optional[str] = None
    percentage: Optional[float] = None
    dream_career: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    created_at: Optional[datetime] = None
