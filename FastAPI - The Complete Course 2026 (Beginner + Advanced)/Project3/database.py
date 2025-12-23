from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:adminadmin@localhost/TodoApplicationDatabase" #for postgres
#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:admin@localhost/TodoApplicationDatabase" #for mysql
#engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})##sqlite only
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
