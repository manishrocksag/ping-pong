from src.player import Player
from src.referee import Referee
from utils import load_data
import settings
import json

def load_players():
    """
    Takes a data file with the set of attributes for the players from
    the data.json file and creates a list of player objects.
    """
    players = []
    data = load_data()

    for item in data:
        players.append(Player(item["no"], item["name"], item["defence_set_length"]))
    return players

def start():
    """
    Creates a list of players objects. Creates a referee object.
    The referee initiates the tournament.
    """
    players = load_players()
    referee = Referee(players)
    referee.start_tournament()
