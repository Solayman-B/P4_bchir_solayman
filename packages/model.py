time_control =["bullet", "blitz", "coup rapide"]

class Tournament:

		number = 0
		list_of_players = []
		round_1 = []
		groupe_1 = []
		groupe_2 = []
		nb_match = 0

		def __init__(self, date):
			self.tournament_name = "nom du tournoi" #input("\nnom du tournoi: ")
			self.location = "lieu du tournoi" #input("\nlieu du tournoi: ")
			self.date = date
			self.round = 4
			self.time_control = "blitz" #time_control[int(input("\nEntrez le chiffre correspondant à la méthode de contrôle du temps:\n\n1. bullet\n\n2. blitz\n\n3. coup rapide\n\n"))-1]
			self.description = ""
			Tournament.number += 1

class Player:
	ranking_list = []
	ranked_players = []

	def __init__(self, name, surname, date_of_birth, sex, ranking):
		self.name = name
		self.surname = surname
		self.date_of_birth = date_of_birth
		self.sex = sex
		self.ranking = ranking


#tournament_info =


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