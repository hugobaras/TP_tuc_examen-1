import requests
import random


base_url = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']


def get_pokemon_stats(api_id):
    """
        Get pokemon stats from the API pokeapi
    """
    return get_pokemon_data(api_id)['stats']


def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{base_url}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_api_id, second_api_id):
    """
        Do battle between 2 pokemons
    """
    premierPokemon = get_pokemon_data(first_api_id)
    secondPokemon = get_pokemon_data(second_api_id)
    battle_result = 0
    return premierPokemon if battle_result > 0 else secondPokemon if battle_result < 0 else {'winner': 'draw'}


def get_stat(pokemon_stats, stat_name):
    for stat in pokemon_stats:
        if stat['stat']['name'] == stat_name:
            return stat['base_stat']
    return None

def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stat between two pokemons
    """
    first_pokemon = get_pokemon_stats(first_pokemon_stats)
    second_pokemon = get_pokemon_stats(second_pokemon_stats)

    first_pokemon_counter = 0
    second_pokemon_counter = 0
    equal_counter = 0

    stat_names = ['hp', 'attack', 'defense',
                  'special-attack', 'special-defense', 'speed']

    for stat_name in stat_names:
        first_pokemon_stat = get_stat(first_pokemon, stat_name)
        second_pokemon_stat = get_stat(second_pokemon, stat_name)

        if (first_pokemon_stat > second_pokemon_stat):
            first_pokemon_counter += 1
        elif (first_pokemon_stat < second_pokemon_stat):
            second_pokemon_counter += 1
        else:
            equal_counter += 1

    return first_pokemon_counter, second_pokemon_counter, equal_counter

def random_pokemon():
    """
    Gives three random pokemons and their stats
    """
    pokemons = []
    pokemons_names = []
    stat_names = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']

    for i in range(3):
        random_number = random.randint(0, 150)
        pokemon_name = get_pokemon_name(random_number)
        pokemon = get_pokemon_stats(random_number)

        pokemons_names.append(pokemon_name)
        for stat_name in stat_names:
            pokemon_stat = get_stat(pokemon, stat_name)
            pokemons.append((stat_name, pokemon_stat))


    return pokemons, pokemons_names