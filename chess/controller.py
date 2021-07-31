from view import *
from model import *
from database import *
import datetime
from utils import *
from operator import itemgetter


class ApplicationController:

	def __init__(self):
		self.controller = None
	"""start the application"""
	def start(self):
		self.controller = HomeMenuController()
		while self.controller:
			self.controller = self.controller()

class HomeMenuController:
	"""Print the home menu et get the user response"""
	def __init__(self):
		self.menu = Menu()
		self.view = HomeMenuView(self.menu)

	def __call__(self):
		# build the menu
		self.menu.add("auto", "nouveau tournoi", NewGameController())
		self.menu.add("auto", "charger un tournoi", ResumeGameController())
		self.menu.add("auto", "afficher les rapports", RapportsController())

		# the view display the menu and get the response
		user_choice = self.view.get_user_choice()

		# Give the handler choiced by the user
		return user_choice.handler

class NewGameController:
	"""get the tournament informations"""
	def __init__(self):
		tournament.starting_date = datetime.datetime.now().strftime('%d/%m/%Y')

	def __call__(self):
		# enter the tournament informations
		new_game_view = NewGameView()

		for i in range(10):
			value = new_game_view.get_user_info(tournament)
		tiny.serialize(table_tournament, value)
		if tournament.nb_days > 1:
			tournament.ending_date = (datetime.datetime.now() + datetime.timedelta(days=tournament.nb_days)).strftime('%d/%m/%Y')
			tournament.date = f"du {tournament.starting_date} au {tournament.ending_date}"
		else:
			tournament.date = tournament.starting_date
			tournament.ending_date = tournament.starting_date
		tiny.update(table_tournament, {"date_de_fin": tournament.ending_date}, query.date_de_debut == tournament.starting_date)


		print("\n", tournament.name, tournament.location, tournament.date, tournament.time_control, "\n")

		return PlayersController

