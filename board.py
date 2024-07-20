from player import Player


class Board:
    def __init__(self):
        self.grid = [' ' for _ in range(9)]

    def show(self):
        print()
        for i in range(1, 10, 3):
            print(f' {self.grid[i-1]} | {self.grid[i]} | {self.grid[i+1]}      {i},{i+1},{i+2}')
            if i < 6:
                print(f'-----------')
        print()

    def update_cell(self, loc: str, player: Player):
        idx = loc - 1
        self.grid[idx] = player.mark
