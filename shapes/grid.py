from shapes import Line

import pygame

class Grid:
    def __init__(
            self,
            x_pos,
            y_pos,
            size,
            margin,
            line_width,
            color
    ):
        self.sprites = pygame.sprite.Group()

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = int(size)
        self.margin = margin
        self.cell_size = self.size // 3
        self.line_width = int(line_width)
        self.color = color
        self.create()



    def create(self):
        grid_center = self.size // 2
        # Draw horizontal lines
        for i in range(1, 3):
            h_line = Line(
                position = (
                    self.x_pos + grid_center,
                    self.y_pos + (self.cell_size * i)
                ),
                line_length=self.size,
                line_width=self.line_width,
                color = self.color
            )
            v_line = Line(
                position = (
                    self.margin + (self.cell_size * i),
                    self.y_pos + grid_center
                ),
                line_length=self.line_width,
                line_width=self.size,
                color = self.color
            )
            self.sprites.add(h_line, v_line)


    def get_sprites(self):
        return self.sprites.sprites()

