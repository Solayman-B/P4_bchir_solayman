from packages.view import *
from packages.model import *

new_tournament = Tournoi(tournament, location, date)

players = number_of_players()
for player in players:
	player = Player("name;", "surname;", "date_of_birth;", "sex;", "ranking;")
	new_player = enter_new_players(player)
	for p in new_player:
		save_a_player(p) # modifier par enregustrement dans tinydb

test

#1er tour

