from models import *

from random import choice

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []


    def new_round(self):
        pass


    def switch_player(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    
    def choose_starter(self):
        self.current_player = choice(self.players)

