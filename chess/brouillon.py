from packages.view import *
from packages.model import *
import time
from random import random


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
print(str(Tournament.round_1))