from utils import check_input


class HomeMenuView:
    # dislaying the menu to the user
    def display_menu(self):
        choice = check_input(
            input(
                "\n\n1/ Nouveau tournoi"
                "\n\n2/ Charger un tournoi"
                "\n\n3/ Afficher les rapports"
                "\n\n4/ Quitter le programme"
                "\n\n>>> "
            ),
            "int",
        )
        return choice


class NewGameView:
    def get_user_info(self, tournament):
        tournament.name = check_input(input("\nNom du tournoi:\n>>> "), "")
        tournament.nb_days = check_input(
            input("\nDurée en jours du tournoi:\n>>> "), "int"
        )
        tournament.location = check_input(input("\nLieu du tournoi:\n>>> "), "")
        tournament.time_control = check_input(
            input(
                "\nContrôle du temps de jeu:\n\nEntrez 'BT' pour bullet, 'BZ' pour blitz, 'CR' pour coup rapide:\n>>> "
            ),
            "T",
        )
        tournament.note = input(
            "\nAjouter une remarque ou tapez 'Entrée' pour continuer:\n>>> "
        )
        tournament.nb_rounds = check_input(
            input(
                "Le nombre de tours est de 4, entrez un autre nombre pour le modifier ou appuyez sur 'Entrée':\n>>> "
            ),
            "rounds",
        )
        return {
            "nom": tournament.name,
            "lieu": tournament.location,
            "nombre_de_jours": tournament.nb_days,
            "date_de_debut": tournament.starting_date,
            "date_de_fin": tournament.ending_date,
            "nombre_de_tours": tournament.nb_rounds,
            "joueurs": "",
            "control_du_temps": tournament.time_control,
            "note": tournament.note,
            "debut_du_round_1": "",
            "matchs_du_round_1": [],
            "fin_du_round_1": "",
            "debut_du_round_2": "",
            "matchs_du_round_2": [],
            "fin_du_round_2": "",
            "debut_du_round_3": "",
            "matchs_du_round_3": [],
            "fin_du_round_3": "",
            "debut_du_round_4": "",
            "matchs_du_round_4": [],
            "fin_du_round_4": "",
            "id": tournament.id,
        }


class PlayersView:
    # number of players
    def nb_players(self):
        nb_players = check_input(
            input("\nCombien de joueurs voulez vous ajouter ?\n>>> "), "int"
        )
        return nb_players

    # add a new player
    def enter_new_player(self, player, id):
        player.name = check_input(input("\nEntrez le nom du joueur:\n>>> "), "")
        player.surname = check_input(input("\nSon prénom:\n>>> "), "")
        player.date_of_birth = check_input(
            input("\nSa date de naissance sous la forme JJ/MM/AAAA:\n>>> "), ""
        )
        player.sex = check_input(input("\nSon sexe 'H' ou 'F':\n>>> "), "H")
        player.points = check_input(input("\nSon nombre de points:\n>>> "), "float")
        player.ranking = check_input(input("\nSon rang:\n>>> "), "int")
        return {
            "nom": player.name,
            "prenom": player.surname,
            "date_de_naissance": player.date_of_birth,
            "sexe": player.sex,
            "nombre_de_points": player.points,
            "classement": player.ranking,
            "id": id,
        }

    # import players from the database
    def nb_import_players(self, table_players, model_player):
        for player in sorted(table_players, key=lambda i: i["id"]):
            print(player["id"], player["nom"], player["prenom"])
        nb_imported_players = check_input(
            input(
                "\n\nEntrez le nombre de joueurs à importer parmis la liste précédente."
                f"\n(Chiffre entre 0 et {len(table_players)})\n>>> "
            ),
            "players",
        )

        return nb_imported_players

    def wich_player_to_import(self):
        imported_player_id = check_input(
            input("\n\nQuel est l'id du joueur que vous souhaitez importer?\n>>> "),
            "players",
        )
        return imported_player_id


class MatchView:
    def display_match(self, color, p1, p2):

        print(f"Le joueur {p1} avec les {color} affrontera le joueur {p2}\n")


class ResultsView:
    def enter_results(self, player):
        results = check_input(
            input(
                f"\nJoueur: {player['nom'], player['prenom']}  "
                "\n\nEntrez 'V' pour victoire, 'N' pour nul, et 'D' pour défaite:\n>>> "
            ),
            "results",
        )
        return results


class RapportsView:

    # user choosing the tournament number
    def tournament_number(self):
        num_tournament = check_input(
            input(
                "\n\nVeuillez entrer le n° du tournoi (cf liste des tournois):\n>>> "
            ),
            "tournament",
        )
        return num_tournament

    # user choosing the round number
    def round_number(self):
        round = check_input(
            input("Indiquez le tour que vous souhaitez poursuivre:\n>>> "),
            "int",
        )
        return round

    # user modifying the rank of players
    def new_ranking(self, player):
        ranking = check_input(
            input("Entrez le nouveau rang du joueur n°{id}    nom: {nom}  prénom: {prenom}    date de naissance: {date_de_naissance}"
                          "  sexe: {sexe}    nombre de points: {nombre_de_points}    classement: {classement}:\n>>> ".format_map(player)), "int")
        return ranking

    # user choosing the rapport he wants to be displayed
    def choice(self):
        choice = check_input(
            input(
                "\nVous souhaitez afficher un rapport contenant:"
                "\n\n1/ Les acteurs par ordre alphabétique"
                "\n\n2/ Les acteurs par classement"
                "\n\n3/ Les joueurs d'un tournoi par ordre alphabétique"
                "\n\n4/ Les joueurs d'un tournoi par classement"
                "\n\n5/ Tous les tournois"
                "\n\n6/ Les tours d'un tournois"
                "\n\n7/ Les matchs d'un tournoi"
                "\n\n8/ Retour au menu principal"
                "\n\n>>> "
            ),
            "int",
        )
        return choice


class RankingView:
    # asking the user if he wants to modify the ranking of players
    def modifying_ranking(self):
        modify_ranking = check_input(
            input(
                "Si vous souhaitez modifier le classement tapez 'C' sinon appuyez sur la touche 'Entrée':\n>>> "
            ),
            "ranking",
        )
        return modify_ranking
