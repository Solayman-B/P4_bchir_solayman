from tinydb import TinyDB, Query
db = TinyDB('db.json')
table_tournament = db.table("Tournaments")
table_players = db.table("Players")


class Tinydb:

	def serialize(self, table, key, value):
		table.insert({key: value})

	def deserealize(key,table, value):
		for item in db:
			pass

	#db.truncate()

	#print(db.all())