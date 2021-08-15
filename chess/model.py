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
        self.id = 0
        self.categories = [
            "nom",
            "lieu",
            "date_de_debut",
            "date_de_fin",
            "nombre_de_tours",
            "control_du_temps",
            "note",
        ]


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
        self.categories = [
            "nom",
            "prenom",
            "date_de_naissance",
            "sexe",
            "nombre_de_points",
            "classement",
            "id",
        ]
        Players.id += 1


class Rounds:
    def __init__(self):
        self.starting_round = str()
        self.finishing_round = str()
        self.ranked_list_of_players = []
        self.list_of_played_matchs = []
        self.list_of_matchs_of_this_round = []
        self.players_to_reintegrate = []
        self.players_to_match = []
        self.matchs_of_this_round_db = []


class Color:
    def random(self):
        if random() < 0.5:
            color = "blancs"
        else:
            color = "noirs"
        return color
