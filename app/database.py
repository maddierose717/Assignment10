# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

def get_engine(database_url: str = None):
    url = database_url or settings.DATABASE_URL
    engine = create_engine(url, pool_pre_ping=True, echo=False)
    return engine

def get_sessionmaker(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Add this line - it's what your user.py needs
Base = declarative_base()

def get_db():
    engine = get_engine()
    SessionLocal = get_sessionmaker(engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()