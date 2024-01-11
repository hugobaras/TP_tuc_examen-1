from app.utils import pokeapi

app = pokeapi(__name__)

from app import routes


app.run(debug=True)