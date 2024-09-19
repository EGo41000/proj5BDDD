import os, models, schema, random
from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, sessionmaker

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env (do not overver already defined vars)

SQLALCHEMY_DATABASE_URL=os.getenv('SQLALCHEMY_DATABASE_URL')
print('SQLALCHEMY_DATABASE_URL', SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Gestion des sessions
Session = sessionmaker(bind=engine)

def create_user(user: schema.UserCreate) -> schema.UserCreated:
    '''
    Crée un nouvel user
    :param user: schema UserCreate
    :return: schema UserCreated
    '''
    with Session() as session:
        new_user = models.User(id=random.randint(0, 99999), **user.model_dump())
        session.add(new_user)
        session.commit()
        return schema.UserCreated.model_validate(new_user, from_attributes=True)
    return None

def get_user_by_id(user_id: int) -> schema.UserCreated:
    '''
    get_user_by_id : récupère un User à partir de son id
    :param user_id: l'ID du user
    :return: User
    '''
    with Session() as session:
        user = session.query(models.User).get(user_id)
        return schema.UserCreated.model_validate(user, from_attributes=True)

