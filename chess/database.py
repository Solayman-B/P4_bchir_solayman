from tinydb import TinyDB
from tinydb import Query

db = TinyDB("db.json")
table_tournament = db.table("Tournaments")
table_players = db.table("Players")
query = Query()


class Tinydb:
    # saving to database
    def serialize(self, table, entry):
        table.insert(entry)

    # updating the database
    def update(self, table, value, key):
        table.update(value, key)
