from .line import Line

import pygame

class Grid:
    def __init__(self, grid_xpos, grid_ypos, grid_size, grid_margin, grid_line_width, grid_color):
        self.bg_color = '#696969'
        self.all_sprites = pygame.sprite.Group()
        # self.create_background(grid_xpos, grid_ypos, grid_size)
        self.create(grid_xpos, grid_ypos, grid_size, grid_margin, grid_line_width, grid_color)


    def create(self, grid_xpos, grid_ypos, grid_size, grid_margin, grid_line_width, grid_color):

        grid_size = int(grid_size)
        grid_line_width = int(grid_line_width)
        grid_cell_size = grid_size // 3

        grid_center = grid_size // 2

        # Draw horizontal lines
        for i in range(1, 3):
            h_line = Line(
                position = (grid_xpos + grid_center, grid_ypos + (grid_cell_size * i)),
                line_size = (grid_size, grid_line_width),
                color = grid_color
            )
            v_line = Line(
                position = (grid_margin + (grid_cell_size * i), grid_ypos + grid_center),
                line_size = (grid_line_width, grid_size),
                color = grid_color
            )
            self.all_sprites.add(h_line, v_line)


    def get_sprites(self):
        return self.all_sprites.sprites()
    
    def create_background(self, grid_xpos, grid_ypos, grid_size):
        bg_sprite = pygame.sprite.Sprite()
        bg_sprite.image = pygame.Surface((grid_size, grid_size))
        bg_sprite.image.fill(self.bg_color)
        bg_sprite.rect = bg_sprite.image.get_rect()
        bg_sprite.rect = (grid_xpos, grid_ypos)

        self.all_sprites.add(bg_sprite)