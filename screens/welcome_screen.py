from .screen import Screen

from core import *

import pygame

class WelcomeScreen(Screen):
    def __init__(self, screen_manager, settings_manager, game):
        super().__init__(screen_manager, settings_manager)
        self.load_configuration_file()
        self.game = game


    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.screen_manager.set_screen('selection')

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.screen_manager.set_screen('selection')


    def update(self, dt):
        pass


    def draw(self, screen):
        self.screen_width, self.screen_height = screen.get_width(), screen.get_height()
        # Load colors
        background_color = self.settings.get('styles').get('background_color')
        accent_color = self.settings.get('styles').get('accent_color')
        
        # Draw the background
        Renderer.draw_background(screen, background_color)

        # Print Welcome Headings
        title_pos = self.screen_height // 3
        screen_middle = self.screen_width // 2
        Renderer.draw_title(screen, 'Welcome to', accent_color, (screen_middle, title_pos - 40), 18)
        Renderer.draw_title(screen, 'Tic Tac Toe', accent_color, (screen_middle, title_pos), 46)
        Renderer.draw_title(screen, '- by Seb', accent_color, (screen_middle, title_pos + 50), 16)
        Renderer.draw_title(screen, 'Press Enter to start', '#9da222', (screen_middle, self.screen_height - 100), 26)
        

    def load_configuration_file(self):
        self.settings = self.settings_manager.get_settings()

