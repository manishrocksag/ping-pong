"""
    cherrypy server to manage all the apis and web sockets connections.
    It exposes the end point to all the apis.
"""

from src.web_command_handler import WebApiHandler
from src.operations import start, get_players_info
from utils import create_response, load_data, load_report_data
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

    def api_starttournament(self, args):
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
