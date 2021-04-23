from fastapi import FastAPI
from blog.models import Base
from blog.database import engine
from blog.routers import blog, user, authentication


app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
