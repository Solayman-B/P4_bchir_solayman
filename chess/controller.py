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
		




class ResumeGameController:
	def __call__(self):
		print("resumegame controller")


class RankingUpdateController:
	def __call__(self):
		print("ranking controller")

def is_input_ok(input,number_of_choices):
	"""Vérifie que l'entrée utilisateur corresponde bien à un choix proposé et retourne la valeur True si c'est le cas. Sinon retourne False et demande de ressaisir une entrée valide."""
	while True:
		try:
			int(input) in range(1, number_of_choices+1)
			return True
			break
		except ValueError:
			#ErrorMessagePrinting(input)
			return False
	#if input.isdigit() and int(input) in range(1,number_of_choices+1):
	#	return True
	#else:
	#	print(f"Votre saisie \"{input}\", ne correspond pas aux choix indiqués. Veuillez rééssayer svp.")
	#	return False