# proj5BDDD

projet pour le cours 5BDDD  
Utilisation de _FastAPI_

## Installation (linux)
Lien documentation  
VENV : https://fastapi.tiangolo.com/virtual-environments/ et https://docs.python.org/3/library/venv.html  
Pages statiques : https://fastapi.tiangolo.com/reference/staticfiles/  
Redirections : https://fastapi.tiangolo.com/uk/advanced/custom-response/#redirectresponse
Templates : https://fastapi.tiangolo.com/advanced/templates/  

```bash
 # Création environnement virtuel & activation
 python3 -m venv venv
 source venv/bin/activate
 # Installation librairies listées dans 'requirements.txt'
 pip install -r requirements.txt
 pip freeze
```

Déactivation de l'environnement virtuel (si besoin)
```bash
 deactivate 
```

## Démarrage application

Variables d'environnement à définir dans un fichier .env (exemple): 
```text
TEST=147852369
BDD_URL=sqlite://:memory:
```

```bash
 fastapi dev main.py
```

Accès au swagger sur http://127.0.0.1:8000/docs  
Accès à la page index : http://127.0.0.1:8000/static/index.html  
Page principale (renvoie vers static) : http://127.0.0.1:8000/  
Page template : http://127.0.0.1:8000/items/123?q=test  

## Tests
Les tests doivent passer sans erreur
```bash
 pytest
```
