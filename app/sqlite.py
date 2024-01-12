"""
SQLite Configuration and Database Connection.

This module configures the SQLite database connection using SQLAlchemy.

Attributes:
- `SQLITE_URL` (str): SQLite database URL.
- `engine` (Engine): SQLAlchemy database engine.
- `SessionLocal` (sessionmaker): Session factory for creating database sessions.
- `Base` (DeclarativeMeta): Base class for declarative class definitions.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLITE_URL = "sqlite:///./sqlite.db"
engine = create_engine(SQLITE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# End-of-file (EOF)
