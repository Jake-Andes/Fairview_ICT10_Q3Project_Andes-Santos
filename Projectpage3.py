from pyscript import document  # type: ignore

# Example Intrams Team Players
team_players = [
    "Akingson Jake Andes",
    "Alexander Tacan",
    "Alexi Villanueva",
    "Ashley Kirsten Y. Santos",
    "Audrey Anne Dumaguing",
    "Aurora Ishtar A. Ubana",
    "Cyrenne Mendez",
    "Danielle Aleena Noble",
    "Fil Ayala",
    "Gabrielle L. Damondamon",
    "Giovanni Escarda",
    "Jarix Zales",
    "John Alfred F. Taruc Jr.",
    "John Ligas",
    "Joseph Deray",
    "Kurt Tenorio",
    "Margaux Alaina Ferrer",
    "Marley Summer Manese",
    "Martina Cabrillos",
    "Mary Bernadette Daed",
    "Mike Jared De Jesus",
    "Nathan Mari Anthony Devera Grande",
    "Nathan Tiongson",
    "Pauline Ecraela",
    "Riso Salapunen",
    "Vic Gorom",
    "Zion Margaret Fabul"
]

def add_player(event=None):
    output = document.getElementById("playerList")

    if output.innerText == "":   # If nothing is shown yet
        names = ""
        for player in team_players:
            names += player + "\n"
        output.innerText = names
    else:   # If already shown, clear it
        output.innerText = ""   