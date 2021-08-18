from database import table_players
from database import table_tournament


def check_input(info, key):
    """Verify that user input is corresponding"""

    # not empty
    if key == "":
        while info == "":
            info = input("\nVeuillez entrez une saisie valide svp: ")
        return info
    # sex
    elif key == "H":
        while info.upper() != "H" and info.upper() != "F":
            info = input("\nVeillez entrer 'H' ou 'F' svp: ")
        return info
    # time control
    elif key == "T":
        while info.upper() != "BT" and info.upper() != "BZ" and info.upper() != "CR":
            info = input("\nVeillez entrer 'BT', 'BZ' ou 'CR' svp: ")
        return info
    # result of a match
    elif key == "results":
        while info.upper() != "V" and info.upper() != "N" and info.upper() != "D":
            info = input("\nVeillez entrer 'V', 'N' ou 'D' svp: ")
        return info

    # ranking
    elif key == "ranking":
        if info.upper() == "C":
            return info.upper
        else:
            info = ""
            return info
    # tournament number
    elif key == "tournament":
        while not info.isdigit():
            info = input("\nVeuillez entrez un nombre svp: ")
        else:
            while int(info) > len(table_tournament):
                info = input(
                    f"\nVeuillez entrez un nombre compris entre 1 et {len(table_tournament)} svp: "
                )
            else:
                return int(info)
    # number of rounds (by default 4)
    elif key == "rounds":
        if info.isdigit():
            return int(info)
        else:
            return 4
    else:
        while not info.isdigit():
            info = input("\nVeuillez entrer un chiffre svp: ")
            # points
        if key == "float":
            return float(info)
            # number
        elif key == "int":
            return int(info)
        # number of imported players
        elif key == "players":
            while int(info) not in range(0, len(table_players)+1):
                info = input(
                    f"veuillez entrez un nombre compris entre 0 et {len(table_players)} svp: "
                )
            return int(info)
