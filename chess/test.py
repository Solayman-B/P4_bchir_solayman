for i in range(tournament.nb_rounds):
	round.starting_round = datetime.datetime.now().strftime('%d/%m/%Y à %H:%M')
	Tinydb.serialize(self, table_tournament, f"debut du round {i + 1}", round.starting_round)
	print(f"le round {i + 1} à débuté le {round.starting_round} \n")
	"""sort players in two lists"""
	ranking_controller.rank_this_list(model_player.list_of_players, i)
	Tinydb.serialize(self, table_tournament, f"matchs du round {i + 1}", round.list_of_matchs_of_this_round)
	"""adding points to each player"""
	ranking_controller.enter_results()
	# mise à jour de la db avec les nouveaux points
	Tinydb.update(self)
	round.finishing_round = datetime.datetime.now().strftime('%d/%m/%Y à %H:%M')
	Tinydb.serialize(self, table_tournament, f"fin du round {i + 1}", round.finishing_round)
	round.list_of_matchs_of_this_round.insert(0, round.starting_round)
	round.list_of_matchs_of_this_round.append(round.finishing_round)
	tournament.rounds_list.append((f"Round{i + 1}", round.list_of_matchs_of_this_round))
	round.list_of_matchs_of_this_round.clear()
	print(f"le round {i + 1} s'est terminé le {round.finishing_round}\n\n			**********\n")


# if check_input(input("Si vous souhaitez modifier les classements tapez 'C' sinon appuyez sur la touche 'Entrée':\n\n>>> "), "C"):
#	ranking_update.rank_players(round.ranked_list_of_players)




def serialize(self, table, key, value):
	table.insert({key: value})