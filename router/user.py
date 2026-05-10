from typing import List
from fastapi import APIRouter , Depends
from db.database import get_db
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db import db_user
from auth.oauth2 import oauth2_scheme

router = APIRouter(prefix="/user",tags=["user"])

@router.post("/", response_model=UserDisplay)
def create_user(request :UserBase , db : Session = Depends(get_db)):
    return db_user.create_user(db , request)

@router.get("/", response_model=List[UserDisplay])
def get_all_user(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

@router.get("/{id}", response_model=UserDisplay)
def get_user(id : int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return db_user.get_user(db, id)

@router.get("/username", response_model=UserDisplay)
def get_user(username : str, db: Session = Depends(get_db)):
    return db_user.db_user_by_username(db, username)

@router.put("/update/{id}", response_model=UserDisplay)
def update_user(id : int, request : UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)
@router.delete("/delete/{id}")
def delete_user(id : int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)