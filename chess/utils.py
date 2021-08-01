from view import *
from model import *
from database import *

def check_input(info, key):
	"""Verify that user input is corresponding"""
	# not empty
	if key == "":
		while info == "":
			info = input("\nVeuillez entrez une saisie valide svp: ")
		return info
	# number
	elif key == int:
		while info.isdigit() == False:
			info = input("\nVeuillez entrer un chiffre svp: ")
		return int(info)
	# sex
	elif key == "H":
		while info.upper() != "H" and info.upper() != "F":
			info = input("\nVeillez entrer 'H' ou 'F' svp: ")
		return info
	# time control
	elif key == "T":
		while info.upper() != "BT" and info.upper() != "BZ" and info.upper() != "CR":
			info = input("\nVeillez entrer 'BT', 'BZ' ou 'CR' svp: ")
		return info
	# result of a match
	elif key == "results":
		while info.upper() != "V" and info.upper() != "N" and info.upper() != "D":
			info = input("\nVeillez entrer 'V', 'N' ou 'D' svp: ")
		return info
	# number of rounds 4 by default
	elif key == "rounds":
		if info.isdigit():
			return int(info)
		else:
			return 4
	# ranking
	elif key == "ranking":
		if info.upper() == "C":
			return info.upper
		else:
			info = ""
			return info
	#tournament number
	elif key == "tournament":
		while info.isdigit() == False:
			info = input("\nVeuillez entrez un nombre svp: ")
		else:
			while int(info) > len(table_tournament):
				info = input(f"\nLe numéro de tournoi n'existe pas, veuillez entrez un nombre compris entre 1 et {len(table_tournament)} svp: ")
			else:
				return int(info)
	# resuming round
	elif key == "resuming_round":
		while info.isdigit() == False:
			info = input("\nVeuillez entrez un nombre svp: ")
		else:
			while int(info) not in range(1,5):
				info = input(f"\nLe numéro de round n'existe pas, veuillez entrez un nombre compris entre 1 et {tournament.nb_rounds} svp: ")
			else:
				return int(info)


tournament = Tournament()
round = Rounds()

color = Color()
tiny = Tinydb()