"""
Base Models for Trainers, Items, and Pokemon.

Includes Pydantic BaseModel classes for defining data models.

Dependencies:
- `date` (class): Date class from the `datetime` module.
- `List` (class): List class from the `typing` module.
- `Optional` (class): Optional class from the `typing` module.
- `Union` (class): Union class from the `typing` module.
- `BaseModel` (class): BaseModel class from the `pydantic` module.
"""
import dataclasses
from datetime import date
from typing import List, Optional, Union
from pydantic import BaseModel

#
# ITEM
#
class ItemBase(BaseModel):
    """
    Base model for item-related data.
    """
    name: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    """
    Model for creating a new item.
    """

class Item(ItemBase):
    """
    Model for representing an item with additional details.
    """
    id: int
    trainer_id: int

    @dataclasses.dataclass
    class Config:
        """
        Configuration class for Pydantic models.

        Attributes:
        - `orm_mode` (bool): Indicates whether the model should be used in ORM mode.
        """
        orm_mode = True

# POKEMON
#
class PokemonBase(BaseModel):
    """
    Base model for Pokemon-related data.
    """
    api_id: int
    custom_name: Optional[str] = None

class PokemonCreate(PokemonBase):
    """
    Model for creating a new Pokemon.
    """


class Pokemon(PokemonBase):
    """
    Model for representing a Pokemon with additional details.
    """
    id: int
    name: str
    trainer_id: int

    @dataclasses.dataclass
    class Config:
        """
        Configuration class for Pydantic models.

        Attributes:
        - `orm_mode` (bool): Indicates whether the model should be used in ORM mode.
        """
        orm_mode = True

#
# TRAINER
#
class TrainerBase(BaseModel):
    """
    Base model for trainer-related data.
    """
    name: str
    birthdate: date



class Trainer(TrainerBase):
    """
    Model for representing a trainer with additional details.
    """
    id: int
    inventory: List[Item] = []
    pokemons: List[Pokemon] = []

    @dataclasses.dataclass
    class Config:
        """
        Configuration class for Pydantic models.

        Attributes:
        - `orm_mode` (bool): Indicates whether the model should be used in ORM mode.
        """
        orm_mode = True
