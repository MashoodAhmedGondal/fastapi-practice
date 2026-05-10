from sqlalchemy.orm.session import Session
from db.models import DbUser
from db.hash import Hash
from schemas import  UserBase
from fastapi import HTTPException


def create_user(db : Session, request : UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db : Session):
    return db.query(DbUser).all()

def get_user(db : Session, id: int):
    user  = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with {id} not found")
    return user

def get_user_by_username(db : Session, username: str):
    user  = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with {username} not found")
    return user

def update_user(db : Session, id :int, request : UserBase):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    user.username = request.username
    user.email = request.email
    user.password = Hash.bcrypt(request.password)
    db.commit()
    return user

def delete_user(db : Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with {id} not found")
    db.delete(user)
    db.commit()
    return "User deleted"