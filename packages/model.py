

class Tournament:
	def __init__(self):
		self.name =""
		self.nb_days = ""
		self.date = ""
		self.location = ""
		self.nb_participants = ""

class Players:
	id = 1
	def __init__(self):
		self.id = Players.id
		Players.id += 1
		self.name = ""
		self.surname = ""
		self.sex = ""
		self.birthdate = ""
		self.ranking = ""
		self.point = ""

class Menu:
	def __init__(self):
		self._entries = {}
		self._autokey = 1

	def add(self, key, handler):
		if key == "auto":
			key = str(self._autokey)
			self._autokey +=1

		self._entries[str(key)] = MenuEntry(option, handler)

	def items(self):
		return self._entries.items()

	def __contains__(self, choice):
		return str(choice) in self._entries

	def __getitem__(self, choice):
		return self._entries[choice]

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