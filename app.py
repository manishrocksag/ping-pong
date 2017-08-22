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
        self.current_players_list = {}
        index = 0

    def api_registerplayers(self, args):
        """
        Register all the new players from the data file.
        """
        if not self.players:
            self.players = load_players()
            output = []

            for player in self.players:
                self.players_info[player.name] = player
                self.current_players_list[player.name] = player
                output.append({"name": player.name})
            return create_response(output)
        else:
            return error(1001, "players already registered.")

    def api_registerreferee(self, args):
        """
        Create a new instance of the referee who conducts new tournaments.
        """
        if not self.referee:
            self.referee = Referee(self.players)
            return create_response("referee successfully registered.")
        else:
            return error(1001, "referee already registered.")

    def api_addplayer(self, args):
        """
        Add a new player to the data file.
        """
        no = int(args["no"])
        name = args["name"]
        defence_set_length = int(args["defence_set_length"])
        data = load_data()
        data.append({"no": no, "name": name, "defence_set_length": defence_set_length})
        write_data(data)
        return create_response(settings.SUCCESS)

    def api_createnewtournament(self, args):
        """
        Initialize a new tournament.
        """
        self.players = []
        self.players_info = {}
        self.winners = []

        return create_response(settings.SUCCESS)

    def api_shuffleplayers(self, args):
        """
        Randomly shuffle a array of players.
        """
        self.players = random.shuffle(self.players)
        return create_response(settings.SUCCESS)

    def api_startmatch(self, args):
        """
        Starts a match between the two players and returns the
        winner and loser of the match. It also returns the
        winner and loser scores for the match.
        """
        if not self.referee:
            return error(10001, "referee is not registered yet.")

        player1 = args["player1"]
        player2 = args["player2"]

        if player1 not in self.players_info or player2 not in self.players_info:
            return error(1001, "player with the given name does not exists.")

        if self.players_info[player1].is_playing:
            return error(1002, player1 + " has already played his game.")

        if self.players_info[player2].is_playing:
            return error(1002, player2 + " has already played his game.")

        self.players_info[player1].is_playing = True
        self.players_info[player2].is_playing = True

        game = Game(self.index, self.players_info[player1], self.players_info[player2], settings.WINNING_GAME_POINTS, settings.START_RANGE,
                    settings.END_RANGE)
        _winner, _loser, _winner_score, _loser_score = game.start_game()
        winner = game.get_winner()
        winner.is_winner = True
        winner.re_initialize()
        self.winners.append(winner)
        self.current_players_list.pop(_loser.name, None)
        self.current_players_list.pop(_winner.name, None)
        return create_response({"winner": winner.name, "loser": _loser.name, "winner_score": _winner_score, "loser_score": _loser_score})

    def api_makeamove(self, args):
        pass

    def api_getremainingplayers(self, args):
        """
        Gets the list of players who have not played a single match.
        """
        output = []
        for item in self.current_players_list:
            output.append(item)
        return create_response(output)

    def api_winnerslist(self, args):
        """
        Get the list of all the winners for the match.
        """
        winners_list = []
        for item in self.winners:
            winners_list.append(item.name)
        return create_response(winners_list)

    def api_currentwinner(self, args):
        """
        Get the name of the most recent winner.
        """
        return create_response(self.winners[-1].name)

    def api_startwholetournament(self, args):
        """
        Starts the whole tournament between all the players and
        returns the list of the winners after the end of the
        tournament.
        """
        output = start()
        return create_response(output)

    def api_getplayers(self, args):
        """
        Get the list of the players which are registered with the
        system.
        """
        if "id" in args:
            _id = int(args["id"])
        else:
            _id = None
        return create_response(get_players_info(_id))

    def api_report(self, args):
        """
        Generates the reports of all the games held in past.
        """
        return create_response(load_report_data())


def main():
        app = App(10007, '0.0.0.0')
        app.start()


if __name__ == '__main__':
    main()
