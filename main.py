from random import choice
import os
from time import sleep


class Player:
    def __init__(self, id: str, name: str, mark: str):
        self.id = id
        self.name = name
        self.mark = mark
    
    def __str__(self):
        return self.name


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


class Game:
    def __init__(self):
        self.board = Board()
        self.players = None
        self.current_player_idx = None
        self.heading = {
            'title': 'Tic Tac Toe',
            'players_info': '',
            'next_turn': ''
        }
        self.is_running = True

    def play(self) -> None:
        
        # Get users data
        self.players = self.get_players_data()

        self.set_heading()
        
        # Choose random starter
        self.choose_starter()
        self.heading['next_turn'] = f"{self.players[self.current_player_idx]} starts"

        while(self.is_running):
            
            self.current_player_move()
            #self.check_winner()
            self.switch_player()

            # 


        self.clear_screen()
        print("Quiting...")

    def current_player_move(self):
        self.clear_screen()
        self.board.show()
        
        while(True):
            player_input = input("Enter your position: \n")

            if self.has_quited(player_input):
                return None
        
            try:
                player_input = int(player_input)
                if player_input in range(1, 10):
                    break
                else:
                    print("Invalid option, enter (1-9): ")    
            except Exception as e:
                print("Not a number, enter (1-9): ")
        
        self.board.update_cell(player_input, self.players[self.current_player_idx])
        
    def switch_player(self) -> None:
        self.current_player_idx = 1 if self.current_player_idx == 0 else 0
        self.heading['next_turn'] = f'Is {self.players[self.current_player_idx]} turn'
          
    def clear_screen(self) -> None:
        os.system('clear')

        for text in self.heading.values():
            self.print_centered(text)

    def print_centered(self, text: str) -> None:
        term_width = os.get_terminal_size()[0]
        text_len = len(text)
        spcs = int((term_width - text_len) / 2)
        print(f"{" " * spcs}{text}")

    def has_quited(self, player_input: str) -> bool:
        if isinstance(player_input, str):
            if player_input.upper() == "Q":
                self.is_running = False
                return True
            else:
                return False
        
    def choose_starter(self) -> None:
        self.current_player_idx = choice([0, 1])
        return None

    def set_heading(self) -> None:
        self.heading['players_info'] = (
            f"{self.players[0].name} ({self.players[0].mark})"
            "    VS    "
            f"{self.players[1].name} ({self.players[1].mark})"
            "\n"
        )

    def get_player_name(self, player_id: str) -> str:
        self.clear_screen()
        player_name = input(f"{player_id}, enter your name: \n")

        if self.has_quited(player_name):
            return None
        if not player_name:
            return player_id
        else:
            return player_name.split()[0].title()

    def get_player_mark(self, player_name: str, player_id: str) -> str:
        self.clear_screen()
        player_mark = input(f"{player_name}, X or O?: \n").upper()

        if self.has_quited(player_mark):
            return None
        if not player_mark:
            return "X" if player_id == "Player 1" else "O"
        elif player_mark not in ["X", "O"]:
            self.clear_screen()
            input("Not valid, try again:  X or O?: \n")
        else:
            return player_mark

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
    
    

if __name__ == "__main__":
    game = Game()
    game.play()