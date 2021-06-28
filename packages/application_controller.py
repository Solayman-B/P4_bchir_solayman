from models.menu import Menu
from packages.home_menu import HomeMenuView

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
		Menu.add("auto", "créer un nouveau tournoi", NewGameController())
		Menu.add("auto", "continuer le dernier tournoi", ResumeGameController())
		Menu.add("auto", "mise à jour du classement", RankingUpdateController())

		# la vue affiche le menu et collecte la réponse
		user_choice = self.view.get_user_choice()

		#retourné le controlleur associé au choix au controlleur principal
		return user_choice.handler

class NewGameController:

	pass


class ResumeGameController:

	pass


class RankingUpdateController:

	pass


app = ApplicationController()
app.start()