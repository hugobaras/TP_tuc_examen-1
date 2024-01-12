"""
API Router for managing trainers, items, and Pokemon.

This module defines an API router using FastAPI to handle operations related to 
trainers, items, and Pokemon. It includes the following endpoints:

1. **Create Trainer (POST /):**
    - Create a new trainer.
    - Parameters:
        - `trainer` (schemas.TrainerCreate): Trainer data to be created.
    - Returns:
        - The created trainer.

2. **Get Trainers (GET /):**
    - Retrieve a list of trainers with optional pagination.
    - Parameters:
        - `skip` (int): Number of trainers to skip (default: 0).
        - `limit` (int): Maximum number of trainers to return (default: 100).
    - Returns:
        - A list of trainers.

3. **Get Trainer by ID (GET /{trainer_id}):**
    - Retrieve a specific trainer by their ID.
    - Parameters:
        - `trainer_id` (int): ID of the trainer to retrieve.
    - Returns:
        - The trainer with the specified ID.
    - Raises:
        - HTTPException (404): If the trainer is not found.

4. **Add Item to Trainer's Inventory (POST /{trainer_id}/item/):**
    - Add an item to a trainer's inventory.
    - Parameters:
        - `trainer_id` (int): ID of the trainer.
        - `item` (schemas.ItemCreate): Item data to be added.
    - Returns:
        - The created item.

5. **Add Pokemon to Trainer's Collection (POST /{trainer_id}/pokemon/):**
    - Add a Pokemon to a trainer's collection.
    - Parameters:
        - `trainer_id` (int): ID of the trainer.
        - `pokemon` (schemas.PokemonCreate): Pokemon data to be added.
    - Returns:
        - The created Pokemon.

Dependencies:
- `database` (Session): Dependency to interact with the database.
- `actions` (module): Functions for handling trainer-related actions.
- `schemas` (module): Data models (schemas) used by the API.

Exception Handling:
- If an internal server error occurs during any operation, it raises an
 HTTPException with a 500 status code.

"""

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends, HTTPException
from ..utils.utils import get_db
from .. import actions, schemas
router = APIRouter()


@router.post("/", response_model=schemas.Trainer)
def create_trainer(database: Session = Depends(get_db)):
    """
        Create a trainer
    """
    return actions.create_trainer(database=database)


@router.get("", response_model=List[schemas.Trainer])
def get_trainers(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all trainers
        Default limit is 100
    """
    trainers = actions.get_trainers(database, skip=skip, limit=limit)
    return trainers


@router.get("/{trainer_id}", response_model=schemas.Trainer)
def get_trainer(trainer_id: int, database: Session = Depends(get_db)):
    """
        Return trainer from his id
    """
    db_trainer = actions.get_trainer(database, trainer_id=trainer_id)
    if db_trainer is None:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return db_trainer


@router.post("/{trainer_id}/item/", response_model=schemas.Item)
def create_item_for_trainer(
    trainer_id: int, item: schemas.ItemCreate, database: Session = Depends(get_db)
):
    """
        Add an item in trainer inventory
    """
    return actions.add_trainer_item(database=database, item=item, trainer_id=trainer_id)


@router.post("/{trainer_id}/pokemon/", response_model=schemas.Pokemon)
def create_pokemon_for_trainer(
    trainer_id: int, pokemon: schemas.PokemonCreate, database: Session = Depends(get_db)
):
    """
        Add a Pokemon to a trainer
    """
    return actions.add_trainer_pokemon(database=database, pokemon=pokemon, trainer_id=trainer_id)
