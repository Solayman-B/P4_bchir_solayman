from tinydb import TinyDB, Query, where
db = TinyDB('db.json')
table_tournament = db.table("Tournaments")
table_players = db.table("Players")


class Tinydb:

	def serialize(self, table, key, value):
		table.insert({key: value})

	def update(self):
		table_players.update({"nombre de points": 10}, where ("identifiant") == 1)
		table_players.search(where("identifiant") == 1)

	def deserealize(key,table, value):
		for item in db:
			pass

	#db.truncate()

	#print(db.all())