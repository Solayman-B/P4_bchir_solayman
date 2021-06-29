class ErrorMessagePrinting:
	def __init__(self, input):
		"""imprime un message d'erreur qui demande à l'utilisateur de saisir une entrée valide"""
		self.message = print(f"Votre saisie \"{input}\", ne correspond pas aux choix indiqués. Veuillez rééssayer svp.")

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
	pass


def is_input_ok(input,number_of_choices):
	"""Vérifie que l'entrée utilisateur corresponde bien à un choix proposé et retourne la valeur True si c'est le cas. Sinon retourne False et demande de ressaisir une entrée valide."""
	while True:
		try:
			int(input) in range(1, number_of_choices+1)
			return True
			break
		except ValueError:
			print(f"Votre saisie \"{input}\", ne correspond pas aux choix indiqués. Veuillez rééssayer svp.")
			return False
	#if input.isdigit() and int(input) in range(1,number_of_choices+1):
	#	return True
	#else:
	#	print(f"Votre saisie \"{input}\", ne correspond pas aux choix indiqués. Veuillez rééssayer svp.")
	#	return False


def start_or_continue_tournament():
	"""Propose à l'utilisateur de créer un nouveau tournoi ou de continuer avec le dernier utiliser"""
	start_or_continue_tournament_input = input("\nEntrez le chiffre correspondant à votre choix:\n\n1. Créer un nouveau tournoi.\n\n2.Continuer le dernier tournoi\n\n")
	if is_input_ok(start_or_continue_tournament_input, 2):
		return int(start_or_continue_tournament_input)

def enter_tournament_info(tournament_info, date):
	tournament_info.append(input("\nnom du tournoi: "))
	tournament_info.append(input("\nlieu du tournoi: "))
	date_input = input(f"\nla date du tournoi est le {date}, tapez \'v\' pour valider sinon tapez \'m\' pour modifier: ")
	if date_input.lower() == v:
		tournament_info.append(date)
	else:
		new_date_input = input("\nEntrez la nouvelle date au format suivant \'01/01/1970\' ou \'du 01/01/1970 au 03/01/1970\': ")
		tournament_info.append(new_date_input)
	tournee_input = input("\nLe nombre de tournées est de 4, tapez \'v\' pour valider sinon tapez \'m\' pour modifier: ")
	if tournee_input.lower() == v:
		tournament_info.append(4)
	else:
		new_tournee_input = input("\nEntrez le nombre de tournées: ")
		if is_input_ok(new_tournee_input,1000):
			tournament_info.append(int(new_tournee_input))
		else:
			tournament_info.append(4)

	tournament_info.append(input("\nEntrez \'bu\' pour bullet\n\n\'bl\' pour blitz\n\n\'cr\' pour coup rapide: "))
	tournament_info.append(input("\n: "))
	return tournament_info

def home_menu():
	home_input = input("\nEntrez le chiffre correspondant à votre choix:\n\n1. Créer un nouveau tournoi.\n\n2. Modifier le tournoi\n\n3. Débuter le tournoi\n\n4. Mettre à jour le classement\n\n5. Sauvegarder le tournoi\n\n6. Charger un tournoi\n\n")
	if is_input_ok(home_input, 6):
		return int(home_input)
	else:
		home_menu()


def print_tournament_info(new_tournament):
	def tournament_info(tournament_name, location, date, round, time_control):
		print(f"\nLe tournoi {tournament_name}, à lieu à {location}, en date du {date}, se joue en {round} tours, avec la méthode {time_control}")
	tournament_info(new_tournament.tournament_name, new_tournament.location, new_tournament.date, new_tournament.round, new_tournament.time_control)


def input_a():
	choice_a = input("\nEntrez le chiffre correspondant à votre choix:\n\n1. Ajouter un joueur enregistré\n\n2. Enregistrer un nouveau joueur\n\n")
	if is_input_ok(choice_a,2) == 1:
		input_a()
	else:
		return int(choice_a)


# modifier le tournoi
def modify_tournament(new_tournament):
	modify_tournament_input = input("\nEntrez le chiffre correspondant à votre choix:\n\n1. Nom du tournoi\n\n2. Lieu du tournoi\n\n3. Date du tournoi\n\n4. Nombre de tours\n\n5. Contrôle du temps\n\n6. Description\n\n")
	if is_input_ok(modify_tournament_input, 6) == False:
		modify_tournament()
	else:
		modify_tournament_input = int(modify_tournament_input)
		if modify_tournament_input == 1:
			new_tournament.tournament_name = input("\nEntrez le nom du tournoi:\n\n")
		elif modify_tournament_input == 2:
			new_tournament.location = input("\nEntrez le lieu du tournoi:\n\n")
		elif modify_tournament_input == 3:
			new_tournament.date = input("\nEntrez la date du tournoi au format 01/01/1970:\n\n")
		elif modify_tournament_input == 4:
			new_tournament.round = input("\nEntrez le nombre de tours:\n\n")
		elif modify_tournament_input == 5:
			new_tournament.time_control = input("\nEntrez la méthode de gestion du temps:\n\n")
		elif modify_tournament_input == 6:
			new_tournament.description = input("\nAjouter une remarque:\n\n")
	return new_tournament

# ajouter un joueur enregistré
#print(liste_des_joueurs)


# ajouter un nouveau joueur
def enter_new_player():
	name = "nom" #input("\nEntrez le nom du joueur: ")
	surname = "prenom" # input("\nSon prénom: ")
	date_of_birth = "01/01/1991" # input("\nSa date de naissance: ")
	sex = "homme" # input("\nSon sexe: ")
	ranking = int(input("\nSon rang: "))
	print(ranking)
	return name, surname, date_of_birth, sex, ranking


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