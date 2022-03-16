from db.database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
#db.resetDatabase()


#pokemons = db.spawnChanceGT(9)

#avg_spawns > 50
pokemons = db.collection.find({"avg_spawns": {"$gt": 50}})

#candy = Bulbasaur Candy ou Squirtle Candy
pokemons = db.collection.find({"$or": [{"candy":"Bulbasaur Candy"},{"candy": "Squirtle Candy"}]})

#type = Grass e Poison
tipo = ["Grass", "Poison"]
pokemons = db.executeQuery({"type": {"$all": tipo}})

#sem o campo next_evolution
pokemons = db.collection.find({"next_evolution": {"$exists": False}})

#candy_count < 20
pokemons = db.collection.find({"candy_count": {"$lt": 20}})

writeAJson(pokemons, "pokemons")

