from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env (do not overver already defined vars)

# Définition de la base
Base = declarative_base()

# Définition d'une table en tant que classe Python
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

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
new_user = User(id=1, name="John Doe")
session.add(new_user)
session.commit()