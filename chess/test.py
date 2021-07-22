from database import *
from model import *
from view import *
tournament = Tournament()
tinydb = Tinydb()
new_game_view = NewGameView()


db.truncate()
for key, value in zip(keys, tournament.info):
	print(key, "key")
	tinydb.serialize(table_tournament, key, value)

print(db.all(), "base de données")
