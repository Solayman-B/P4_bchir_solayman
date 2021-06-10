from packages.view import *
from packages.model import *

#creation du tournoi
new_tournament = Tournoi(tournament, location, date)

#creation des joueurs
players = number_of_players()
for player in players:
	new_player = enter_new_players()
	player = Player(new_player[0],new_player[1],new_player[2],new_player[3],new_player[4])
	ranking_list.append(new_player[4])
	list_of_players.append(player)

#trie des joueurs
ranking_list.sort()
for x in range(0,8):
	for i in range(0,8):
		if list_of_players[i].ranking == ranking_list[x]:
			ranked_players.append(list_of_players[i])

#creation de paires de joueurs

for i in range(0, 4):
	b = len(ranked_players) // 2
	groupe_1.append(ranked_players.pop(b))
	groupe_2.append(ranked_players.pop())

tour_1 = [groupe_1, groupe_2]
print(tour_1[0][0].name)

#1er tour

