from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class Article(BaseModel):
    title: str
    content: str
    published: bool
    class Config:
        from_attributes = True

class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] =[]
    class Config:
        from_attributes = True

class User(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    class Config:
        from_attributes = True