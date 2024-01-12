"""
API Router for managing items.

This module defines an API router using FastAPI to manage items. 
It includes the following endpoints:

- GET /: Retrieve a list of items with optional pagination.
- Dependencies:
  - database: Session dependency to interact with the database.
  - actions: Functions for handling item-related actions.
  - schemas: Data models (schemas) used by the API.

Endpoint Details:
- GET /:
  - Returns a list of items.
  - Default limit is set to 100.

"""

from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from ..utils.utils import get_db
from .. import actions, schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.Item])
def get_items(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
    Return all items.
    Default limit is 100.
    """
    try:
        items = actions.get_items(database, skip=skip, limit=limit)
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") from e
