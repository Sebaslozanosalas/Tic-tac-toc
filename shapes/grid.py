from shapes.line import Line

import pygame

class Grid:

    def __init__(self, grid_xpos, grid_ypos, grid_size, grid_margin, grid_line_width, grid_color):
        self.bg_color = '#696969'
        self.all_sprites = pygame.sprite.Group()

        self.grid_xpos = grid_xpos
        self.grid_ypos = grid_ypos
        self.grid_size = int(grid_size)
        self.grid_margin = grid_margin
        self.grid_cell_size = self.grid_size // 3
        self.grid_line_width = int(grid_line_width)
        self.grid_color = grid_color
        self.create()
        
        # self.create_background(grid_xpos, grid_ypos, grid_size)


    def create(self):

        grid_center = self.grid_size // 2

        # Draw horizontal lines
        for i in range(1, 3):
            h_line = Line(
                position = (self.grid_xpos + grid_center, self.grid_ypos + (self.grid_cell_size * i)),
                line_size = (self.grid_size, self.grid_line_width),
                color = self.grid_color
            )
            v_line = Line(
                position = (self.grid_margin + (self.grid_cell_size * i), self.grid_ypos + grid_center),
                line_size = (self.grid_line_width, self.grid_size),
                color = self.grid_color
            )
            self.all_sprites.add(h_line, v_line)


    def get_sprites(self):
        return self.all_sprites.sprites()
    

    def create_background(self):
        bg_sprite = pygame.sprite.Sprite()
        bg_sprite.image = pygame.Surface((self.grid_size, self.grid_size))
        bg_sprite.image.fill(self.bg_color)
        bg_sprite.rect = bg_sprite.image.get_rect()
        bg_sprite.rect = (self.grid_xpos, self.grid_ypos)

        self.all_sprites.add(bg_sprite)


    def get_cell_coordinates(self) -> list[tuple]:
        
        # Calculate X positions
        x_start = self.grid_xpos + (self.grid_cell_size // 2)
        x_positions = [x_start + (self.grid_cell_size * i) for i in range(3)]
        
        # Calculate Y positions
        y_start = self.grid_ypos + (self.grid_cell_size // 2)
        y_positions = [y_start + (self.grid_cell_size * i)  for i in range(3)]

        # Make final positions
        all_positions = []
        for x_pos in x_positions:
            for y_pos in y_positions:
                all_positions.append((x_pos, y_pos))

        return all_positions
