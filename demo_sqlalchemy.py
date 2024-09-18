from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os, random

from models import Base, User

load_dotenv()  # take environment variables from .env (do not overver already defined vars)

# Connexion à la base de données
SQLALCHEMY_DATABASE_URL=os.getenv('SQLALCHEMY_DATABASE_URL')
print('SQLALCHEMY_DATABASE_URL', SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Création de la table
Base.metadata.create_all(engine)

# Gestion des sessions
Session = sessionmaker(bind=engine)
session = Session()

# Insertion d'un nouvel utilisateur
n=random.randint(0, 999999)
new_user = User(id=n, name=f"John Doe-{n}", surname="rien")
print('USER:', new_user)
session.add(new_user)


stmt = select(User)
print(stmt)
print('----------------------------')
for user in session.scalars(stmt):
    print(user)

session.commit()