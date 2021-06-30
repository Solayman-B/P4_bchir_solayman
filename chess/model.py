import time

class Tournament:
	def __init__(self):
		self.name = ""
		self.nb_days = ""
		self.location = ""
		self.nb_participants = ""
		self.time = time.time()
		self.date = ""
		self.tournament_info = {}

	def enter_informations(self, i, info):
		self.tournament_info[i] = info




	#def save_informations(self, name, nb_days, date, location, nb_participants):
	#	self.tournament_info = {"nom du tournoi: " : name, "nombre de jours du tournoi: " : nb_days, "date du tournoi: ": date, "lieu du tournoi: " : location, "nombre de participants: ": nb_participants}


class Players:
	id = 0
	def __init__(self):
		self.id += 1
		self.name = ""
		self.surname = ""
		self.sex = ""
		self.birthdate = ""
		self.ranking = ""
		self.point = ""

class MenuEntry:
	def __init__(self, option, handler):
		self.option = option
		self.handler = handler

	def __str__(self):
		return str(self.option)

class Menu:
	def __init__(self):
		self.entries = {}
		self.autokey = 1

	def add(self, key, option, handler):
		if key == "auto":
			key = str(self.autokey)
			self.autokey += 1

		self.entries[str(key)] = MenuEntry(option, handler)

	def items(self):
		return self.entries.items()

	def __contains__(self, choice):
		return str(choice) in self.entries

	def __getitem__(self, choice):
		return self.entries[choice]


class Rounds:
	number = 1
	def __init__(self):
		self.nb_rounds = 4
		self.rounds_name = f"round{Rounds.number}"
		Rounds.number +=1

class TimeControl:
	def __init__(self):
		self.blitz = ""
		self.bullet = ""
		self.rapid = ""