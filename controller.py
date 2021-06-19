from packages.view import *
from packages.model import *
import time
from random import random
#creation du tournoi
new_tournament = Tournament(time.strftime("%d/%m/%Y"))

print_tournament_info(new_tournament)

choice_a = input_a()

if  choice_a == 1:
	a = modify_tournament()
	if a == 1:
		new_tournament.tournament_name = input("\nEntrez le nom du tournoi:\n\n")
	elif a == 2:
		new_tournament.location = input("\nEntrez le lieu du tournoi:\n\n")
	elif a == 3:
		new_tournament.date = input("\nEntrez la date du tournoi au format 01/01/1970:\n\n")
	elif a == 4:
		new_tournament.round = input("\nEntrez le nombre de tournées:\n\n")
	elif a == 5:
		new_tournament.time_control = input("\nEntrez la méthode de gestion du temps:\n\n")
	elif a == 6:
		new_tournament.players = input("\nEntrez le lieu du tournoi:\n\n")
	elif a == 7:
		new_tournament.description = input("\nAjouter une remarque:\n\n")
	print_tournament_info(new_tournament)
	choice_a = input_a()
elif choice_a == 2:
	pass
elif choice_a == 3:
	y = 1
	while y == 1:
		x = enter_new_player()
		print(x)
		player = Player(x[0], x[1], x[2], x[3], x[4])
		Tournament.ranking_list.append(x[4])
		Tournament.list_of_players.append(player)
		y = int(input("\n\n1. Ajouter un nouveau joueur\n\n2. Fin des ajouts\n\n"))
	print(Tournament.list_of_players)
	print(len(Tournament.list_of_players))


#trie des joueurs
Tournament.ranking_list.sort()
for x in range(0,len(Tournament.list_of_players)):
	for i in range(0,len(Tournament.list_of_players)):
		if Tournament.list_of_players[i].ranking == Tournament.ranking_list[x]:
			Tournament.ranked_players.append(Tournament.list_of_players[i])

#creation de paires de joueurs

for i in range(0, int(len(Tournament.list_of_players)/2)):
	hasard = random()
	if hasard < 0.5:
		color = "blancs"
		anticolor = "noirs"
	else:
		color = "noirs"
		anticolor = "blancs"
	x = len(Tournament.ranked_players) // 2
	Tournament.groupe_1.append(Tournament.ranked_players.pop(x))
	a = Tournament.groupe_1[0].name + " " + Tournament.groupe_1[0].surname + " avec les " + color
	Tournament.groupe_2.append(Tournament.ranked_players.pop())
	b = Tournament.groupe_2[0].name + " " + Tournament.groupe_2[0].surname + " avec les " + anticolor
	round_1(a, b, i+1)
Tournament.tour_1 = [Tournament.groupe_1, Tournament.groupe_2]

#1er tour1