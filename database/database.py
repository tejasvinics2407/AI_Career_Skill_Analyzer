# =========================================================
# DATABASE CONFIGURATION
# =========================================================

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# =========================================================
# DATABASE URL
# =========================================================

DATABASE_URL = "sqlite:///./career_skill_twin.db"


# =========================================================
# DATABASE ENGINE
# =========================================================

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


# =========================================================
# SESSION
# =========================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# =========================================================
# BASE CLASS
# =========================================================

Base = declarative_base()


# =========================================================
# DATABASE SESSION DEPENDENCY
# =========================================================

def get_db():
    """
    Create a database session and close it
    after the operation is complete.
    """

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()
# =========================================================
# CREATE DATABASE TABLES
# =========================================================

from database import models

Base.metadata.create_all(bind=engine)