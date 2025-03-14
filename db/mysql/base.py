from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import Config

Base = declarative_base()

engine = create_engine(
    f'mysql+pymysql://{Config.USER}:{Config.PASSWORD}@{Config.HOST}:{Config.PORT}/graduation_project'
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_db():
    '''
    check the connection to the database
    '''
    try:
        engine.connect()
        return True
    except Exception as e:
        print(e)
        return False
