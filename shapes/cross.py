from shapes.line import Line

import pygame

class Cross:
    
    def __init__(self, position, line_size, color='white'):
        self.all_sprites = pygame.sprite.Group()
        self.color = color
        self.create(position, line_size)

    def create(self, position, line_size):
        for angle in [-45, 45]:
            line = Line(
                position=position,
                line_size=line_size,
                color=self.color
            )
            line.rotate(angle)
            self.all_sprites.add(line)

    def get_sprites(self):
        return self.all_sprites.sprites()