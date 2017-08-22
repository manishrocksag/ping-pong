from random import randint
import settings


class Player(object):
    def __init__(self, _id, name, len_defence_array):
        self._id = _id
        self.name = name
        self.is_active = True
        self.len_defence_array = len_defence_array
        self.defence_array = [0 for _ in range(self.len_defence_array)]
        self.score = 0
        self.current_role = None
        self.is_playing = False
        self.is_winner = False

    def shut_down(self):
        """
        Shut down the player and set its is_active flag to False.
        """
        self.is_active = False
        self.score = 0
        self.current_role = None

    def re_initialize(self):
        """
        After every game set the score and defence array of the player to 0.
        """
        self.defence_array = [0 for _ in range(self.len_defence_array)]
        self.score = 0
        self.is_playing = False
        self.is_winner = False

    def pick_a_number(self, start_range, end_range):
        return randint(start_range, end_range)

    def create_defence_array(self, start_range, end_range):
        for i in range(self.len_defence_array):
            self.defence_array[i] = randint(start_range, end_range)

    def get_current_role(self):
        return self.current_role

    def is_offensive(self):
        return self.current_role == settings.OFFENSIVE

    def __str__(self):
        return str({"id": self._id, "name": self.name})
