from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from blog.models import Blog
from blog.schemas import Blogschema


def get_all_blogs(db: Session):
    blogs = db.query(Blog).all()
    return blogs


def get_blog(id, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                            "detail": f"Blog with id {id} is not available!"})
    return blog


def create_blog(request: Blogschema, db: Session):
    print(request)
    new_blog = Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update_blog(id, request: Blogschema, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                            "detail": f"Blog with id {id} is not available!"})
    blog.title = request.title
    blog.body = request.body
    db.commit()
    return {"detail": f"Blog with id {id} is updated!"}


def delete_blog(id, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                            "detail": f"Blog with id {id} is not available!"})
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Blog with id {id} is deleted!"}
