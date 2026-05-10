from fastapi import APIRouter, Response
from enum import Enum
from starlette import status
from typing import Optional
from pydantic import BaseModel

router = APIRouter(prefix="/blog", tags=["blog"])

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published : Optional[bool] = False


@router.post("/new/{id}")
def create_blog(blog : BlogModel, id : int, version : int = 1):
    return {
        "id" : id,
        "data" : blog,
        "version" : version
    }


