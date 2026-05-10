from typing import List
from fastapi import APIRouter , Depends

from auth.oauth2 import get_current_user
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay
from sqlalchemy.orm import Session
from db import db_article
from schemas import UserBase
from auth import oauth2
router = APIRouter(prefix="/article",tags=["article"])

@router.post("/", response_model=ArticleDisplay)
def create_article(article: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db,article)

@router.get("/{id}")#, response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db) , current_user: UserBase = Depends(get_current_user)):
    return {
        "data": db_article.get_article(db, id),
        "user": current_user
    }
