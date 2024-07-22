from core.player import Player


class Board:

    def __init__(self):
        self.new()
        self.winner_mark = None


    def new(self):
        self.grid = [' ' for _ in range(9)]
    

    def get_valid_moves(self):
        return [i + 1 for i in range(len(self.grid)) if self.grid[i] == ' ']
    

    def update_cell(self, idx, mark):
        self.grid[idx] = mark


    def check_win(self):
        win_combinatios = [
            [0,1,2], [3,4,5],
            [6,7,8], [0,3,6],
            [1,4,7], [2,5,8],
            [0,4,8], [2,4,6],
        ]
        for comb in win_combinatios:
            if self.grid[comb[0]] == self.grid[comb[1]] == self.grid[comb[2]] != ' ':
                return self.grid[comb[0]]
        return None


    def check_tie(self):
        return ' ' not in self.grid