class PlayersController():
	"""enter the players informations"""
	def __call__(self):
		model_player = Players()
		view_player = PlayersView()
		# récupérer joueurs déjà présents dans la DB
		model_player.nb_players = view_player.nb_players(model_player.nb_players)
		players = [Players() for i in range(model_player.nb_players)]
		for player in players:
			model_player.list_of_players.append(view_player.enter_new_player(player))
		""" MODIFIE LA LISTE 'Players.list' POUR LES TESTS """
		model_player.list_of_players = [{"nom": "Delafontaine", "prenom": "Jean", "date_de_naissance": "01/06/1991", "sexe": "h", "nombre_de_points": 0.0, "classement": 25, "id": 1}, {"nom": "Sarkozy", "prenom": "Nicolas", "date_de_naissance": "01/07/1991", "sexe": "h", "nombre_de_points": 0.0, "classement": 32, "id": 2}, {"nom": "Mouse", "prenom": "Mickey", "date_de_naissance": "01/08/1991", "sexe": "h", "nombre_de_points": 0.0, "classement": 21, "id": 3}, {"nom": "Elephant", "prenom": "Babar", "date_de_naissance": "01/09/1991", "sexe": "h", "nombre_de_points": 0.0, "classement": 14, "id": 4}, {"nom": "Bond", "prenom": "James", "date_de_naissance": "01/10/1991", "sexe": "h", "nombre_de_points": 0.0, "classement": 85, "id": 5}, {"nom": "Neige", "prenom": "Anna", "date_de_naissance": "01/11/1991", "sexe": "f", "nombre_de_points": 0.0, "classement": 66, "id": 6}, {"nom": "Baba", "prenom": "Ali", "date_de_naissance": "01/12/1991", "sexe": "h", "nombre_de_points": 0.0, "classement": 47, "id": 7}, {"nom": "Ourson", "prenom": "Winnie", "date_de_naissance": "01/01/1991", "sexe": "h", "nombre_de_points": 0.0, "classement": 48, "id": 8}]
		"""  MODIFIE LA LISTE 'Players.list' POUR LES TESTS """
		#print(table_tournament.get(doc_id=1)["joueurs"])
		z = 0
		tiny.update(table_tournament, {"joueurs": tuple(model_player.list_of_players)},
					query.date_de_debut == tournament.starting_date)
		for player in model_player.list_of_players:
			tiny.serialize(table_players, player)
			z += 1

		"""starting the rounds of the tournament"""
		ranking_update = RankingUpdateController()
		ranking_controller = RankingController()
		for i in range(tournament.nb_rounds):
			# if check_input(input("Si vous souhaitez modifier le classement tapez 'C' sinon appuyez sur la touche 'Entrée':\n\n>>> "), "ranking"):
			#	ranking_update.rank_players(round.ranked_list_of_players)
			round.starting_round = datetime.datetime.now().strftime('%d/%m/%Y à %H:%M')
			tiny.update(table_tournament, {f"debut_du_round {i+1}": round.starting_round}, query.date_de_debut == tournament.starting_date)
			print(f"le round {i+1} à débuté le {round.starting_round} \n")
			"""sort players in two lists"""
			ranking_controller.rank_this_list(model_player.list_of_players, i)
			"""adding points to each player"""
			ranking_controller.enter_results()
			tiny.update(table_tournament, {f"matchs du round {i + 1}": round.matchs_of_this_round_db}, query.date_de_debut == tournament.starting_date)
			round.matchs_of_this_round_db.clear()
			round.finishing_round = datetime.datetime.now().strftime('%d/%m/%Y à %H:%M')
			tiny.update(table_tournament, {f"fin du round {i+1}": round.finishing_round}, query.date_de_debut == tournament.starting_date)
			round.list_of_matchs_of_this_round.insert(0, round.starting_round)
			round.list_of_matchs_of_this_round.append(round.finishing_round)
			tournament.rounds_list.append((f"Round{i+1}", round.list_of_matchs_of_this_round))
			round.list_of_matchs_of_this_round.clear()
			print(f"le round {i+1} s'est terminé le {round.finishing_round}\n\n			**********\n")
		# if check_input(input("Si vous souhaitez modifier le classement tapez 'C' sinon appuyez sur la touche 'Entrée':\n\n>>> "), "ranking"):
		#	ranking_update.rank_players(round.ranked_list_of_players)


		print("Fin du tournoi.")

class RankingController:
	"""sort the players by points (4), and if they're equal by ranking (5), and split them into two separated lists"""
	def play_it(self, p1, p2, lenth_ranked_list_of_players):
		match_view = MatchView()
		if len(round.list_of_matchs_of_this_round) != lenth_ranked_list_of_players:
			match_view.display_match(color.random(), (p1["id"], p1["nom"], p1["prenom"]), (p2["id"], p2["nom"], p2["prenom"]))
			match = p1["id"], p2["id"]
			round.list_of_matchs_of_this_round.append(match)

	def is_match_already_played(self, p1, p2, lenth_ranked_list_of_players):
		if (p1["id"], p2["id"]) in round.list_of_played_matchs or (p2["id"], p1["id"]) in round.list_of_played_matchs:
			round.players_to_reintegrate.append(p1)
			round.players_to_reintegrate.append(p2)
		else:
			self.play_it(p1, p2, lenth_ranked_list_of_players)

	def rank_this_list(self, list_of_players, i):
		list_of_players = sorted(list_of_players, key=lambda i: i['classement'])
		round.ranked_list_of_players = sorted(list_of_players, key=lambda i: i['nombre_de_points'], reverse=True)
		lenth_ranked_list_of_players = len(round.ranked_list_of_players) // 2
		# for the 1st round
		if i == 0:
			for p1, p2 in zip(round.ranked_list_of_players[:lenth_ranked_list_of_players],
										  round.ranked_list_of_players[lenth_ranked_list_of_players:]):
				self.play_it(p1, p2, lenth_ranked_list_of_players)
		# for the others rounds
		else:
			while len(round.list_of_matchs_of_this_round) != lenth_ranked_list_of_players:
				for p1, p2 in zip(list_of_players[::2], list_of_players[1::2]):
					if round.players_to_reintegrate:
						p3 = round.players_to_reintegrate.pop()
						p4 = round.players_to_reintegrate.pop()
						self.is_match_already_played(p1,  p3, lenth_ranked_list_of_players)
						self.is_match_already_played(p2, p4, lenth_ranked_list_of_players)
					else:
						self.is_match_already_played(p1, p2, lenth_ranked_list_of_players)


	def enter_results(self):
		"""saving the points earned by each player during the last match"""
		results = ResultsView()
		for player in round.ranked_list_of_players:
			result = results.enter_results(player)
			# saving new points
			if result == "V":
				player["nombre_de_points"] += 1.0
			elif result == "N":
				player["nombre_de_points"] += 0.5
			else:
				player["nombre_de_points"] += 0.0
			#mise à jour de la db avec les nouveaux points
			nb_points = player["nombre_de_points"]
			tiny.update(table_players, {"nombre_de_points": nb_points}, query.id == player["id"])
		for match in round.list_of_matchs_of_this_round:
			round.list_of_played_matchs.append(match)
			round.matchs_of_this_round_db.append([(match[0], player["nombre_de_points"]), (match[1], player["nombre_de_points"])])

