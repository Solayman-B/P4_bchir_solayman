class Tournoi:
    def __init__(self, tournament, location, date):
        self.tournament = tournament
        self.location = location
        self.date = date
        self.number_of_turns = 4
        self.round = ""
        self.time_control = ""
        self.description = ""


def number_of_players(p = 8):
    players = []
    for i in range(1,p+1):
        players.append("player" + str(i))
    return players


class Player:
    def __init__(self, name, surname, date_of_birth, sex, ranking):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.ranking = ranking


def save_a_player(player):
    #mauvais format du texte
    with open("players.csv", "a") as file:
        file.write(player)
        print(player)

def enter_new_players(player):
	name = input("\nEntrez le nom du joueur: ")
	surname = input("\nSon prénom: ")
	date_of_birth = input("\nSa date de naissance: ")
	sex = input("\nSon sexe: ")
	ranking = input("\nSon rang: ")
	return name, surname, date_of_birth, sex, ranking

test

#class 1er Tour:
 #   trie les joueurs par classement
  #  divise les joueurs en 2 moitié (supérieur et inférieur)
   # les 1er de chaque moitié s affrontent etc

#class autre Tour:
 #   while joueurs pas affrontés
  #  trie les joueurs par point
   # si meme point par classement
    #1 et 2, 3 et 4 si joueur déjà rencontré le suivant

#randint couleur noir ou blanc pour partie