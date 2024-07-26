from settings import *
from screens import *

import pygame

class Screen:
    def __init__(self, screen_manager, settings_manager=None):
        self.screen_manager = screen_manager
        self.settings_manager = settings_manager
        self.sprites = pygame.sprite.Group()

    def handle_events(self, event):
        pass


    def update(self, dt):
        pass


    def draw(self, screen):
        pass