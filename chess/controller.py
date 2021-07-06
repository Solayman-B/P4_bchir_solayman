from view import *
from model import *
import datetime
from random import random


class ApplicationController:

	def __init__(self):
		self.controller = None

	def start(self):
		self.controller = HomeMenuController()
		while self.controller:
			self.controller = self.controller()

class HomeMenuController:

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
	def __call__(self):
		Players.nb_players = PlayersView.nb_players(self, Players.nb_players)
		players = [Players() for i in range(Players.nb_players)]
		for player in players:
			Players.list.append(PlayersView.enter_new_player(self, player, Players.id))

		print(f"{Players.list} Players.list")
		# trie par classement des joueurs
		#RankingController(Players.list, Players.ranking, Players.ranking[0])

class RankingController:
	def __call__(self, list, id, indice):
		sorted(list, key = lambda id: indice)


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