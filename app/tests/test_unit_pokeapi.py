import pytest
from ..utils import pokeapi

sample_pokemon_data = {
    'name': 'Pikachu',
    'stats': [
        {'stat': {'name': 'hp'}, 'base_stat': 50},
        {'stat': {'name': 'attack'}, 'base_stat': 55},
        {'stat': {'name': 'defense'}, 'base_stat': 40},
        {'stat': {'name': 'special-attack'}, 'base_stat': 50},
        {'stat': {'name': 'special-defense'}, 'base_stat': 50},
        {'stat': {'name': 'speed'}, 'base_stat': 90},
    ]
}

def test_get_pokemon_name(mocker):
    api_id = 25
    mocker.patch("pokeapi.requests.get").return_value.json.return_value = {'name': 'Pikachu'}
    result = pokeapi.get_pokemon_name(api_id)
    assert result == 'Pikachu'
    pokeapi.requests.get.assert_called_once_with(f"{pokeapi.BASE_URL}/pokemon/{api_id}", timeout=10)

def test_get_pokemon_stats(mocker):
    api_id = 25
    mocker.patch("pokeapi.requests.get").return_value.json.return_value = sample_pokemon_data
    result = pokeapi.get_pokemon_stats(api_id)
    assert result == sample_pokemon_data['stats']
    pokeapi.requests.get.assert_called_once_with(f"{pokeapi.BASE_URL}/pokemon/{api_id}", timeout=10)


def test_battle_compare_stats():
    result = pokeapi.battle_compare_stats(1, 2)
    assert result == (0, 6, 0)


def test_get_pokemon_name():
    assert pokeapi.get_pokemon_name(1) == "bulbasaur"

def test_get_pokemon_stats():
    assert pokeapi.get_pokemon_stats(1) == [
  {
    "base_stat": 45,
    "effort": 0,
    "stat": {
      "name": "hp",
      "url": "https://pokeapi.co/api/v2/stat/1/"
    }
  },
  {
    "base_stat": 49,
    "effort": 0,
    "stat": {
      "name": "attack",
      "url": "https://pokeapi.co/api/v2/stat/2/"
    }
  },
  {
    "base_stat": 49,
    "effort": 0,
    "stat": {
      "name": "defense",
      "url": "https://pokeapi.co/api/v2/stat/3/"
    }
  },
  {
    "base_stat": 65,
    "effort": 1,
    "stat": {
      "name": "special-attack",
      "url": "https://pokeapi.co/api/v2/stat/4/"
    }
  },
  {
    "base_stat": 65,
    "effort": 0,
    "stat": {
      "name": "special-defense",
      "url": "https://pokeapi.co/api/v2/stat/5/"
    }
  },
  {
    "base_stat": 45,
    "effort": 0,
    "stat": {
      "name": "speed",
      "url": "https://pokeapi.co/api/v2/stat/6/"
    }
  }
]
    
def test_get_battle_compare_stats():
  assert pokeapi.battle_compare_stats(1, 2) == (0, 6, 0)


def test_get_pokemon_data(mocker):
    api_id = 25
    mocker.patch("pokeapi.requests.get").return_value.json.return_value = sample_pokemon_data
    result = pokeapi.get_pokemon_data(api_id)
    assert result == sample_pokemon_data
    pokeapi.requests.get.assert_called_once_with(f"{pokeapi.BASE_URL}/pokemon/{api_id}", timeout=10)

