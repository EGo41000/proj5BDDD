import os
from alembic import command
from alembic.config import Config

def pytest_configure(config):
    print('OK pytest_configure')
    #os.environ['SQLALCHEMY_DATABASE_URL']='sqlite:///:memory:' # PB with multithreaded
    os.environ['SQLALCHEMY_DATABASE_URL']='sqlite:///test.db'

    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    print('ALEMBIC')
