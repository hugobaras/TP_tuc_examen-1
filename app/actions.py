"""
Database Operations for Trainers, Pokemon, and Items.

This module provides functions for performing CRUD operations on the database,
specifically for trainers, Pokemon, and items.

Dependencies:
- `Session` (class): Session class from the `sqlalchemy.orm` module.
- `models` (module): Database models.
- `schemas` (module): Pydantic schemas for data validation.
- `get_pokemon_name` (function): Function from the `utils.pokeapi` module.

1. **Trainer Operations:**
    - `get_trainer(database: Session, trainer_id: int):`
        - Find a trainer by their ID.
    - `get_trainer_by_name(database: Session, name: str):`
        - Find a trainer by their name.
    - `get_trainers(database: Session, skip: int = 0, limit: int = 100):`
        - Find all trainers.
    - `create_trainer(database: Session, trainer: schemas.TrainerCreate):`
        - Create a new trainer.

2. **Pokemon Operations:**
    - `add_trainer_pokemon(database: Session, pokemon: schemas.PokemonCreate, trainer_id: int):`
        - Create a Pokemon and link it to a trainer.
    - `get_pokemon(database: Session, pokemon_id: int):`
        - Find a Pokemon by its ID.
    - `get_pokemons(database: Session, skip: int = 0, limit: int = 100):`
        - Find all Pokemon.

3. **Item Operations:**
    - `add_trainer_item(database: Session, item: schemas.ItemCreate, trainer_id: int):`
        - Create an item and link it to a trainer.
    - `get_items(database: Session, skip: int = 0, limit: int = 100):`
        - Find all items.
"""
from sqlalchemy.orm import Session
from . import models, schemas
from .utils.pokeapi import get_pokemon_name


def get_trainer(database: Session, trainer_id: int):
    """
        Find a user by his id
    """
    return database.query(models.Trainer).filter(models.Trainer.id == trainer_id).first()


def get_trainer_by_name(database: Session, name: str):
    """
        Find a user by his name
    """
    return database.query(models.Trainer).filter(models.Trainer.name == name).all()


def get_trainers(database: Session, skip: int = 0, limit: int = 100):
    """
        Find all users
        Default limit is 100
    """
    return database.query(models.Trainer).offset(skip).limit(limit).all()


def create_trainer(database: Session):
    """
        Create a new trainer
    """
    db_trainer = models.Trainer()
    database.add(db_trainer)
    database.commit()
    database.refresh(db_trainer)
    return db_trainer


def add_trainer_pokemon(database: Session, pokemon: schemas.PokemonCreate, trainer_id: int):
    """
        Create a pokemon and link it to a trainer
    """
    db_item = models.Pokemon(
        **pokemon.dict(), name=get_pokemon_name(pokemon.api_id), trainer_id=trainer_id)
    database.add(db_item)
    database.commit()
    database.refresh(db_item)
    return db_item


def add_trainer_item(database: Session, item: schemas.ItemCreate, trainer_id: int):
    """
        Create an item and link it to a trainer
    """
    db_item = models.Item(**item.dict(), trainer_id=trainer_id)
    database.add(db_item)
    database.commit()
    database.refresh(db_item)
    return db_item


def get_items(database: Session, skip: int = 0, limit: int = 100):
    """
        Find all items
        Default limit is 100
    """
    return database.query(models.Item).offset(skip).limit(limit).all()


def get_pokemon(database: Session, pokemon_id: int):
    """
        Find a pokemon by his id
    """
    return database.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()


def get_pokemons(database: Session, skip: int = 0, limit: int = 100):
    """
        Find all pokemons
        Default limit is 100
    """
    return database.query(models.Pokemon).offset(skip).limit(limit).all()
