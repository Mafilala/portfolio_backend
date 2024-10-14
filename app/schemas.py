from os import link
from pydantic import BaseModel, EmailStr
# from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class SocialIn(BaseModel):
    link: str
    icon: str
    name: str


class SocialOut(BaseModel):
    id: int
    link: str
    icon: str
    name: str


class ProjectIn(BaseModel):
    image_url: str
    live_url: str
    name: str
    description: str


class SkillIn(BaseModel):
    icon: str
    name: str
    description: str


class AboutIn(BaseModel):
    image_url: str
    intro: str
    experience: str


class ContactIn(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    message: str
    email: str
    phone_number: str
