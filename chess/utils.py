

def is_digit(info):
	"""Vérifie que l'entrée utilisateur corresponde bien à un chiffre et retourne la valeur True si c'est le cas. Sinon retourne False et demande de ressaisir une entrée valide."""
	while info.isdigit() == False:
		info = input("\nVeuillez entrer un chiffre svp: ")
	return int(info)