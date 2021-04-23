from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from blog.schemas import Blogschema, GetBlogschema, Userschema
from blog.database import get_db
from blog.services.blog_service import get_all_blogs, get_blog, create_blog, update_blog, delete_blog
from blog.oauth2 import get_current_user

router = APIRouter(tags=["Blogs"], prefix="/blog")


@router.get("/", response_model=List[GetBlogschema])
def all(db: Session = Depends(get_db), current_user: Userschema = Depends(get_current_user)):
    return get_all_blogs(db)


@router.get("/{id}", status_code=200, response_model=GetBlogschema)
def show(id: int, db: Session = Depends(get_db)):
    return get_blog(id, db)
    

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: Blogschema, db: Session = Depends(get_db)):
    return create_blog(request, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: Blogschema, db: Session = Depends(get_db)):
    return update_blog(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    return delete_blog(id, db)