from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'postgresql://postgres:password@localhost:5432/cc_local', echo=False)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = session_local()
Base = declarative_base()
