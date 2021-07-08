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
		# construire un menu
		self.menu.add("auto", "créer un nouveau tournoi", NewGameController())
		self.menu.add("auto", "continuer le dernier tournoi", ResumeGameController())
		self.menu.add("auto", "mise à jour du classement", RankingUpdateController())

		# la vue affiche le menu et collecte la réponse
		user_choice = self.view.get_user_choice()

		# retourné le controlleur associé au choix au controlleur principal
		return user_choice.handler

class NewGameController:
	"""get the tournament informations"""
	def __init__(self):
		self.tournament = Tournament()
		self.view = NewGameView()
		self.tournament.starting_date = datetime.datetime.now().strftime('%d/%m/%Y')

	def __call__(self):
		# entrer info tournoi

		self.tournament.name, self.tournament.nb_days, self.tournament.location, self.tournament.time_control, self.tournament.note, = self.view.get_user_info(self.tournament)
		if self.tournament.nb_days > 1:
			self.tournament.ending_date = (datetime.datetime.now() + datetime.timedelta(days=self.tournament.nb_days)).strftime('%d/%m/%Y')
			self.tournament.date = f"du {self.tournament.starting_date} au {self.tournament.ending_date}"
		else:
			self.tournament.date = self.tournament.starting_date
		print(self.tournament.name, self.tournament.location, self.tournament.date, self.tournament.time_control, "\n")
		return PlayersController

class PlayersController:
	"""enter the players informations"""
	def __call__(self):
		model_player = Players()
		view_player = PlayersView()
		model_player.nb_players = view_player.nb_players(model_player.nb_players)
		players = [Players() for i in range(model_player.nb_players)]
		for player in players:
			model_player.list.append(list(view_player.enter_new_player(player)))

		# trie par classement des joueurs
		"""TEST SUPPRIMER LA LIGNE 65 QUI MODIFIE LA LISTE 'Players.list'"""
		model_player.list = [["Delafontaine", "Jean", "01/06/1991", "h", 0, 25, 1], ["Sarkozy", "Nicolas", "01/07/1991", "h", 0, 32, 2], ["Mouse", "Mickey", "01/08/1991", "h", 0, 21, 3], ["Éléphant", "Babar", "01/09/1991", "h", 0, 14, 4], ["Bond", "James", "01/10/1991", "h", 0, 85, 5], ["Neige", "Anna", "01/11/1991", "f", 0, 66, 6], ["Baba", "Ali", "01/12/1991", "h", 0, 47, 7], ["Ourson", "Winnie", "01/01/1991", "h", 0, 48, 8]]
		"""TEST SUPPRIMER LA LIGNE 65 QUI MODIFIE LA LISTE 'Players.list'"""
		ranking_controller = RankingController()
		# 								points [4] ranking [5]
		ranking_controller.rank_this(model_player.list, 4, 5)


class RankingController:
	"""sort the players and split them into two lists"""
	def rank_this(self,list, points, ranking):
		round_1 = Ranking()
		round_1.ranked_list = sorted(list, key=itemgetter(points, ranking))
		lenth_list = len(round_1.ranked_list) // 2
		list_1 = round_1.ranked_list[:lenth_list]
		list_2 = round_1.ranked_list[lenth_list:]
		self.generating_pairs(list_1,list_2)
		self.enter_results(round_1.ranked_list)

	def generating_pairs(self,list_1, list_2):
		match = Match()
		color = Color()
		z = 1
		for x,y in zip(list_1, list_2):
			i = x,y
			match.list.append(i)
			print(f"Match {z} {x[0]} {x[1]} avec les {color.random()} affrontera {y[0]} {y[1]}")
			z += 1

	def enter_results(self,list):
		z = 0
		for i in list:
			results = ResultsView.enter_results(i)
			a = list[z].pop(4)
			if results == "V":
				list[z].insert(4, 1 + a)
			elif results == "N":
				list[z].insert(4, 0.5 + a)
			else:
				list[z].insert(4, 0 + a)
			z += 1

		print(list)

class ResumeGameController:
	def __call__(self):
		print("resumegame controller")


class RankingUpdateController:
	def __call__(self):
		print("ranking controller")


		#if input.isdigit() == True:
		#	return True
		#else:
		#	return False