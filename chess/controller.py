import datetime
from tinydb import Query
from database import Tinydb
from model import Tournament
from model import Players
from model import Color
from model import Rounds
from utils import table_players
from utils import table_tournament
from view import HomeMenuView
from view import NewGameView
from view import PlayersView
from view import MatchView
from view import RankingView
from view import RapportsView
from view import ResultsView


class HomeMenuController:
    """Print the home menu et get the user response"""

    def __init__(self):
        home_menu_view = HomeMenuView()
        while home_menu_view:
            choice = home_menu_view.display_menu()
            if choice == 1:
                new_game = NewGameController()
                new_game()
            elif choice == 2:
                resume_game = ResumeGameController()
                resume_game()
            elif choice == 3:
                rapports = RapportsController()
                rapports()
            elif choice == 4:
                print("\nAu revoir")
                home_menu_view = False
            else:
                print("Veuillez entrez un chiffre entre 1 et 4 svp.")


tournament = Tournament()
query = Query()
tiny = Tinydb()


class NewGameController:
    """get the tournament informations"""

    def __init__(self):
        tournament.starting_date = datetime.datetime.now().strftime("%d/%m/%Y")

    def __call__(self):
        # enter the tournament informations
        new_game_view = NewGameView()
        value = new_game_view.get_user_info(tournament)
        tiny.serialize(table_tournament, value)
        # update the tournament id
        new_id = len(table_tournament)
        tiny.update(table_tournament, {"id": new_id}, query.id == 0)
        if tournament.nb_days > 1:
            tournament.ending_date = (
                datetime.datetime.now() + datetime.timedelta(days=tournament.nb_days)
            ).strftime("%d/%m/%Y")
            tournament.date = (
                f"du {tournament.starting_date} au {tournament.ending_date}"
            )
        else:
            tournament.date = tournament.starting_date
            tournament.ending_date = tournament.starting_date
        tiny.update(
            table_tournament,
            {"date_de_fin": tournament.ending_date},
            query.id == len(table_tournament),
        )
        print(
            "\n",
            tournament.name,
            tournament.location,
            tournament.date,
            tournament.time_control,
            "\n",
        )
        players = PlayersController()
        players()


round = Rounds()


class PlayersController:
    """enter the players informations"""

    def __call__(self):
        model_player = Players()
        view_player = PlayersView()
        model_player.list_of_players.clear()

        """Asking the user if he wants to import players if the database is not empty"""
        # how many players he wants to imports
        if table_players:
            nb_imported_players = view_player.nb_import_players(
                table_players, model_player
            )
            # wich player he wants to import
            for i in range(nb_imported_players):
                imported_player_id = view_player.wich_player_to_import()
                model_player.list_of_players.append(
                    table_players.get(doc_id=imported_player_id)
                )

        # user adding players
        model_player.nb_players = view_player.nb_players()
        players = [Players() for _ in range(model_player.nb_players)]
        for player, i in zip(players, range(1, 9)):
            ids = len(table_players) + i
            model_player.list_of_players.append(
                view_player.enter_new_player(player, ids)
            )
        # saving new players in the database
        for player in model_player.list_of_players:
            if player not in table_players:
                tiny.serialize(table_players, player)
        # updating already existing players
        tiny.update(
            table_tournament,
            {"joueurs": tuple(model_player.list_of_players)},
            query.id == len(table_tournament),
        )
        self.let_it_go(model_player.list_of_players, range(tournament.nb_rounds))

    def let_it_go(self, list_of_players, nb_rounds):
        """starting the rounds of the tournament"""

        ranking_update = RankingUpdateController()
        ranking_controller = RankingController()
        ranking_view = RankingView()
        for i in nb_rounds:
            round.starting_round = datetime.datetime.now().strftime("%d/%m/%Y à %H:%M")
            tiny.update(
                table_tournament,
                {f"debut_du_round_{i+1}": round.starting_round},
                query.id == len(table_tournament),
            )
            print(f"le round {i+1} à débuté le {round.starting_round} \n")
            # sort players in two lists
            ranking_controller.rank_this_list(list_of_players, i)
            # adding points to each player
            ranking_controller.enter_results()
            tiny.update(
                table_tournament,
                {f"matchs_du_round_{i + 1}": round.matchs_of_this_round_db},
                query.id == len(table_tournament),
            )
            round.matchs_of_this_round_db.clear()
            round.finishing_round = datetime.datetime.now().strftime("%d/%m/%Y à %H:%M")
            tiny.update(
                table_tournament,
                {f"fin_du_round_{i+1}": round.finishing_round},
                query.id == len(table_tournament),
            )
            round.list_of_matchs_of_this_round.insert(0, round.starting_round)
            round.list_of_matchs_of_this_round.append(round.finishing_round)
            tournament.rounds_list.append(
                (f"Round{i+1}", round.list_of_matchs_of_this_round)
            )
            round.list_of_matchs_of_this_round.clear()
            print(
                f"le round {i+1} s'est terminé le {round.finishing_round}\n\n			**********\n"
            )
            modify_ranking = ranking_view.modifying_ranking()
            if modify_ranking:
                ranking_update.rank_players(round.ranked_list_of_players)
        print("Fin du tournoi.")


