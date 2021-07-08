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


class Players:
	id = 0
	nb_players = int()
	list = []
	def __init__(self):
		self.name = str()
		self.surname = str()
		self.sex = str()
		self.birthdate = None
		self.ranking = int()
		self.points = float()
		self.id = Players.id
		Players.id += 1


class Ranking:
	ranked_list = []

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

class Match:
	def __init__(self):
		self.list = []

class Color:
	def random(self):
		if random() < 0.5:
			color = "blancs"
		else:
			color = "noirs"
		return color

class Results:
	pass