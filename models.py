from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, sessionmaker

# Définition de la base
Base = declarative_base()

# Définition d'une table en tant que classe Python
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    no = Column(Integer)

    def __repr__(self) -> str:
        return f"User[{self.id}] : {self.name}"
