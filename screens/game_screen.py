from screens.screen import Screen
from core.gui import GUI

import pygame

class GameScreen(Screen):

    def __init__(self, screen_manager, settings_manager):
        super().__init__(screen_manager, settings_manager)
        self.load_configuration_file()


    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.screen_manager.set_screen('welcome')


    def update(self):
        pass


    def draw(self, screen):
        bg_color = self.settings.get('styles').get('background_color')
        accent_color = self.settings.get('styles').get('accent_color')
        GUI.draw_background(screen, bg_color)
        GUI.draw_title(screen, 'Ready to play', accent_color)


    def load_configuration_file(self):
        self.settings = self.settings_manager.get_settings()