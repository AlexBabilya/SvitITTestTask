from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from modules.user.crud import get_user_by_email, create_user
from modules.user.schemas import User, UserCreate, UserLogin
from modules.database import get_db
from .utils import verify_password, create_access_token

auth_router = APIRouter()

@auth_router.post("/signup", response_model=User)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@auth_router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.username)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}