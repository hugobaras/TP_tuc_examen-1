"""
API routes for Pokemon information using FastAPI and Flask.

Endpoints:
- GET /: Retrieve a list of Pokemon with optional pagination.
- GET /stats/{first_pokemon_id}: Get the stats of a specific Pokemon.
- GET /battle_stats/{first_pokemon_id}/{second_pokemon_id}: 
Conduct a battle between two Pokemon and compare their stats.
- GET /random: Retrieve information about three randomly selected Pokemon.

Dependencies:
- FastAPI: Web framework for building APIs with Python type hints.

Modules:
- actions: Functions for interacting with the database
 and retrieving Pokemon information.
- schemas: Defines data models (schemas) for the API.
- utils: Utility functions, including database connection 
and PokeAPI integration.
"""
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from .. import actions, schemas
from ..utils.utils import get_db
from ..utils.pokeapi import (
    get_pokemon_stats,
    battle_compare_stats,
    get_pokemon_name,
    random_pokemon,
)
router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
    Return all pokemons
    Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons


@router.get("/stats/{first_pokemon_id}")
def get_stats(first_pokemon_id: int):
    """
    Return only one pokemon stats
    """
    stats = get_pokemon_stats(first_pokemon_id)
    return stats


@router.get("/battle_stats/{first_pokemon_id}/{second_pokemon_id}")
def battle_pokemons(first_pokemon_id: int, second_pokemon_id: int):
    """
    Return pokemons stats
    """
    stats = battle_compare_stats(first_pokemon_id, second_pokemon_id)
    first_pokemon_name = get_pokemon_name(first_pokemon_id)
    second_pokemon_name = get_pokemon_name(second_pokemon_id)
    first_pokemon_counter, second_pokemon_counter, equal_counter = stats

    result = ""
    if first_pokemon_counter > second_pokemon_counter:
        if equal_counter == 0:
            result = (
                f"Victoire de {first_pokemon_name}: {first_pokemon_counter} stats contre "
                f"{second_pokemon_name} {second_pokemon_counter} stats"
            )
        else:
            result = (
                f"Victoire de {first_pokemon_name}: {first_pokemon_counter} stats contre "
                f"{second_pokemon_name} {second_pokemon_counter} stats, égalité : {equal_counter}"
            )
    elif first_pokemon_counter < second_pokemon_counter:
        if equal_counter == 0:
            result = (
                f"Victoire de {first_pokemon_name}: {second_pokemon_counter} stats contre "
                f"{second_pokemon_name} {first_pokemon_counter} stats"
            )
        else:
            result = (
                f"Victoire de {first_pokemon_name}: {second_pokemon_counter} stats contre "
                f"{second_pokemon_name} {first_pokemon_counter} stats, égalité : {equal_counter}"
            )
    else:
        result = (
            f"Egalité : {first_pokemon_name}: {first_pokemon_counter} stats, "
            f"{second_pokemon_name}: {second_pokemon_counter} stats"
        )

    return result


@router.get("/random")
def random_pokemons():
    """
    Return pokemons randomly
    """
    pokemons = random_pokemon()

    result = []

    # Utiliser une boucle pour récupérer les trois premiers Pokémon
    for i in range(3):
        pokemon_data = {
            "pokemon": pokemons[1][i],
            "stats": pokemons[0][i * 6 : (i + 1) * 6],
        }
        result.append(pokemon_data)

    return result