class RankingController:
    def play_it(self, p1, p2, lenth_ranked_list_of_players):
        """verify that the number of matchs is not already complete before playing another one"""
        match_view = MatchView()
        color = Color()
        if len(round.list_of_matchs_of_this_round) != lenth_ranked_list_of_players:
            match_view.display_match(
                color.random(),
                (p1["id"], p1["nom"], p1["prenom"]),
                (p2["id"], p2["nom"], p2["prenom"]),
            )
            match = p1["id"], p2["id"]
            round.list_of_matchs_of_this_round.append(match)

    def is_match_already_played(self, p1, p2, lenth_ranked_list_of_players):
        """verify that a match hasn't been played before,
        then play it, otherwise split the two players
        and add them to a waiting to another player list"""
        if (p1["id"], p2["id"]) in round.list_of_played_matchs or (
            p2["id"],
            p1["id"],
        ) in round.list_of_played_matchs:
            round.players_to_reintegrate.append(p1)
            round.players_to_reintegrate.append(p2)
        else:
            self.play_it(p1, p2, lenth_ranked_list_of_players)

    def rank_this_list(self, list_of_players, i):
        """sort the players by points and if they're equal by ranking,
        then split them into two separated lists, and match them by two"""
        list_of_players = sorted(list_of_players, key=lambda i: i["classement"])
        round.ranked_list_of_players = sorted(
            list_of_players, key=lambda i: i["nombre_de_points"], reverse=True
        )
        lenth_ranked_list_of_players = len(round.ranked_list_of_players) // 2
        # for the 1st round
        if i == 0:
            for p1, p2 in zip(
                round.ranked_list_of_players[:lenth_ranked_list_of_players],
                round.ranked_list_of_players[lenth_ranked_list_of_players:],
            ):
                self.play_it(p1, p2, lenth_ranked_list_of_players)
        # for the others rounds
        else:
            while (
                len(round.list_of_matchs_of_this_round) != lenth_ranked_list_of_players
            ):
                for p1, p2 in zip(list_of_players[::2], list_of_players[1::2]):
                    # verify if there's any player in the waiting to another player list to form a match
                    if round.players_to_reintegrate:
                        p3 = round.players_to_reintegrate.pop()
                        p4 = round.players_to_reintegrate.pop()
                        self.is_match_already_played(
                            p1, p3, lenth_ranked_list_of_players
                        )
                        self.is_match_already_played(
                            p2, p4, lenth_ranked_list_of_players
                        )
                    else:
                        self.is_match_already_played(
                            p1, p2, lenth_ranked_list_of_players
                        )

    def enter_results(self):
        """saving the points earned by each player during the last match"""
        results = ResultsView()
        for player in round.ranked_list_of_players:
            result = results.enter_results(player)
            # saving new points
            if result == "V":
                player["nombre_de_points"] += 1.0
            elif result == "N":
                player["nombre_de_points"] += 0.5
            else:
                player["nombre_de_points"] += 0.0
            # updating database with the new points
            nb_points = player["nombre_de_points"]
            tiny.update(
                table_players, {"nombre_de_points": nb_points}, query.id == player["id"]
            )
        for match in round.list_of_matchs_of_this_round:
            round.list_of_played_matchs.append(match)
            round.matchs_of_this_round_db.append(
                [
                    (match[0], player["nombre_de_points"]),
                    (match[1], player["nombre_de_points"]),
                ]
            )


class ResumeGameController:
    def __call__(self):
        player = PlayersController()
        rapport_view = RapportsView()
        num_tournament = rapport_view.tournament_number()
        round = rapport_view.round_number()
        nb_rounds = range(round - 1, tournament.nb_rounds)
        list_of_players = sorted(
            table_tournament.get(doc_id=num_tournament)["joueurs"],
            key=lambda i: i["classement"],
        )
        player.let_it_go(list_of_players, nb_rounds)


