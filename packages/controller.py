from packages.view import *
from packages.model import *
import time
from random import random


#choix de l'utilisateur de créer un nouveau tournoi ou de continuer avec le dernier utiliser
Tournament.choices.append(start_or_continue_tournament())
if Tournament.choices[-1] == 1:
	new_tournament = Tournament()
	print(enter_tournament_info(new_tournament.tournament_info, time.strftime("%d/%m/%Y"))

elif Tournament.choices[-1] == 2:
	pass
# Tournament.tournament_list[-1]

else:
	pass



"""while Tournament.choices[1] != 3:

	Tournament.choices[1] = home_menu()

	if Tournament.choices[1] == 1:
		new_tournament = Tournament(time.strftime("%d/%m/%Y"))
	elif Tournament.choices[1] == 2:
		new_tournament = modify_tournament(new_tournament)
	#elif

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
		new_tournament.round = input("\nEntrez le nombre de tours:\n\n")
	elif a == 5:
		new_tournament.time_control = input("\nEntrez la méthode de gestion du temps:\n\n")
	elif a == 6:
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
		Player.ranking_list.append(x[4])
		Tournament.list_of_players.append(player)
		y = int(input("\n\n1. Ajouter un nouveau joueur\n\n2. Fin des ajouts\n\n"))
	#print(Tournament.list_of_players[0][0])


#trie des joueurs
Player.ranking_list.sort()
for x in range(0,len(Tournament.list_of_players)):
	for i in range(0,len(Tournament.list_of_players)):
		if Tournament.list_of_players[i].ranking == Player.ranking_list[x]:
			Player.ranked_players.append(Tournament.list_of_players[i])

#creation de paires de joueurs
Tournament.nb_match = len(Tournament.list_of_players)//2
for i in range(1, Tournament.nb_match):
	hasard = random()
	if hasard < 0.5:
		color = "blancs"
		anticolor = "noirs"
	else:
		color = "noirs"
		anticolor = "blancs"
	x = len(Player.ranked_players) // 2
	Tournament.groupe_1.append(Player.ranked_players.pop(x))
	a = Tournament.groupe_1[0].name + " " + Tournament.groupe_1[0].surname
	Tournament.groupe_2.append(Player.ranked_players.pop())
	b = Tournament.groupe_2[0].name + " " + Tournament.groupe_2[0].surname
	Tournament.round_1.append(a)
	Tournament.round_1.append(0)
	Tournament.round_1.append(b)
	Tournament.round_1.append(0)
	round_1(a, b, i, color, anticolor)

#1er tour1
for i in range (1, Tournament.nb_match+1):
	a = enter_results(Tournament.round_1)
	if a == 1:
		Tournament.round_1[i] += 1
	elif a == 2:
		Tournament.round_1[i] += 0.5
		Tournament.round_1[i+2] += 0.5
	else:
		Tournament.round_1[i] = enter_results(Tournament.round_1)
	#if %2 impaire i
print(str(Tournament.round_1))"""