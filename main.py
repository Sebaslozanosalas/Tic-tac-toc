from core import *
from screens import *
from settings import *

import pygame

class App:
    def __init__(self):
        self.running = True
        self.title = 'Tic Tac Toe by Seb'
        self.width = 500
        self.height = 700
        self.fps = 60
        self.dt = None
        

    def setup(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.all_sprites = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        
        # Create SettingsmManager
        self.settings_manager = SettingsManager()
        game = Game()

        # Create ScreenManager and Screens
        self.screen_manager = ScreenManager()
        self.screen_manager.add_screen(
            'welcome', WelcomeScreen(self.screen_manager, self.settings_manager, game)
        )
        self.screen_manager.add_screen(
            'game', PlayingScreen(self.screen_manager, self.settings_manager, game)
        )
        self.screen_manager.add_screen(
            'selection', SelectionScreen(self.screen_manager, self.settings_manager, game)
        )

        # Set Welcome Screen
        self.screen_manager.set_screen('welcome')


    def run(self):
        self.setup()

        # Main game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.screen_manager.handle_events(event)

            self.screen_manager.update(self.dt)
            self.screen_manager.draw(self.screen)
            pygame.display.update()
            self.dt = self.clock.tick(self.fps) / 1000

        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.run()

