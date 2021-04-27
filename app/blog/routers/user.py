from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from blog.schemas import Userschema, GetUserschema
from blog.database import get_db
from blog.services.user_service import get_all_users, get_user, create_user

router = APIRouter(tags=["Users"], prefix="/user")


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[GetUserschema])
def all(db: Session = Depends(get_db)):
    return get_all_users(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=GetUserschema)
def show(id: int, db: Session = Depends(get_db)):
    return get_user(id, db)


@router.post("/", response_model=GetUserschema)
def create(request: Userschema, db: Session = Depends(get_db)):
    return create_user(request, db)


# @router.put("/user/{id}", status_code=status.HTTP_202_ACCEPTED)
# def update_user(id: int, request: schemas.User, db: Session = Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.id == id)
#     if not user.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"detail": f"User with id {id} is not available!"})
#     user.update(request)
#     db.commit()
#     return {"detail": f"User with id {id} is updated!"}


# @router.delete("/user/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_user(id: int, db: Session = Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.id == id)
#     if not user.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"detail": f"User with id {id} is not available!"})
#     user.delete()
#     db.commit()
#     return {"detail": f"User with id {id} is deleted!"}
