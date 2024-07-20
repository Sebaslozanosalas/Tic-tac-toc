from board import Board
from player import Player

from random import choice
import os

class Game:

    def __init__(self):
        self.board = Board()
        self.players = None
        self.current_player_idx = None
        self.heading = {
            'title': 'Tic Tac Toe',
            'players_info': '',
            'scores': '',
            'game_status': ''
        }
        self.is_running = True
        self.keep_playing = True


    def play(self) -> None:
        # Get users data
        self.players = self.get_players_data()

        self.set_heading()

        while(self.keep_playing):

            self.new_round()
            while(self.is_running):
                self.current_player_move()
                if not self.check_round_end():
                    self.switch_player()
            if self.keep_playing:
                if not self.play_again():
                    break
        
        self.quit_game()
            
    def quit_game(self):
        if self.players[0].win_count > self.players[1].win_count:
            game_result = f"{self.players[0].name} Wins!"
        elif self.players[0].win_count < self.players[1].win_count:
            game_result = f"{self.players[1].name} Wins!"
        else:
            game_result = "It's a tie!"

        self.heading['game_status'] = game_result
        self.clear_screen()
        self.print_centered("Quiting, thank you for playing")
        print("\n" * 3) 

    def play_again(self) -> bool:
        player_input: str = input("Press Q to exit or enter to play again: ")
        return not self.has_quited(player_input)


    def check_round_end(self) -> bool:

        def show_game_result(self):
            self.is_running = False
            self.clear_screen()
            self.board.show()

        # check for winner
        if self.board.check_winner():
            # get winner and add to win count
            winner = self.players[0] if self.players[0].mark == self.board.winner_mark else self.players[1]
            winner.win_count += 1

            # set message and restar round
            self.heading['game_status'] = f"{winner.name} wins!"
            show_game_result(self)
            return True
        
        if self.board.check_tie():
            # set message and restar rounds
            self.heading['game_status'] = f"It's a tie!"
            show_game_result(self)
            return True
        
        return False

    def new_round(self):
        self.is_running = True
        self.board.reset()
        self.choose_starter()
        self.heading['game_status'] = f"{self.players[self.current_player_idx]} starts"
        self.update_scores()
        
    def update_scores(self):
        self.heading['scores'] = f"{self.players[0].win_count} - {self.players[1].win_count}"

    def current_player_move(self):
        
        input_message = "Enter your position: "

        while(True):
            self.clear_screen()
            self.board.show()
            
            player_input = input(input_message)

            if self.has_quited(player_input):
                return None
            try:
                player_input = int(player_input)
                if player_input in self.board.get_valid_moves():
                    break
                else:
                    input_message = "Invalid, enter your position: "
            except Exception as e:
                input_message = "Not a number, enter your position: "
        
        self.board.update_cell(player_input, self.players[self.current_player_idx])
        

    def switch_player(self) -> None:
        self.current_player_idx = 1 if self.current_player_idx == 0 else 0
        self.heading['game_status'] = f'Is {self.players[self.current_player_idx]} turn'
          

    def clear_screen(self) -> None:
        os.system('clear')
        for key, value in self.heading.items():
            self.print_centered(value)
            if key == 'scores':
                print("")
        print("\n" * 3)


    def print_centered(self, text: str) -> None:
        term_width = os.get_terminal_size()[0]
        text_len = len(text)
        spcs = int((term_width - text_len) / 2)
        print(f"{" " * spcs}{text}")


    def has_quited(self, player_input: str) -> bool:
        if isinstance(player_input, str):
            if player_input.upper() == "Q":
                self.is_running = False
                self.keep_playing = False
                return True
            return False

        
    def choose_starter(self) -> None:
        self.current_player_idx = choice([0, 1])
        return None


    def set_heading(self) -> None:
        self.heading['players_info'] = (
            f"{self.players[0].name} ({self.players[0].mark})"
            "    VS    "
            f"{self.players[1].name} ({self.players[1].mark})"
        )


    def get_player_name(self, player_id: str) -> str:
        self.clear_screen()
        player_input = input(f"{player_id}, enter your name: \n")

        if self.has_quited(player_input):
            return None
        if not player_input:
            return player_id
        else:
            return player_input.split()[0].title()


    def get_player_mark(self, player_name: str, player_id: str) -> str:
        self.clear_screen()
        player_input = input(f"{player_name}, X or O?: \n").upper()

        if self.has_quited(player_input):
            return None
        if not player_input:
            return "X" if player_id == "Player 1" else "O"
        elif player_input not in ["X", "O"]:
            self.clear_screen()
            input("Not valid, try again:  X or O?: \n")
        else:
            return player_input


    def get_players_data(self) -> list[Player]:
        players: list[Player] = []
        for id in range(1, 3):
            player_id = f"Player {id}"
            player_name = self.get_player_name(player_id)
            if id == 1:
                player_mark = self.get_player_mark(player_name, player_id)
            else:
                player_mark = "O" if player_mark == "X" else "O"
            players.append(Player(player_id, player_name, player_mark))
        return players
    