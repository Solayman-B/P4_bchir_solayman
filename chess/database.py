from tinydb import TinyDB, Query, where
db = TinyDB('db.json')
table_tournament = db.table("Tournaments")
table_players = db.table("Players")
query = Query()


class Tinydb:

	def serialize(self, table, entry):
		table.insert(entry)

	def update(self, value, key):
		table_players.update(value, key)

	def deserealize(key,table, value):
		for item in db:
			pass

	#db.truncate()

	#print(db.all())