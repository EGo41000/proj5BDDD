from typing import Union

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from dotenv import load_dotenv
import os, schema, crud, uvicorn

load_dotenv()  # take environment variables from .env (do not overver already defined vars)

# Instancie FastAPI
app = FastAPI()
# Traitement des fichiers statics (HTML, CSS, JS, images...)
app.mount("/static", StaticFiles(directory="static"), name="static")
# Traitement es templates (Janja2)
templates = Jinja2Templates(directory="templates")

@app.get("/health")
def get_health():
    '''
    Traitement du GET /health pour docker
    :return: "OK"
    '''
    return "OK"


@app.get("/")
def read_root():
    '''
    Traitement du GET /
    :return: redirection vers /static/index.html
    '''
    return RedirectResponse("/static/index.html") # {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(request: Request, item_id: int, q: Union[str, None] = None):
    '''
    Recherche d'un item, sous forme de template
    :param request: Request lié à l'appel GET
    :param item_id: l'ID de l'item
    :param q: Un paramètre optionnel
    :return: Le template avec le contexte de l'item
    '''
    return templates.TemplateResponse(
        request=request, name="item.html", context={"item_id": item_id, "q": q}
    )

@app.get("/user/{user_id}", response_model=schema.UserCreated)
def read_user(request: Request, user_id: int):
    '''
    Récupère le User
    :param request: Request lié à l'appel GET
    :param user_id: l'ID
    :return: Le User sous forme de JSON
    '''
    return crud.get_user_by_id(user_id)

@app.post("/user", response_model=schema.UserCreated)
def post_user(request: Request, user: schema.UserCreate):
    '''
    Création de User
    :param request: Request lié à l'appel GET
    :param user: Un objet de type User
    :return: le User en question
    '''
    return crud.create_user(user)
