import pytest
from fastapi.testclient import TestClient
from main import app

import schema, crud
import dotenv, os, time
dotenv.load_dotenv()

# https://fastapi.tiangolo.com/tutorial/testing/
client = TestClient(app)

def test_root():
    '''
    Teste le status de le requête
    :return:
    '''
    response = client.get("/")
    assert response.status_code == 200

def test_get_user():
    '''
    Teste le status de le requête et le résultat attendu
    :return:
    '''
    u0=schema.UserCreate(name='User creation 2', email='EGo@gmail.com')
    uc = crud.create_user(u0)
    assert uc.id > 0

    response = client.get(f"/user/{uc.id}")
    assert response.status_code == 200
    assert response.json() ==  {'email': 'EGo@gmail.com', 'id': uc.id, 'name': 'User creation 2'}

