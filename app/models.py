"""
Database Models for Trainers, Pokemon, and Items.

This module defines SQLAlchemy models for representing trainers, 
Pokemon, and items in the database.

Dependencies:
- `dataclasses` (module): Module providing a decorator and functions 
for defining data classes.
- `Column` (class): Column class from the `sqlalchemy` module.
- `ForeignKey` (class): ForeignKey class from the `sqlalchemy` module.
- `Integer` (class): Integer class from the `sqlalchemy` module.
- `String` (class): String class from the `sqlalchemy` module.
- `Date` (class): Date class from the `sqlalchemy` module.
- `relationship` (function): Function from the `sqlalchemy.orm` module.

1. **Trainer Model:**
    - Class representing a Pokemon trainer.
    - Attributes:
        - `id` (int): Primary key for the trainer.
        - `name` (str): Trainer's name.
        - `birthdate` (Date): Trainer's birthdate.
        - `inventory` (relationship): One-to-Many relationship with items.
        - `pokemons` (relationship): One-to-Many relationship with Pokemon.
    
2. **Pokemon Model:**
    - Class representing a Pokemon.
    - Attributes:
        - `id` (int): Primary key for the Pokemon.
        - `api_id` (int): ID from the PokeAPI.
        - `name` (str): Pokemon's name from the PokeAPI.
        - `custom_name` (str): Custom name for the Pokemon.
        - `trainer_id` (int): Foreign key referencing the Trainer model.
        - `trainer` (relationship): Many-to-One relationship with Trainer.

3. **Item Model:**
    - Class representing an item.
    - Attributes:
        - `id` (int): Primary key for the item.
        - `name` (str): Item's name.
        - `description` (str): Item's description.
        - `trainer_id` (int): Foreign key referencing the Trainer model.
        - `trainer` (relationship): Many-to-One relationship with Trainer.
"""

import dataclasses
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from .sqlite import Base

@dataclasses.dataclass
class Trainer(Base):
    """
        Class representing a pokemon trainer
    """
    __tablename__ = "trainers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birthdate = Column(Date)

    inventory = relationship("Item", back_populates="trainer")
    pokemons = relationship("Pokemon", back_populates="trainer")

@dataclasses.dataclass
class Pokemon(Base):
    """
        Class representing a pokemon
        Parameters:
            api_id (int): id from the pokeapi
            name (str): Populate with the pokeapi data 
    """
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    api_id = Column(Integer, index=True)
    name = Column(String, index=True)
    custom_name = Column(String, index=True)
    trainer_id = Column(Integer, ForeignKey("trainers.id"))

    trainer = relationship("Trainer", back_populates="pokemons")

@dataclasses.dataclass
class Item(Base):
    """
        Class representing a pokemon trainer
    """
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    trainer_id = Column(Integer, ForeignKey("trainers.id"))

    trainer = relationship("Trainer", back_populates="inventory")
