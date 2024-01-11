from ..app.utils import pokeapi

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


