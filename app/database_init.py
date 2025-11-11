# app/database_init.py

from app.database import Base, get_engine
from app.models.user import User  # Import the User model
import logging

logger = logging.getLogger(__name__)

def init_db():
    """
    Initialize the database by creating all tables.
    
    This function creates all tables defined by SQLAlchemy models
    that inherit from Base.
    """
    try:
        engine = get_engine()
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {str(e)}")
        raise

def drop_db():
    """
    Drop all database tables.
    
    WARNING: This will delete all data in the database!
    Use with caution, typically only in test environments.
    """
    try:
        engine = get_engine()
        Base.metadata.drop_all(bind=engine)
        logger.info("Database tables dropped successfully")
    except Exception as e:
        logger.error(f"Error dropping database tables: {str(e)}")
        raise

if __name__ == "__main__":
    # Allow running this script directly to initialize the database
    logging.basicConfig(level=logging.INFO)
    print("Initializing database...")
    init_db()
    print("Database initialized successfully!")
