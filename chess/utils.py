
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
	elif key == "h":
		while info.lower() != "h" and info.lower() != "f":
			info = input("\nVeillez entrer 'h' ou 'f' svp: ")
		return info
