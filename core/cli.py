from random import choice
from os import system, get_terminal_size

class CLI:

    def __init__(self):
        self.game_info = None


    def get_player_name(self, player_id):
        self.update_screen()
        player_input = input(f'{player_id}, enter your name: \n')

        if not player_input:
            return player_id
        else:
            return player_input.split()[0].title()


    def get_player_mark(self, player_name):
        self.update_screen()
        player_input = input(f'{player_name}, X or O?: \n').upper()

        # Default selection
        if not player_input:
            return choice(['X', 'O'])
        
        while(True):
            if player_input not in ['X', 'O']:
                self.update_screen()
                player_input = input('Not valid, try again:  X or O?: \n').upper()
            else:
                return player_input


    def get_player_move(self, player, board):
        input_message = 'Enter your position: '
                
        while(True):
            self.update_screen()
            self.print_board(board.grid)

            player_input = input(input_message)

            if self.has_quited(player_input):
                return None
            
            try:
                player_input = int(player_input)
                if player_input in board.get_valid_moves():
                    break
                else:
                    input_message = 'Invalid, enter your position: '
            
            except Exception as e:
                input_message = 'Not a number, enter your position: '
        
        return player_input, player.mark


    def update_game_info(self, game_info):
        self.game_info = game_info


    def update_screen(self):
        system('clear')
        self.print_heading()
        

    def has_quited(self, player_input):
        if isinstance(player_input, str):
            if player_input.upper() == 'Q':
                return True
        return False


    def print_round_result(self, board):
        self.update_screen()
        self.print_board(board)
        return self.has_quited(input('Press Q to exit or enter to play again: '))


    def print_board(self, board):
        print()
        for i in range(1, 10, 3):
            print(f' {board[i-1]} | {board[i]} | {board[i+1]}      {i},{i+1},{i+2}')
            if i < 6:
                print(f'-----------')
        print()


    def print_heading(self):
        for key, value in self.game_info.items():
            self.print_centered(value)
            if key == 'scores':
                print('')
        print('\n' * 3)


    def print_centered(self, text):
        text_len = len(text)
        term_width = get_terminal_size()[0]
        spcs = int((term_width - text_len) / 2)
        print(f'{' ' * spcs}{text}')
