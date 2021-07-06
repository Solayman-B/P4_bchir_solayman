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

		tournament.name = check_input(input("\nNom du tournoi: "),"")
		tournament.nb_days = check_input(input("\nDurée en jours du tournoi: "), int)
		tournament.location = check_input(input("\nLieu du tournoi: "), "")
		tournament.note = input("\nAjouter une remarque ou tapez 'Enrée' pour continuer ")
		return tournament.name, tournament.nb_days, tournament.location, tournament.note


class PlayersView:
	# nombre de joueurs
	def nb_players(self, nb_players):
		nb_players = check_input(input("\nCombien de joueurs voulez vous ajouter ? "), int)
		return nb_players

	# ajouter un nouveau joueur
	def enter_new_player(self, player):
		player.name = check_input(input(f"\nEntrez le nom du joueur: "), "")
		player.surname = check_input(input("\nSon prénom: "),"")
		player.date_of_birth = check_input(input("\nSa date de naissance sous la forme JJ/MM/AAAA: "), "")
		player.sex = check_input(input("\nSon sexe 'H' ou 'F': "), "h")
		player.ranking = check_input(input("\nSon rang: "), int)
		player.points = 0.0
		return player.name, player.surname, player.date_of_birth, player.sex, player.points, player.ranking

#print(list des match)
def round_1 (a,b, i, color, anticolor):
	print(f"match {i}. {a} avec les {color} affrontera {b} avec les {anticolor}")


#resultats = input()
def enter_results(u):
	enter_results_input = input(f"\nRentrez les chiffres correspondants aux résultats du match {u[0]} vs {u[2]}\n\n1. pour la victoire de {u[0]} \n\n2. en cas de match nul\n\n3. pour la victoire de {u[2]}\n\n")
	if is_input_ok(enter_results_input, 3) == False:
		enter_results(u)
	else:
		return int(enter_results_input)