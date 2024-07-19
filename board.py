class Board:

    def __init__(self):
        self.grid = [' ' for _ in range(9)]

    def show(self):
        print()
        for i in range(0, 9, 3):
            print(f' {self.grid[i]} | {self.grid[i+1]} | {self.grid[i+2]}      {i},{i+1},{i+2}')
            if i < 6:
                print(f'-----------')


    def update_cell(self, player, loc):

        if self.grid[loc] != ' ':
            print('Opcion no valida')
        else:
            self.grid[loc] = player.mark

