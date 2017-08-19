from src.game import Game
import time
from utils import write_data
import settings

class Referee(object):
    """
    Implements the referee class. The referee takes the set of players
    for the game. He has the role of starting the game and declaring
    the winner after every game ends.
    """
    def __init__(self, players):
        self.players = players

    def start_play_offs(self, players):
        """
        Takes the initial list of players. Fixes a tournament between
        players of 2 in group.
        """
        report_data = []
        winners = []
        for index in range(0, len(players), 2):
            game = Game(index, players[index], players[index+1], settings.WINNING_GAME_POINTS, settings.START_RANGE, settings.END_RANGE)
            game.start_game()
            winner = game.get_winner()
            winners.append(winner)
            report_data.append({"players": [players[index].name, players[index+1].name], "winner": winner.name, "datetime": str(time.time())})
        
        return winners, report_data

    def start_tournament(self):
        """
        Coducts the playoffs between the players. Every winner moves up
        in the tournament till there is a single winner left in the chain.
        """
        _winners = self.players
        persist_data = {}

        data = []
        while len(_winners) != 1:
            _winners, report_data = self.start_play_offs(_winners)
            data.append(report_data)
            for item in _winners:
                # set the score and defence array of the winner to 0 for the next game.
                item.re_initialize()
        persist_data["results"] = data
        for index, item in enumerate(persist_data["results"]):
            for ind, result in enumerate(item):
                result["game"] = str(index) + "_" + str(ind)
        write_data(persist_data)
        return persist_data
