from http.client import HTTPException
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app import actions, schemas
from app.utils.utils import get_db
from app.utils.pokeapi import get_pokemon_stats, battle_compare_stats, get_pokemon_name, random_pokemon
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
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
    first_pokemon_counter = stats[0]
    second_pokemon_counter = stats[1]
    equal_counter = stats[2]
    result = ""
    if (first_pokemon_counter > second_pokemon_counter):
        if(equal_counter == 0):
            result = "Victoire de "+ str(first_pokemon_name) + " : " + str(first_pokemon_counter) + " stats contre "+ str(second_pokemon_name) + " " + str(second_pokemon_counter) + " stats"
        else:
            result = "Victoire de "+ str(first_pokemon_name) + " : " + str(first_pokemon_counter) + " stats contre "+ str(second_pokemon_name) + " " + str(second_pokemon_counter) + " stats, égalité : "+ str(equal_counter) 
    elif (first_pokemon_counter < second_pokemon_counter):
        if(equal_counter == 0):    
            result = "Victoire de "+ str(first_pokemon_name) + " : " + str(second_pokemon_counter) + " stats contre "+ str(second_pokemon_name) + " " + str(first_pokemon_counter) +" stats"
        else:
            result = "Victoire de "+ str(first_pokemon_name) + " : " + str(second_pokemon_counter) + " stats contre "+ str(second_pokemon_name) + " " + str(first_pokemon_counter) +" stats, , égalité : "+ str(equal_counter)

    else:
        result = "Egalité : "+ str(first_pokemon_name) + " : " + str(first_pokemon_counter) + " stats, "+ str(second_pokemon_name) + " : " + str(second_pokemon_counter) + " stats"
        
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
            "stats": pokemons[0][i * 6 : (i + 1) * 6]
        }
        result.append(pokemon_data)

    return result


   
