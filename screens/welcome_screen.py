from screens.screen import Screen
from core.gui import GUI

import pygame

class WelcomeScreen(Screen):

    def __init__(self, screen_manager, settings_manager):
        super().__init__(screen_manager, settings_manager)
        self.load_configuration_file()


    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.screen_manager.set_screen('game')


    def update(self):
        pass


    def draw(self, screen):
        color = self.settings.get('styles').get('accent_color')
        GUI.draw_background(screen, color)
        GUI.draw_title(screen, 'Welcome', 'black')

        
        # screen.fill((100, 100, 100))
        # font = pygame.font.Font('freesansbold.ttf', 32)
        # title = font.render('Welcome Screen', True, 'white')
        # titleRect = title.get_rect()
        # titleRect.center = (screen.get_width() // 2, 50)
        # screen.blit(title, titleRect)

    def load_configuration_file(self):
        self.settings = self.settings_manager.get_settings()