class RapportsController:
    """printing rapports to the user"""

    def __call__(self):
        rapport = RapportsView()
        choice = rapport.choice()
        rapport_view = RapportsView()

        while rapport:
            # alphabeticall sorting of all the actors
            if choice == 1:
                print("Liste des acteurs par ordre alphabétique:\n")
                dict = sorted(table_players, key=lambda i: i["nom"])
                for player in range(len(table_players)):
                    print("Joueur n°{id}    nom: {nom}  prénom: {prenom}    date de naissance: {date_de_naissance}"
                          "  sexe: {sexe}    nombre de points: {nombre_de_points}    classement: {classement}\n\n".format_map(dict[player]))
            # rank sorting of all the actors
            elif choice == 2:
                print("Liste des acteurs par classement:\n")
                dict = sorted(table_players, key=lambda i: i["classement"])
                for player in range(len(table_players)):
                    print("Joueur n°{id}    nom: {nom}  prénom: {prenom}    date de naissance: {date_de_naissance}"
                          "  sexe: {sexe}    nombre de points: {nombre_de_points}    classement: {classement}\n\n".format_map(dict[player]))
            # alphabeticall sorting of players of a tournament
            elif choice == 3:
                num_tournament = rapport_view.tournament_number()
                print(
                    f"Liste des joueurs du tournoi n°{num_tournament} par ordre alphabétique:\n"
                )
                dict = sorted(
                        table_tournament.get(doc_id=num_tournament)["joueurs"],
                        key=lambda i: i["nom"],
                    )
                for player in range(8):
                    print("Joueur n°{id}    nom: {nom}  prénom: {prenom}    date de naissance: {date_de_naissance}"
                          "  sexe: {sexe}    nombre de points: {nombre_de_points}    classement: {classement}\n\n".format_map(
                        dict[player]))

            # rank sorting of players of a tournament
            elif choice == 4:
                num_tournament = rapport_view.tournament_number()
                print(
                    f"Liste des joueurs du tournoi n°{num_tournament} par classement:\n"
                )
                dict = sorted(
                        table_tournament.get(doc_id=num_tournament)["joueurs"],
                        key=lambda i: i["classement"],
                    )

                for player in range(8):
                    print("Joueur n°{id}    nom: {nom}  prénom: {prenom}    date de naissance: {date_de_naissance}"
                          "  sexe: {sexe}    nombre de points: {nombre_de_points}    classement: {classement}\n\n".format_map(
                        dict[player]))
            # tournaments list
            elif choice == 5:
                print("Liste des tournois:\n")
                for row in range(1, len(table_tournament) + 1):
                    print(f"Tournoi n°{row}\n")
                    for category in tournament.categories:
                        print(
                            category, ": ", table_tournament.get(doc_id=row)[category]
                        )
                    for player in table_tournament.get(doc_id=row)["joueurs"]:
                        print(
                            "joueurs : ", player["id"], player["nom"], player["prenom"]
                        )
                    print("\n")
            # rounds of a tournament list
            elif choice == 6:
                num_tournament = rapport_view.tournament_number()
                print(f"Liste des tours du tournoi n°{num_tournament}:\n")
                dict = sorted(table_players, key=lambda i: i["id"])
                for y in range(1, 5):
                    print(
                        f"Round {y}:",
                        table_tournament.get(doc_id=num_tournament)[
                            f"debut_du_round_{y}"
                        ])
                    for i in range(4):
                        print("Joueur n°{id}    {nom}   {prenom}    {nombre_de_points}pts".format_map(
                            dict[table_tournament.get(doc_id=num_tournament)[f"matchs_du_round_{y}"][i][0][
                                     0] - 1]) + " vs " + "Joueur n°{id}    {nom}   {prenom}    {nombre_de_points}pts\n".format_map(
                            dict[table_tournament.get(doc_id=num_tournament)[f"matchs_du_round_{y}"][i][1][
                                     0] - 1]))  # match, joueur, id
                    print(table_tournament.get(doc_id=num_tournament)[
                            f"fin_du_round_{y}"
                        ])
            # matchs of a tournament list
            elif choice == 7:
                num_tournament = rapport_view.tournament_number()
                print(f"Liste des matchs du tournoi n°{num_tournament}:\n")
                dict = sorted(table_players, key=lambda i: i["id"])
                for y in range(1,5):
                    print(f"Matchs du round n°{y}\n\n")
                    for i in range(4):
                        print("Joueur n°{id}    {nom}   {prenom}    {nombre_de_points}pts".format_map(
                                dict[table_tournament.get(doc_id=num_tournament)[f"matchs_du_round_{y}"][i][0][0]-1]) + " vs " + "Joueur n°{id}    {nom}   {prenom}    {nombre_de_points}pts\n".format_map(
                                dict[table_tournament.get(doc_id=num_tournament)[f"matchs_du_round_{y}"][i][1][0]-1])) # match, joueur, id

            # return to the home menu
            else:
                break
            choice = rapport.choice()


class RankingUpdateController:
    """modifying the ranking of players"""

    def rank_players(self, list):
        rapport_view = RapportsView()
        i = 0
        for player in list:
            ranking = rapport_view.new_ranking(player)
            list.pop(0)
            player[5] = ranking
            list.insert(0, player)
            tiny.update(
                table_players, {"classement": ranking}, query.id == player["id"]
            )
            i += 1
