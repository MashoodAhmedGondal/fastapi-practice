from fastapi import APIRouter, Response
from enum import Enum
from starlette import status
from typing import Optional

router = APIRouter(prefix="/blog", tags=["blog"])

# @app.get("/blog/all")
# def get_all_blog():
#     return {"message": "All blogs"}

@router.get("/all",
         summary="Get all blogs",
         description = "This endpoint simulate fetch all blogs")
def get_all_blogs():
    return {"message" : "ALL Blogs here you go"}
# def get_all_blog(page,page_size):
#     return {"message": f"All {page_size} blog on {page}"}

@router.get("/page",)
def get_all_blog(page,page_size: Optional[int] = None, value : bool = None):
    return {"message": f"All {page_size} blog on {page} and value is {value}"}


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"

@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    """
    Simulate fetch blogs type
    - **type** Mandatory path parameter
    - **Endpoint** has a object BlogType
    """
    return {"message": f"Blog Type {type.value}"}

@router.get("/{id}",
status_code = status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"blog number {id} could not be found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog Number {id} found"}