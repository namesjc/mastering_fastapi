from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from blog.database import get_db
from blog.models import User
from blog.schemas import Passwordschema


security = HTTPBasic()


def get_current_username_basic(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    username = db.query(User).filter_by(email=credentials.username).first()
    password_verify = username.check_password(credentials.password)
    if not password_verify:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    password_data = Passwordschema(password=password_verify)
