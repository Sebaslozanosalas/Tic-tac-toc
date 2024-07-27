from .screen import Screen

from core import *
from models import *

from random import choice
import pygame


class SelectionScreen(Screen):
    def __init__(self, screen_manager, settings_manager, game):
        super().__init__(screen_manager, settings_manager)
        self.load_configuration_file()
        self.game = game


    def handle_events(self, event):
        # Handle click 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not bool(self.game.players):
                click_pos = pygame.mouse.get_pos()
                self.handle_shape_clicks(click_pos)
        # Handle "Enter"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.choose_random_mark()


    def update(self, dt):
        self.sprites.update(dt)


    def draw(self, screen):
        self.screen_width, self.screen_height = screen.get_width(), screen.get_height()
        
        # Load colors
        self.background_color = self.settings.get('styles').get('background_color')
        self.accent_color = self.settings.get('styles').get('accent_color')

        # Draw the background
        Renderer.draw_background(screen, self.background_color)

        # Texts
        Renderer.draw_title(screen, 'Player 1, choose your Mark',self.accent_color, (self.screen_width // 2, 100), 30)
        Renderer.draw_title(screen, 'or press enter for random', self.accent_color, (self.screen_width // 2, 130), 16)

        # Markers to choose
        self.draw_markers_to_choose()
        self.sprites.draw(screen)


    def load_configuration_file(self):
        self.settings = self.settings_manager.get_settings()


    def draw_markers_to_choose(self):
        container_size = int(self.screen_width * 0.90)
        side_offset = (self.screen_width - container_size) / 2

        container_third = container_size // 3
        first_pos = side_offset + (container_third) 
        second_pos = side_offset + (container_third * 2)

        self.cross = Renderer.create_cross(
            position=(first_pos, self.screen_height // 2),
            line_length=100,
            line_width=10,
            color=self.accent_color
        )
        self.circle = Renderer.create_circle(
            position=(second_pos, self.screen_height // 2),
            size=80,
            line_width=10,
            color=self.accent_color
        )
        self.sprites.add(
            self.cross.get_sprites(),
            self.circle
        )
    

    def choose_random_mark(self):
        self.create_players(choice(['X', 'O']))


    def handle_shape_clicks(self, click_pos):
        selected_shape = None
        if self.cross and self.cross.rect.collidepoint(click_pos):
            selected_shape = 'X'
        elif self.circle and self.circle.rect.collidepoint(click_pos):
            selected_shape = 'O'

        if selected_shape:
            self.create_players(selected_shape)

    
    def create_players(self, player1_mark):
        # Create Player 1
        player1 = Player('Player 1', player1_mark)

        # Create Player 2
        player2_mark = 'O' if player1_mark == 'X' else 'X'
        player2 = Player('Player 2', player2_mark)

        self.game.players = [player1, player2]
        print(player1, player2)
        self.screen_manager.set_screen('game')

