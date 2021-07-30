from view import *
from model import *
from database import *

def check_input(info, key):
	"""Verify that user input is corresponding"""
	if key == "":
		while info == "":
			info = input("\nVeuillez entrez une saisie valide svp: ")
		return info
	elif key == int:
		while info.isdigit() == False:
			info = input("\nVeuillez entrer un chiffre svp: ")
		return int(info)
	elif key == "H":
		while info.upper() != "H" and info.upper() != "F":
			info = input("\nVeillez entrer 'H' ou 'F' svp: ")
		return info
	elif key == "T":
		while info.upper() != "BT" and info.upper() != "BZ" and info.upper() != "CR":
			info = input("\nVeillez entrer 'BT', 'BZ' ou 'CR' svp: ")
		return info
	elif key == "V":
		while info.upper() != "V" and info.upper() != "N" and info.upper() != "D":
			info = input("\nVeillez entrer 'V', 'N' ou 'D' svp: ")
		return info
	elif key == "4":
		if info.isdigit():
			return int(info)
		else:
			return 4
	elif key == "C":
		if info.upper() == "C":
			return info.upper
		else:
			info = ""
			return info


tournament = Tournament()
round = Rounds()

color = Color()
tiny = Tinydb()