#!/bin/sh

# Applique les migrations Alamnbic
alembic upgrade head
# Démarre le serveur
uvicorn main:app --host 0.0.0.0

