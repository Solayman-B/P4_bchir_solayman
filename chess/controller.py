from operator import itemgetter
from view import *
from model import *
import datetime


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
		self.menu.add("auto", "créer un nouveau tournoi", NewGameController())
		self.menu.add("auto", "continuer le dernier tournoi", ResumeGameController())
		self.menu.add("auto", "mise à jour du classement", RankingUpdateController())

		# the view display the menu and get the response
		user_choice = self.view.get_user_choice()

		# Give the user choice handler
		return user_choice.handler

class NewGameController:
	"""get the tournament informations"""
	def __init__(self):
		self.view = NewGameView()
		tournament.starting_date = datetime.datetime.now().strftime('%d/%m/%Y')

	def __call__(self):
		# entrer info tournoi
		tournament.name, tournament.nb_days, tournament.location, tournament.time_control, tournament.note = self.view.get_user_info(tournament)
		if tournament.nb_days > 1:
			tournament.ending_date = (datetime.datetime.now() + datetime.timedelta(days=tournament.nb_days)).strftime('%d/%m/%Y')
			tournament.date = f"du {tournament.starting_date} au {tournament.ending_date}"
		else:
			tournament.date = tournament.starting_date
		print("\n", tournament.name, tournament.location, tournament.date, tournament.time_control, "\n")
		return PlayersController

class PlayersController():
	"""enter the players informations"""
	def __call__(self):
		model_player = Players()
		view_player = PlayersView()
		model_player.nb_players = view_player.nb_players(model_player.nb_players)
		players = [Players() for i in range(model_player.nb_players)]
		for player in players:
			model_player.list_of_players.append(list(view_player.enter_new_player(player)))

		# trie par classement des joueurs
		"""TEST SUPPRIMER LA LIGNE 65 QUI MODIFIE LA LISTE 'Players.list'"""
		model_player.list_of_players = [["Delafontaine", "Jean", "01/06/1991", "h", 0, 25, 1], ["Sarkozy", "Nicolas", "01/07/1991", "h", 0, 32, 2], ["Mouse", "Mickey", "01/08/1991", "h", 0, 21, 3], ["Éléphant", "Babar", "01/09/1991", "h", 0, 14, 4], ["Bond", "James", "01/10/1991", "h", 0, 85, 5], ["Neige", "Anna", "01/11/1991", "f", 0, 66, 6], ["Baba", "Ali", "01/12/1991", "h", 0, 47, 7], ["Ourson", "Winnie", "01/01/1991", "h", 0, 48, 8]]
		"""TEST SUPPRIMER LA LIGNE 65 QUI MODIFIE LA LISTE 'Players.list'"""


		"""starting the rounds of the tournament"""
		ranking_controller = RankingController()
		round = Rounds()
		for i in range(round.nb_rounds):
			round.starting_round = datetime.datetime.now().strftime('%d/%m/%Y à %H:%M')
			print(f"le round {i+1} à débuté le {round.starting_round} \n")
			"""sort players in two lists"""
			ranking_controller.rank_this_list(model_player.list_of_players, i, round)
			round.finishing_round = datetime.datetime.now().strftime('%d/%m/%Y à %H:%M')
			round.list_of_matchs_of_this_round.insert(0, round.starting_round)
			round.list_of_matchs_of_this_round.append(round.finishing_round)
			tournament.rounds_list.append(f"Round{i+1}")
			tournament.rounds_list.append(round.list_of_matchs_of_this_round)
			round.list_of_matchs_of_this_round.clear()
			print(f"le round {i+1} s'est terminé le {round.finishing_round}\n\n			**********\n")



class RankingController:

	"""sort the players by points (4), and if they're equal by ranking (5), and split them into two separated lists"""

	def rank_this_list(self,list_of_players, i, round):
		match_view = MatchView()
		color = Color()
		round.ranked_list_of_players = sorted(sorted(list_of_players, key=itemgetter(5)), key=itemgetter(4), reverse= True)
		lenth_ranked_list_of_players = len(round.ranked_list_of_players) // 2
		if i == 0:
			for player_1, player_2 in zip(round.ranked_list_of_players[:lenth_ranked_list_of_players],
										  round.ranked_list_of_players[lenth_ranked_list_of_players:]):
				match = [player_1[6], player_1[4]], [player_2[6], player_2[4]]
				round.list_of_matchs_of_this_round.append(match)
				match_view.display_match(color.random(), match[0], match[1])
			self.enter_results(round)

		else:
			def play_it(match):
				if len(round.list_of_matchs_of_this_round) != lenth_ranked_list_of_players:
					match_view.display_match(color.random(), match[0], match[1])
					round.list_of_matchs_of_this_round.append(match)
					self.enter_results(round)

			def is_match_already_played(player_1, player_2):
				if (player_1, player_2) in round.list_of_played_matchs or (player_2, player_1) in round.list_of_played_matchs:
					round.players_to_reintegrate.append(player_1)
					round.players_to_reintegrate.append(player_2)
				else:
					play_it((player_1, player_2))

			while len(round.list_of_matchs_of_this_round) !=lenth_ranked_list_of_players:
				for player_1, player_2 in zip(list_of_players[::2], list_of_players[1::2]):
					if round.players_to_reintegrate:
						p3 = round.players_to_reintegrate.pop()
						p4 = round.players_to_reintegrate.pop()
						is_match_already_played([player_1[6], player_1[4]],  p3)
						is_match_already_played([player_2[6], player_2[4]], p4)
					else:
						is_match_already_played([player_1[6], player_1[4]], [player_2[6], player_2[4]])


	def enter_results(self,round):
		"""saving the points earned by each player during the last match"""
		results = ResultsView()
		z = 0
		for player in round.ranked_list_of_players:
			results.enter_results(player)
			# removed old points
			a = round.ranked_list_of_players[z].pop(4)
			# saving new points
			if results == "V":
				round.ranked_list_of_players[z].insert(4, 1.0 + a)
			elif results == "N":
				round.ranked_list_of_players[z].insert(4, 0.5 + a)
			else:
				round.ranked_list_of_players[z].insert(4, 0.0 + a)
			z += 1
		for match in round.list_of_matchs_of_this_round:
			round.list_of_played_matchs.append(match)

class ResumeGameController:
	def __call__(self):
		print("resumegame controller")


class RankingUpdateController:
	def __call__(self):
		print("ranking controller")