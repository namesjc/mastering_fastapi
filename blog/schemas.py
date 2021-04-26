from typing import List, Optional
from pydantic import BaseModel


class BlogBaseschma(BaseModel):
    title: str
    body: str


class Blogschema(BlogBaseschma):
    class Config():
        orm_mode = True


class Userschema(BaseModel):
    name: str
    email: str
    password: str


class GetUserschema(BaseModel):
    name: str
    email: str
    blogs: List[Blogschema] = []

    class Config():
        orm_mode = True


class GetBlogschema(BaseModel):
    title: str
    body: str
    author: GetUserschema

    class Config():
        orm_mode = True


class Loginschema(BaseModel):
    username: str
    password: str


class Tokenschema(BaseModel):
    access_token: str
    token_type: str


class TokenDataschema(BaseModel):
    email: Optional[str] = None


class Passwordschema(BaseModel):
    password: Optional[str] = None
