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
    response = client.get("/user/100")
    assert response.status_code == 200
    assert response.json() ==  {'email': 'EGo@gmail.com', 'id': 100, 'name': 'goudot-100'}

