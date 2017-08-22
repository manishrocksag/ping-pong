import settings


class Game(object):
    def __init__(self, _id, player1, player2, total_points, start_range, end_range):
        self._id = _id
        self.player1 = player1
        self.player2 = player2
        self.total_points = total_points
        self.start_range = start_range
        self.end_range = end_range
        self.winner = None
        self.loser = None

    def start_game(self):
        self.player1.current_role = settings.OFFENSIVE
        self.player2.current_role = settings.DEFENSIVE
        print "Match between: ", self.player1.name, " ", self.player2.name
        while self.player1.score != self.total_points and self.player2.score != self.total_points:
            print "score", self.player1.score,self.player2.score
            if self.player1.current_role == settings.OFFENSIVE:
                self.perform_a_step(self.player1, self.player2)
            else:
                self.perform_a_step(self.player2, self.player1)

        if self.player1.score == self.total_points:
            self.winner = self.player1
            self.loser = self.player2

        elif self.player2.score == self.total_points:
            self.winner = self.player2
            self.loser = self.player1

        print  self.player1.name, "scored: ", self.player1.score, self.player2.name, "scored: ", self.player2.score,
        print "Winner of the match is: ", self.winner.name, " with score of: ", self.winner.score
        return self.winner, self.loser, self.winner.score, self.loser.score

    def get_winner(self):
        return self.winner

    def perform_a_step(self, player1, player2):
        picked_number = self.player1.pick_a_number(self.start_range, self.end_range)
        player2.create_defence_array(self.start_range, self.end_range)
        if picked_number not in self.player2.defence_array:
            player1.score += 1
        else:
            player2.score += 1
            self.switch_roles(player1, player2)

    def switch_roles(self, player1, player2):
        player1.current_role = settings.DEFENSIVE
        player2.current_role = settings.OFFENSIVE
