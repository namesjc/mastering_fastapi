from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from blog.models import User
from blog.schemas import Userschema

def get_all_users(db: Session):
    users = db.query(User).all()
    return users


def get_user(id, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"detail": f"User with id {id} is not available!"})
    return user


def create_user(request: Userschema, db: Session):
    new_user = User(name=request.name, email=request.email)
    new_user.set_password(request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user