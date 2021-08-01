import random
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
			choice = input("\n\n>>> ")
			# valider le choix
			if choice in self.menu:
				# retourner le choix
				return self.menu[choice]

class NewGameView:
	def get_user_info(self, tournament):
		tournament.name = "Acacias"  # check_input(input("\nNom du tournoi:\n\n>>> "),"")
		tournament.nb_days = 2  # check_input(input("\nDurée en jours du tournoi:\n\n>>> "), int)
		tournament.location = "Paris"  # check_input(input("\nLieu du tournoi:\n\n>>> "), "")
		tournament.time_control = "blitz"  # check_input(input("\nContrôle du temps de jeu:\n\nEntrez 'BT' pour bullet, 'BZ' pour blitz, 'CR' pour coup rapide:\n\n>>> "), 'T')
		tournament.note = ""  # input("\nAjouter une remarque ou tapez 'Entrée' pour continuer:\n\n>>> ")
		tournament.nb_rounds = 4  # check_input(input("Le nombre de tours est de 4, entrez un nouveau nombre pour le modifier sinon appuyez sur 'Entrée':\n\n>>> "), "rounds")
		return {"nom": tournament.name, "lieu": tournament.location, "nombre_de_jours": tournament.nb_days, "date_de_debut": tournament.starting_date, "date_de_fin": tournament.ending_date, "nombre_de_tours": tournament.nb_rounds, "joueurs": "", "control_du_temps": tournament.time_control,"note": tournament.note, "debut_du_round_1": "", "matchs_du_round_1": [], "fin_du_round_1": "", "debut_du_round_2": "", "matchs_du_round_2": [], "fin_du_round_2": "", "debut_du_round_3": "", "matchs_du_round_3": [], "fin_du_round_3": "", "debut_du_round_4": "", "matchs_du_round_4": [], "fin_du_round_4": ""}

class PlayersView:
	# nombre de joueurs
	def nb_players(self, nb_players):
		nb_players = 8 #check_input(input("\nCombien de joueurs voulez vous ajouter ? "), int)
		return nb_players

	# ajouter un nouveau joueur
	def enter_new_player(self, player):
		player.name =""# check_input(input(f"\nEntrez le nom du joueur:\n\n>>> "), "")
		player.surname = ""# check_input(input("\nSon prénom:\n\n>>> "),"")
		player.date_of_birth =""# check_input(input("\nSa date de naissance sous la forme JJ/MM/AAAA:\n\n>>> "), "")
		player.sex =""# check_input(input("\nSon sexe 'H' ou 'F':\n\n>>> "), "H")
		player.points = 0.0
		player.ranking =""# check_input(input("\nSon rang:\n\n>>> "), int)
		return {"nom": player.name, "prenom": player.surname, "date de naissance": player.date_of_birth, "sexe": player.sex, "nombre de points": player.points, "classement": player.ranking, "id": player.id}


class MatchView:
	def display_match(self, color, p1, p2):

		print(f"Le joueur {p1} avec les {color} affrontera le joueur {p2}\n")

#resultats = input()
class ResultsView:
	def enter_results(self, player):
		results = "V" #random.choice("VDN") #check_input(input(f"\nJoueur: {player[6]}  \n\nEntrez 'V' pour une victoire, 'N' pour un match nul, et 'D' pour une défaite:\n\n>>> "), "results")
		return results

class RapportsView:


	def choice(self):
		choice = check_input(input("Vous souhaitez afficher un rapport contenant:"
								   "\n\n1/ Les acteurs par ordre alphabétique"
								   "\n\n2/ Les acteurs par classement"
								   "\n\n3/ Les joueurs d'un tournoi par ordre alphabétique"
								   "\n\n4/ Les joueurs d'un tournoi par classement"
								   "\n\n5/ Tous les tournois"
								   "\n\n6/ Les tours d'un tournois"
								   "\n\n7/ Les matchs d'un tournoi"
								   "\n\n8/ Retour au menu principal"
								   "\n\n>>>   "), int)
		return choice