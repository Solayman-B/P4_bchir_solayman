from random import random

class Tournament:
	def __init__(self):
		self.name = str()
		self.nb_days = int()
		self.location = str()
		self.time = None
		self.starting_date = None
		self.ending_date = None
		self.time_control = str()
		self.note = str()
		self.rounds_list = []
		self.nb_rounds = 4
		self.categories = ["nom", "nombre de jours", "lieu", "control du temps", "nombre de rounds", "note"]


class Players:
	id = 1
	def __init__(self):
		self.name = str()
		self.surname = str()
		self.sex = str()
		self.birthdate = None
		self.ranking = int()
		self.points = float()
		self.id = Players.id
		self.nb_players = int()
		self.list_of_players = []
		self.categories = ["nom", "prenom", "sexe", "date de naissance", "classement", "nombre de points", "identifiant"]
		Players.id += 1

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
	def __init__(self):
		self.starting_round = str()
		self.finishing_round = str()
		self.ranked_list_of_players = []
		self.list_of_played_matchs = []
		self.list_of_matchs_of_this_round = []
		self.players_to_reintegrate = []
		self.players_to_match = []


class Color:
	def random(self):
		if random() < 0.5:
			color = "blancs"
		else:
			color = "noirs"
		return color

class Rapports:
	pass