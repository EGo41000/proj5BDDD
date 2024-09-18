from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os, random

load_dotenv()  # take environment variables from .env (do not overver already defined vars)

# Définition de la base
Base = declarative_base()

# Définition d'une table en tant que classe Python
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))

    def __repr__(self) -> str:
        return f"User[{self.id}] : {self.name}"

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