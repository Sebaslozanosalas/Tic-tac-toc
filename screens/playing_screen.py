from .screen import Screen

from core import *

import pygame

class PlayingScreen(Screen):
    def __init__(self, screen_manager, settings_manager, game):
        super().__init__(screen_manager, settings_manager)
        self.game = game
        self.grid_manager = GridManager()

        # Load settings and colors
        self.styles = self.settings_manager.get_settings().get('styles')
        self.background_color = self.styles.get('background_color')
        self.accent_color = self.styles.get('accent_color')

        self.grid = None
        self.grid_sprites = pygame.sprite.Group()

        self.initialized = False


    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # self.screen_manager.set_screen('welcome')
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            self.handle_clicks(click_pos)


    def update(self, dt):
        self.grid_sprites.update(dt)


    def draw(self, screen):
        if not self.initialized:
            self.screen_setup(screen)

        Renderer.draw_background(screen, self.background_color)

        Renderer.draw_title(screen, 'Playing...', self.accent_color, (self.screen_width // 2, 100), 45)

        heading = f'{self.game.players[0]}   VS   {self.game.players[1]}'
        Renderer.draw_title(screen, heading, self.accent_color, (self.screen_width // 2, 160), 20)
        
        self.grid_sprites.draw(screen)


    def screen_setup(self, screen):
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
        # Create grid
        self.grid_manager.create_grid(screen, self.accent_color)
        self.grid_sprites.add(self.grid_manager.grid.get_sprites())

        self.initialized = True
        

    def handle_clicks(self, click_pos):
        # If clicked in a cell
        if self.grid_manager.clicked_in_cell(click_pos):
            # Get clicked cell and place marker
            x_idx, y_idx = self.grid_manager.get_cell_clicked(click_pos)
            print(f'Cell clicked: ({x_idx}, {y_idx})')
            cell_coordinates = self.grid_manager.get_cell_coordinates()
            print('Cell coordinates: ', cell_coordinates)
            cell_coord = cell_coordinates[y_idx][x_idx]
            print('Cell coord gathered: ', cell_coord)

            cross = Renderer.create_cross(
                position=cell_coord,
                line_length= self.grid_manager.grid.size // 3,
                line_width= self.grid_manager.grid.line_width,
                color=self.accent_color
            )

            self.grid_sprites.add(cross.get_sprites())