class ResumeGameController:
	def __call__(self):
		print("resumegame controller")

class RapportsController:
	def __call__(self):
		rapport = RapportsView()
		choice = rapport.choice()
		app = ApplicationController()

		while rapport:
			"""\n\n1/ Les acteurs par ordre alphabétique"
			
			   "\n\n2/ Les acteurs par classement"
			   """

			if choice == 1:
				pass
			elif choice == 2:
				pass
			elif choice == 3:
				num_tournament = check_input(input("Veuillez entrer le n° du tournoi (cf liste des tournois): "), "tournament")
				print(sorted(table_tournament.get(doc_id=num_tournament)["joueurs"], key = lambda i: i["nom"]) )
			elif choice == 4:
				num_tournament = check_input(input("Veuillez entrer le n° du tournoi (cf liste des tournois): "),
											 "tournament")
				print(sorted(table_tournament.get(doc_id=num_tournament)["joueurs"], key=lambda i: i["classement"]))
			elif choice == 5:
				print("Liste des tournois\n\n")
				for row in range(1,len(table_tournament)+1):
					print(f"Tournoi n°{row}\n\n")
					for category in tournament.categories:
						print(category, ": ", table_tournament.get(doc_id=row)[category])
					for player in table_tournament.get(doc_id=row)["joueurs"]:
						print("joueurs : ", player["id"], player["nom"], player["prenom"])
					print("\n\n")
						#print("joueurs : ", table_tournament.get(doc_id=row)["joueurs"][6],"\n\n")
					#for category in tournament.categories:
					#	print(category, a[category], "LES CATEGORIES")

			elif choice == 6:
				# rounds of the tournament
				print("Liste des tours d'un tournois\n\n")
				print(table_tournament.search(query.name =="Mexique"), "MEXIQQQQQQQQQUE")
				for i in range(9, 21):
					print(table_tournament.get(doc_id=i), "\n\n")
			elif choice == 7:
				# matchs of the tournament
				print("Liste des matchs d'un tournoi\n\n")
				for i in (10, 13, 16, 19):
					print(*table_tournament.get(doc_id=i).values(), "\n\n")
			else:
				# return to the home menu
				app.start()
				break
			choice = rapport.choice()




class RankingUpdateController:
	def rank_players(self, list):
		i = 0
		for player in list:
			ranking = check_input(input(f"Entrez le nouveau rang du joueur : {player}:\n\n>>> "), int)
			list.pop(0)
			player[5] = ranking
			list.insert(0,player)
			tiny.update(table_players, {"classement": ranking}, query.id == player["id"])
			i +=1