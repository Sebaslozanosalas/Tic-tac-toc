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
        self.sprites = pygame.sprite.Group()

        self.initialized = False


    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # self.screen_manager.set_screen('welcome')
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            self.handle_clicks(click_pos)


    def update(self, dt):
        self.sprites.update(dt)


    def draw(self, screen):
        if not self.initialized:
            self.screen_setup(screen)
        
        # Print heading
        Renderer.draw_background(screen, self.background_color)
        Renderer.draw_title(screen, f'{self.game.current_player}', self.accent_color, (self.screen_width // 2, 100), 35)
        # Print versus heading
        heading = f'{self.game.players[0]}   VS   {self.game.players[1]}'
        Renderer.draw_title(screen, heading, '#9da222', (self.screen_width // 2, 140), 20)
        
        self.sprites.draw(screen)


    def screen_setup(self, screen):
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
        # Create grid
        self.grid_manager.create_grid(screen, self.accent_color)
        self.sprites.add(self.grid_manager.grid.get_sprites())

        # Choose random starter
        self.game.choose_starter()
        
        self.initialized = True
        

    def handle_clicks(self, click_pos):
        # If clicked in a cell
        if self.grid_manager.clicked_in_cell(click_pos):
            # Get clicked cell and place marker
            x_idx, y_idx = self.grid_manager.get_cell_clicked(click_pos)
            cell_coordinates = self.grid_manager.get_cell_coordinates()
            cell_coord = cell_coordinates[y_idx][x_idx]

            self.place_mark(cell_coord, self.game.current_player.mark)
            self.game.switch_player()

            


    def place_mark(self, position, mark):
        if mark == 'X':
            sprites = Renderer.create_cross(
                position=position,
                line_length= self.grid_manager.grid.size // 3,
                line_width= self.grid_manager.grid.line_width,
                color=self.accent_color
            ).get_sprites()

        if mark == 'O':
            sprites = Renderer.create_circle(
                position=position,
                size=(self.grid_manager.grid.size // 3) \
                    - (self.grid_manager.grid.line_width * 2),
                line_width=self.grid_manager.grid.line_width,
                color=self.accent_color
            )

        self.sprites.add(sprites)
    
