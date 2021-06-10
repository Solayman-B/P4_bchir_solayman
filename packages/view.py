tournament = "pentecote" # input("Entrez les informations du nouveau tournoi:\n\nnom du tournoi: ")

location = "Paris" # input("\nlieu du tournoi: ")

date = "09/09/2021" # input("\ndate du tournoi: ")

print(f"\nTrès bien le nouveau tournoi {tournament}, à lieu à {location}, en date du {date}")

def enter_new_players():
	name = "nom" #input("\nEntrez le nom du joueur: ")
	surname = "qui joue" # input("\nSon prénom: ")
	date_of_birth = "01/01/1991" # input("\nSa date de naissance: ")
	sex = "homme" # input("\nSon sexe: ")
	ranking = int(input("\nSon rang: "))
	return name, surname, date_of_birth, sex, ranking

#print(list des match)

#resultats = input()

