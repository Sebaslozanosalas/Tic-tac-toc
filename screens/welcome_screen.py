from screens.screen import Screen

import pygame

class WelcomeScreen(Screen):

    def __init__(self, screen_manager):
        super().__init__(screen_manager)


    def handle_events(self, event):
        pass


    def update(self):
        pass


    def draw(self, screen):
        screen.fill((100, 100, 100))
        font = pygame.font.Font('freesansbold.ttf', 32)
        title = font.render('Welcome Screen', True, 'white')
        titleRect = title.get_rect()
        titleRect.center = (screen.get_width() // 2, 50)
        screen.blit(title, titleRect)

