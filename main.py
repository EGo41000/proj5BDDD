from typing import Union

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from dotenv import load_dotenv
import os
import schema

load_dotenv()  # take environment variables from .env.

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return RedirectResponse("/static/index.html") # {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(request: Request, item_id: int, q: Union[str, None] = None):
    #return {"item_id": item_id, "q": q}
    return templates.TemplateResponse(
        request=request, name="item.html", context={"item_id": item_id, "q": q}
    )

@app.get("/user/{user_id}", response_model=schema.User)
def read_user(request: Request, user_id: int):
    user = schema.User(id=user_id, name='goudot', email='EGo@gmail.com')
    return user
