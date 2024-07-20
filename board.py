from player import Player


class Board:
    def __init__(self):
        self.reset()
        self.winner_mark = None

    def show(self):
        print()
        for i in range(1, 10, 3):
            print(f' {self.grid[i-1]} | {self.grid[i]} | {self.grid[i+1]}      {i},{i+1},{i+2}')
            if i < 6:
                print(f'-----------')
        print()
    
    def get_valid_moves(self) -> list[int]:
        valid_moves: list[int] = []
        for i in range(len(self.grid)):
            if self.grid[i] == ' ':
                valid_moves.append(i+1)
        return valid_moves


    def update_cell(self, loc: str, player: Player):
        idx = loc - 1
        self.grid[idx] = player.mark

    def check_winner(self) -> bool:
        win_combos: list[list[int]] = [
            [0,1,2],
            [3,4,5],
            [6,7,8],

            [0,3,6],
            [1,4,7],
            [2,5,8],

            [0,4,8],
            [2,4,6],
        ]
        for combo in win_combos:
            if self.grid[combo[0]] == self.grid[combo[1]] == self.grid[combo[2]] != ' ':
                self.winner_mark = self.grid[combo[0]]
                return True
        return False

    def check_tie(self):
        pass

    def reset(self):
        self.grid = [' ' for _ in range(9)]