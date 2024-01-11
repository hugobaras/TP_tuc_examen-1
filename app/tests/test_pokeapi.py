from app.utils import pokeapi

def test_api():
    assert pokeapi.get_pokemon_name(1) == "bulbasaur"
    