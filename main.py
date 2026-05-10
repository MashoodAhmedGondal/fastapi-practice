from fastapi import FastAPI, HTTPException ,Request
from fastapi.responses import JSONResponse,PlainTextResponse
from db.database import engine
from db import models
from router import blog_get,blog_post,user,article,file
from auth import authentication
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(file.router)
@app.get("/")
def index():
    return {"message": "Hello World"}

# @app.exception_handler(HTTPException)
# def custom_exception_handler(request: Request, exc: HTTPException):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

models.Base.metadata.create_all(bind=engine)


app.mount('/files', StaticFiles(directory='files', html=True), name='files')