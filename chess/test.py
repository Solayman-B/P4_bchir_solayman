list = [(4, 7), (3, 8), (1, 6), (2, 5), (1, 2), (1, 2), (3, 4), (1, 2), (3, 4), (5, 6), (1, 2), (3, 4), (5, 6), (7, 8)]

list_of_players_of_this_round = [1,2]

nb_player_round = 0

a = 4
b = 7
c = a,b

if c in list:
	print("c'est la fête")

if nb_player_round < 8:
	for player in list:
		if player not in list_of_players_of_this_round:
			nb_player_round += 1

while list_of_players_of_this_round:
	print("oulah")
	list_of_players_of_this_round.pop()