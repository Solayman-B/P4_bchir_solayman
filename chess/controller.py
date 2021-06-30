from view import *
from model import *
import time
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

	def __call__(self):
		# entrer info tournoi
		for i in range (1,5):

			if i == 8:
				try:
					if int(info) > 1:
						self.tournament_info[3] = time.strftime(f"Du %d/%m/%Y",
																time.localtime(time) + time.strftime(f"au %d/%m/%Y",
																									 time.localtime(
																										 time + nb_days * 86400)))
					else:
						self.tournament_info[3] = time.strftime("Le %d/%m/%Y", time.localtime(time))
				except ValueError:
					print("ouh la la!")

			info = self.view.get_user_info(i)
			self.tournament.enter_informations(i, info)
		print(self.tournament.nb_days)
		if int(self.tournament.nb_days) > 1:
			info = time.strftime("Du %d/%m/%Y", time.localtime(time) + time.strftime(f"au %d/%m/%Y", time.localtime(time + self.tournament.nb_days * 86400)))
		else:
			info = time.strftime("Le %d/%m/%Y", time.localtime(time))
		self.tournament.enter_informations(5, info)
		print(self.tournament.tournament_info)



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