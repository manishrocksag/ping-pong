"""
    cherrypy server to manage all the apis and web sockets connections.
    It exposes the end point to all the apis.
"""

from src.web_command_handler import WebApiHandler
from src.operations import start, get_players_info, load_players
from utils import create_response, load_data, load_report_data, error, write_data
from src.referee import Referee
from src.game import Game
import random
import settings


class App(WebApiHandler):
    """
    Handles all the /api/ path requests
    """

    def __init__(self, listening_port, listening_ip):
        """
        Initialize the application and bind it to IP address and port number.
        """
        super(App, self).__init__(listening_ip, listening_port, 'index.html')
        self.players = []
        self.referee = None
        self.winners = []
        self.current_winner = None
        self.players_info = {}
        index = 0

    def api_registerplayers(self, args):
        if not self.players:
            self.players = load_players()
            output = []

            for player in self.players:
                self.players_info[player.name] = player.name
                output.append({"name": player.name})
            return output
        else:
            return error(1001, "players already registered.")

    def api_registerreferee(self, args):
        if not self.referee:
            self.referee = Referee(self.players)
            return "referee successfully registered."
        else:
            return error(1001, "referee already registered.")

    def api_addplayer(self, args):
        no = int(args["no"])
        name = args["name"]
        defence_set_length = int(args["defence_set_length"])
        data = load_data()
        data.append({"no": no, "name": name, "defence_set_length": defence_set_length})
        write_data(data)

    def api_createnewtournament(self, args):
        self.players = None
        self.players_info = None
        self.winners = None

        return settings.SUCCESS

    def api_shuffleplayers(self, args):
        self.players = random.shuffle(self.players)
        return settings.SUCCESS

    def api_startmatch(self, args):
        player1 = args["player1"]
        player2 = args["player2"]

        if player1 not in self.players_info or player2 not in self.players_info:
            return error("player with the given name does not exists.")

        if self.players_info[player1].is_playing:
            return error(1002, player1 + " has already played his game.")

        if self.players_info[player2].is_playing:
            return error(1002, player2 + " has already played his game.")

        self.players_info[player2].is_playing = True
        self.players_info[player2].is_playing = True

        game = Game(self.index, self.players_info[player1], self.players_info[player2], settings.WINNING_GAME_POINTS, settings.START_RANGE,
                    settings.END_RANGE)
        game.start_game()
        winner = game.get_winner()
        winner.is_winner = True
        winner.re_initialize()
        self.winners.append(winner)

        return {"winner": winner.name}

    def api_makeamove(self, args):
        pass

    def api_winnerslist(self, args):
        winners_list = []
        for item in self.winners:
            winners_list.append(item.name)
        return winners_list

    def api_currentwinner(self, args):
       return self.winners[-1].name

    def api_startwholetournament(self, args):
         output = start()
         return output

    def api_getplayers(self, args):
        if "id" in args:
            _id = int(args["id"])
        else:
            _id = None
        return get_players_info(_id)

    def api_report(self, args):
        return load_report_data()


def main():
        app = App(10007, '0.0.0.0')
        app.start()


if __name__ == '__main__':
    main()
