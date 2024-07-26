from screens.screen import Screen
from core.gui import GUI

import pygame

class PlayingScreen(Screen):
    def __init__(self, screen_manager, settings_manager, game):
        super().__init__(screen_manager, settings_manager)
        self.load_configuration_file()
        self.game = game


    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # self.screen_manager.set_screen('welcome')
            pygame.quit()


    def update(self, dt):
        self.sprites.update(dt)


    def draw(self, screen):
        self.screen_width, self.screen_height = screen.get_width(), screen.get_height()
        
        # Load colors
        self.background_color = self.settings.get('styles').get('background_color')
        self.accent_color = self.settings.get('styles').get('accent_color')

        # Draw background and title
        GUI.draw_background(screen, self.background_color)
        GUI.draw_title(screen, 'Playing...', self.accent_color, (self.screen_width // 2, 100), 45)

        heading = f'{self.game.players[0]}   VS   {self.game.players[1]}'
        GUI.draw_title(screen, heading, self.accent_color, (self.screen_width // 2, 160), 20)


    def load_configuration_file(self):
        self.settings = self.settings_manager.get_settings()

