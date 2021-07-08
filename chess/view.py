from utils import *

class HomeMenuView:
	def __init__(self, menu):
		self.menu = menu

	def display_menu(self):
		for key, entry in self.menu.items():
			print(f"{key}: {entry.option}\n")

	def get_user_choice(self):
		while True:
			# afficher le menu
			self.display_menu()
			# demander un choix à l'utilisateur
			choice = input(">> ")
			# valider le choix
			if choice in self.menu:
				# retourner le choix
				return self.menu[choice]

class NewGameView:
	def __init__(self):
		pass

	def get_user_info(self, tournament):

		tournament.name = "Acacias"# check_input(input("\nNom du tournoi: "),"")
		tournament.nb_days = 2# check_input(input("\nDurée en jours du tournoi: "), int)
		tournament.location = "Paris"# check_input(input("\nLieu du tournoi: "), "")
		tournament.time_control = "blitz" # check_input(input("\nContrôle du temps de jeu:\n\nEntrez 'BT' pour bullet, 'BZ' pour blitz, 'CR' pour coup rapide: "), 'T')
		tournament.note = ""# input("\nAjouter une remarque ou tapez 'Enrée' pour continuer ")
		return tournament.name, tournament.nb_days, tournament.location, tournament.time_control, tournament.note


class PlayersView:
	# nombre de joueurs
	def nb_players(self, nb_players):
		nb_players = 8 #check_input(input("\nCombien de joueurs voulez vous ajouter ? "), int)
		return nb_players

	# ajouter un nouveau joueur
	def enter_new_player(self, player):
		player.name = ""#check_input(input(f"\nEntrez le nom du joueur: "), "")
		player.surname = ""#check_input(input("\nSon prénom: "),"")
		player.date_of_birth = ""#check_input(input("\nSa date de naissance sous la forme JJ/MM/AAAA: "), "")
		player.sex = ""#check_input(input("\nSon sexe 'H' ou 'F': "), "H")
		player.points = 0.0
		player.ranking = ""#check_input(input("\nSon rang: "), int)
		return player.name, player.surname, player.date_of_birth, player.sex, player.points, player.ranking, player.id


#resultats = input()
class ResultsView:
	def enter_results(i):
		results = check_input(input(f"\nJoueur :{i}  \n\nEntrez 'V' pour une victoire, 'N' pour un match nul, et 'D' pour une défaite: "), "V")
		return results
