from core import *
from screens import *

import pygame


class App:

    def __init__(self):
        self.running = True
        self.title = 'Tic Tac Toe by Seb'
        self.width = 500
        self.height = 700
        self.fps = 60
        

    def setup(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.all_sprites = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

    def run(self):
        self.setup()

        # Create ScreenManager and Screens
        screen_manager = ScreenManager()
        screen_manager.add_screen('game', GameScreen(screen_manager))
        screen_manager.add_screen('welcome', WelcomeScreen(screen_manager))
        # Set Welcome Screen
        screen_manager.set_screen('welcome')

        # Main game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                screen_manager.handle_events(event)

            screen_manager.update()
            screen_manager.draw(self.screen)
            pygame.display.update()
            dt = self.clock.tick(self.fps) / 1000

        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.run()