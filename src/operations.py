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


def get_players_info(id=None):
    player_info = []
    players = load_players()
    if not id:
        for item in players:
            player_info.append(str(item))
    else:
        for item in players:
            if item._id == id:
                player_info.append(str(item))
    return player_info


def start():
    """
    Creates a list of players objects. Creates a referee object.
    The referee initiates the tournament.
    """
    players = load_players()
    referee = Referee(players)
    return referee.start_tournament()
