from typing import Optional, List

from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    description: Optional[str] = None

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]


class ShowBlog(Blog):
    title: str
    description: str
    creator: ShowUser

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

    class Config():
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None