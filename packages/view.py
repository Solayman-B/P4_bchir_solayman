def is_input_ok(a,b):
	if a.isdigit() and int(a) in range(1,b):
		return 0
	else:
		print(f"Votre saisie \"{a}\", ne correspond pas aux choix indiqués. Veuillez rééssayer svp. ")
		return 1


def print_tournament_info(new_tournament):
	def tournament_info(tournament_name, location, date, round, time_control):
		print(f"\nLe tournoi {tournament_name}, à lieu à {location}, en date du {date}, se joue en {round} tours, avec la méthode {time_control}")
	tournament_info(new_tournament.tournament_name, new_tournament.location, new_tournament.date, new_tournament.round, new_tournament.time_control)


def input_a():
	choice_a = input("\nEntrez le chiffre correspondant à votre choix:\n\n1. Modifier une information du tournoi ou ajouter une description\n\n2. Ajouter un joueur enregistré\n\n3. Enregistrer un nouveau joueur\n\n")
	if is_input_ok(choice_a,3) == 1:
		input_a()
	else:
		return int(choice_a)


# modifier le tournoi
def modify_tournament():
	a = input("\nEntrez le chiffre correspondant à votre choix:\n\n1. Nom du tournoi\n\n2. Lieu du tournoi\n\n3. Date du tournoi\n\n4. Nombre de tours\n\n5. Contrôle du temps\n\n6. Description\n\n")
	if is_input_ok(a, 6) == 1:
		modify_tournament()
	else:
		return int(a)

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
	results = input(f"\nRentrez les chiffres correspondants aux résultats du match {u[0]} vs {u[2]}\n\n1. pour la victoire de {u[0]} \n\n2. en cas de match nul\n\n3. pour la victoire de {u[2]}\n\n")
	if is_input_ok(results, 3) == 1:
		enter_results(u)
	else:
		return int(results)