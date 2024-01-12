"""
Database and Date Utility Functions.

This module includes functions for database access and date-related calculations.

1. **get_db():**
    - Function to get a database session.
    - Returns:
        - A database session using SQLite.
    - Example:
        ```python
        with get_db() as db:
            # Perform database operations
        ```

2. **age_from_birthdate(birthdate):**
    - Calculate age from a given birthdate.
    - Parameters:
        - `birthdate` (date): Date object representing the birthdate.
    - Returns:
        - The calculated age as an integer.
    - Example:
        ```python
        birthdate = date(1990, 5, 15)
        age = age_from_birthdate(birthdate)
        print(age)  # Output: Calculated age based on the current date.
"""

from datetime import date
from .. import models
from ..sqlite import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

def get_db():
    """
        Get the DB
    """
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()



def age_from_birthdate(birthdate):
    """
        Return an age from a birthday
    """
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day)
        < (birthdate.month, birthdate.day))
