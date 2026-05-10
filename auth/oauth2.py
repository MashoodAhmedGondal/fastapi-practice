# from fastapi.security import OAuth2PasswordBearer
#  oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# just an idea how to secure an endpoint
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from sqlalchemy.orm.session import Session
from fastapi.param_functions import Depends
from fastapi import HTTPException
from starlette import status
from db import db_user
from db.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = 'bc74959ba56fb62a5a2b1e32d02fcc2683124a73465a0883a01940673b271500'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db : Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db_user.get_user_by_username(db,username)
    if user is None:
        raise credentials_exception
    return user

# from jose import JWTError, ExpiredSignatureError
#
# def get_current_user(
#     token: str = Depends(oauth2_scheme),
#     db: Session = Depends(get_db)
# ):
#     try:
#         payload = jwt.decode(
#             token,
#             settings.SECRET_KEY,
#             algorithms=[ALGORITHM]
#         )
#         email: str = payload.get("sub")
#
#         if email is None:
#             raise HTTPException(
#                 status_code=401,
#                 detail="Could not validate credentials"
#             )
#
#     except ExpiredSignatureError:
#         # ← specifically catches expired token!
#         raise HTTPException(
#             status_code=401,
#             detail="Session expired! Please login again."
#         )
#
#     except JWTError:
#         # ← catches any other JWT error
#         raise HTTPException(
#             status_code=401,
#             detail="Could not validate credentials"
#         )
#
#     # Find user in database
#     user = db.execute(
#         select(User).where(User.email == email)
#     ).scalar_one_or_none()
#
#     if user is None:
#         raise HTTPException(
#             status_code=401,
#             detail="User not found!"
#         )
#
#     return user