from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from passlib.context import CryptContext


pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship("Blog", back_populates="author")

    def set_password(self, password):
        self.password = pwd_ctx.hash(password)

    def check_password(self, password):
        return pwd_ctx.verify(password, self.password)


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", back_populates="blogs")
