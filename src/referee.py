from src.game import Game


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
        winners = []
        for index in range(0, len(players), 2):
            game = Game(index, players[index], players[index+1], settings.WINNING_GAME_POINTS, settings.START_RANGE, settings.END_RANGE)
            game.start_game()
            winner = game.get_winner()
            winners.append(winner)
        return winners

    def start_tournament(self):
        """
        Coducts the playoffs between the players. Every winner moves up
        in the tournament till there is a single winner left in the chain.
        """
        _winners = self.players
        while len(_winners) != 1:
            _winners = self.start_play_offs(_winners)
            for item in _winners:
                # set the score and defence array of the winner to 0 for the next game.
                item.re_initialize()
        return _winners
