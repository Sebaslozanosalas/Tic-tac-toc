from core.board import Board
from core.player import Player
from core.cli import CLI

from random import choice
import os

class Game:

    def __init__(self):
        self.cli = CLI()
        self.board = Board()
        self.players = None
        self.current_player = None 
        self.keep_playing = True
        self.running = True
        self.game_info = {
            'title': 'Tic Tac Toe',
            'vs_heading': '',
            'scores': '',
            'game_status': ''
        }


    def setup(self):
        self.cli.update_game_info(self.game_info)
        self.get_players_data()
        
        # Set Versus Heading
        self.game_info['vs_heading'] = (
            f'{self.players[0].name} ({self.players[0].mark})'
            '    VS    '
            f'{self.players[1].name} ({self.players[1].mark})'
        )


    def play(self):
        self.setup()

        # Main game loop
        while(self.keep_playing):

            # Round loop
            self.new_round()
            while(self.running):
                # Get player move
                self.cli.update_game_info(self.game_info)
                self.current_player_move()
                
                # Check for round end
                if not self.round_ended():
                    self.switch_player()
        
        self.quit()


    def quit(self):
        # Set game result
        if self.players[0].win_count > self.players[1].win_count:
            game_result = f'{self.players[0].name} Wins!'
        elif self.players[0].win_count < self.players[1].win_count:
            game_result = f'{self.players[1].name} Wins!'
        else:
            game_result = 'It\'s a tie!'
        self.game_info['game_status'] = game_result

        self.cli.update_screen()
        self.cli.print_centered('Thank you for playing')
        print('\n' * 3) 


    def round_ended(self) -> bool:        
        round_ended = False

        # Check for winner
        winner_mark = self.board.check_win()
        if winner_mark:
            round_ended = True
            winner = self.players[0] if self.players[0].mark == winner_mark else self.players[1]
            winner.win_count += 1
            self.game_info['game_status'] = f'{winner.name} wins!'
        
        # Check for tie
        if self.board.check_tie():
            round_ended = True
            self.game_info['game_status'] = f'It\'s a tie!'
        
        if round_ended:
            self.running = False
            if self.cli.print_round_result(self.board.grid): # True if user quited
                self.keep_playing = False

        return round_ended


    def new_round(self):
        self.running = True
        self.board.new()

        # Choose random starter
        self.current_player = choice(self.players)

        # Update game info
        self.game_info['game_status'] = f'{self.current_player} starts'
        self.game_info['scores'] = f'{self.players[0].win_count} - {self.players[1].win_count}'


    def current_player_move(self):
        # Get player move
        result = self.cli.get_player_move(self.current_player, self.board)
        if not result:
            self.end_game()
            return
        position, mark = result
        # Update board
        self.board.update_cell(position - 1, mark)


    def switch_player(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
        self.game_info['game_status'] = f'Is {self.current_player} turn'


    def get_players_data(self):
        # Create Player 1
        player1_name = self.cli.get_player_name('Player 1')
        player1_mark = self.cli.get_player_mark(player1_name)
        player1 = Player('Player 1', player1_name, player1_mark)
        
        # Create Player 2
        player2_name = self.cli.get_player_name('Player 2')
        player2_mark = 'O' if player1_mark == 'X' else 'X'
        player2 = Player('Player 2', player2_name, player2_mark)
        
        self.players = [player1, player2]


    def has_quited(self, player_input):
        if self.cli.has_quited(player_input):
            self.end_game()
            return True
        return False


    def end_game(self):
        self.running = False
        self.keep_playing = False