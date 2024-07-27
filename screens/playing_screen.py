from screens.screen import Screen
from core.gui import GUI

import pygame

class PlayingScreen(Screen):
    def __init__(self, screen_manager, settings_manager, game):
        super().__init__(screen_manager, settings_manager)
        self.load_configuration_file()
        self.game = game

        # Load colors
        self.background_color = self.settings.get('styles').get('background_color')
        self.accent_color = self.settings.get('styles').get('accent_color')

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
        self.sprites.update(dt)


    def draw(self, screen):
        if not self.initialized:
            self.screen_setup(screen)

        GUI.draw_background(screen, self.background_color)

        GUI.draw_title(screen, 'Playing...', self.accent_color, (self.screen_width // 2, 100), 45)

        heading = f'{self.game.players[0]}   VS   {self.game.players[1]}'
        GUI.draw_title(screen, heading, self.accent_color, (self.screen_width // 2, 160), 20)
        
        self.grid_sprites.draw(screen)


    def screen_setup(self, screen):
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
        self.create_grid(screen)

        self.initialized = True
        

    def load_configuration_file(self):
        self.settings = self.settings_manager.get_settings()
        
        
    def create_grid(self, screen):
        grid_margin = 0.05
        grid_color = self.accent_color
        self.grid = GUI.create_grid(screen, grid_color, grid_margin)
        self.grid_sprites.add(self.grid.get_sprites())


    def handle_clicks(self, click_pos):
        if self.clicked_in_cell(click_pos):
            cell_idxs = self.get_cell_clicked(click_pos)
            # self.place_mark(cell_idxs, 'X')


    def get_cell_clicked(self, click_pos):
        x_click_pos, y_click_pos = click_pos

        x_limits, y_limits = self.grid.get_cell_limits()
        print(f'click_position: {click_pos}')

        for i in range(3):
            if x_click_pos < x_limits[i]:
                x_cell_idx = i 
                break
        for i in range(3):
            if y_click_pos < y_limits[i]:
                y_cell_idx = i 
                break
        
        print(x_cell_idx, y_cell_idx)
        return (x_cell_idx, y_cell_idx)
        

    def clicked_in_cell(self, click_pos):
        x_click_pos, y_click_pos = click_pos
        # Validate x position inside grid
        if x_click_pos > self.grid.grid_xpos \
            and x_click_pos < (self.grid.grid_xpos + self.grid.grid_size):
            # Validate y position inside grid
            if y_click_pos > self.grid.grid_ypos \
                and y_click_pos < (self.grid.grid_ypos + self.grid.grid_size):
                return True
        return False
    

    def place_mark(self, cell_idxs, mark):
        pass
        # GUI.draw_marker_on_board()