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

Développement :
```bash
 fastapi dev main.py
```
Production : 
```bash
 ./entrypoint.sh
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

# Config VM (OLD)
ssh supinfo@4.233.202.36
PWD : SupInfo-2024
```bash
sudo apt update
sudo apt upgrade
sudo apt install docker.io
sudo usermod -aG docker $USER
# deconnect & reconnect

# install lazydocker
curl https://raw.githubusercontent.com/jesseduffield/lazydocker/master/scripts/install_update_linux.sh | bash

# récupère l'image
docker pull container-registry.oracle.com/database/free:latest
docker images

#creation volume 'oradata'
docker volume create oradata
# lancemenbt instance
docker run --name oracle -p 1521:1521 -p 5500:5500 -p 2484:2484 --ulimit nofile=1024:65536 --ulimit nproc=2047:16384 --ulimit stack=10485760:33554432 --ulimit memlock=3221225472 -e ORACLE_PWD=SUPINFO2024 -e ORACLE_EDITION=standard -e ENABLE_TCPS=true -v oradata:/opt/oracle/oradata container-registry.oracle.com/database/free:latest
```

# Utilisation de BDD Oracle sur serveur distant (datalab)
Serveur : host datalab.myconnectech.fr  
Créer une connection sécurésée SSH avec tunnel (port 1521):
```bash
 # pass : ********
ssh -f -N -L 1521:localhost:1521 supinfo@datalab.myconnectech.fr
```
Puis utiliser DBeaver pour se connecter:
![static/img.png](static/img.png)


# Docker
Build de l'image : 
```bash
 docker build -t myfastapiapp .
```

Execution conteneur :
```bash
 docker run -d -p 8000:8000 --name myfastapiapp myfastapiapp
```

# Connection python - Oracle
Utilisation librairie oracledb (à ajouter dans requirements.txt)  
Définir dans .env :
```text
# connect oracledb
DATABASE_USER=USER
DATABASE_PASSWORD=*************
DATABASE_DSN=localhost:1521/FREEPDB1

DATABASE_TABLE=SCHEMA.TABLE_NAME

# POur SQLalchemy:
SQLALCHEMY_DATABASE_URL=oracle+oracledb://USER:PASSWORD@localhost:1521/?service_name=FREEPDB1
```
Execution de la démo oracledb :
```bash
 python3 conn_oracle.py 
```
Execution de la démo SQLalchemy :
```bash
 python3 demo_sqlalchemy.py 
```

# Alembic
```bash
 # Création de la migration - après MaJ du modele
 alembic revision --autogenerate -m "$(date)" #"COMMENTAIRE"
```
```bash
 alembic upgrade head # Mise à jour BDD
```
