from random import choice
import os


class Player:
    def __init__(self, name: str, mark: str):
        self.name = name
        self.mark = mark


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




class Game:
    def __init__(self):
        pass


def print_header(*args):
    clear_screen()
    print_centered('Tic Tac Toe')
    if len(args) == 1:
        print_centered(args[0])
    print('\n')


def clear_screen():
    os.system('clear')


def print_centered(string):
    terminal_width = os.get_terminal_size()[0]
    string_length = len(string)
    empty_space_required = int((terminal_width - string_length)/2)
    empty_space = " " * empty_space_required
    
    #Add empoty space in front of string
    print(empty_space + string)


def get_player_choice(player):

    player_input = input(f'{player.name}, (1-9): ')
    if player_input not in range(1,10):
        player_input = input()


# create players
print_header()
p1 = Player('p1')
p2 = Player('p2')

# set markers
print_header(f'{p1.name} vs {p2.name}')
p2.mark = 'O' if p1.get_mark() == 'X' else 'X'


# create and show board
print_header(f'{p1.name} vs {p2.name}')
board = Board()
board.show()

# pick starter
current_player = choice([p1, p2])

get_player_choice(current_player, board)