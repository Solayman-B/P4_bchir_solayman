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

		self.tournament.name, self.tournament.nb_days, self.tournament.location, self.tournament.note, = self.view.get_user_info(self.tournament)
		if self.tournament.nb_days > 1:
			self.tournament.ending_date = (datetime.datetime.now() + datetime.timedelta(days=self.tournament.nb_days)).strftime('%d/%m/%Y')
			self.tournament.date = f"du {self.tournament.starting_date} au {self.tournament.ending_date}"
		else:
			self.tournament.date = self.tournament.starting_date
		print(self.tournament.name, self.tournament.location, self.tournament.date)
		return PlayersController

class PlayersController:
	"""enter the players informations"""
	def __call__(self):
		Players.nb_players = PlayersView.nb_players(self, Players.nb_players)
		players = [Players() for i in range(Players.nb_players)]
		for player in players:
			Players.list.append(PlayersView.enter_new_player(self, player))

		# trie par classement des joueurs
		"""TEST SUPPRIMER LA LIGNE 65 QUI MODIFIE LA LISTE 'Players.list'"""
		Players.list = [("Delafontaine", "Jean", "01/06/1991", "h", 0, 25), ("Sarkozy", "Nicolas", "01/07/1991", "h", 0, 32), ("Mouse", "Mickey", "01/08/1991", "h", 0, 21), ("Éléphant", "Babar", "01/09/1991", "h", 0, 14), ("Bond", "James", "01/10/1991", "h", 0, 85), ("Neige", "Anna", "01/11/1991", "f", 0, 66), ("Baba", "Ali", "01/12/1991", "h", 0, 47), ("Ourson", "Winnie", "01/01/1991", "h", 0, 48)]
		"""TEST SUPPRIMER LA LIGNE 65 QUI MODIFIE LA LISTE 'Players.list'"""
		RankingController.rank_this(self, Players.list, 4, 5)


class RankingController:
	"""sort the players and split them into two lists"""
	def rank_this(self, list, points, ranking):
		ranked_list = sorted(list, key=itemgetter(points, ranking))
		print(f"{ranked_list} ranked list")
		lenth_list = len(ranked_list) // 2
		list_1 = ranked_list[:lenth_list]
		list_2 = ranked_list[lenth_list:]
		PairsOfPlayers.generating_pairs(self,list_1,list_2)

class PairsOfPlayers:
	"""generating pairs of players"""
	def generating_pairs(self,list_1, list_2):
		match = Match()
		for i in zip(list_1, list_2):
			match.list.append(i)
		print(f"{match.list} match list")



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