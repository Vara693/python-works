import math
import random

class player:
    def __init__(self, letter):
        #X or O
        self.letter = letter

    def move(self, game):
        pass


class RandomCompPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def move(self, game):
        choice = random.choice(game.available_moves())
        return choice  

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def move(self, game):
        pass