from shapes.line import Line

import pygame

class Cross:  
    def __init__(self, position, line_size, color='white'):
        self.all_sprites = pygame.sprite.Group()
        self.color = color
        self.create(position, line_size)


    def create(self, position, line_size):
        # Line 1 
        line_1 = Line(
            position=position,
            line_size=line_size,
            color=self.color
        )
        line_1.rotate(-45)
        line_1_rect = line_1.rect

        # Line 2
        line_2 = Line(
            position=position,
            line_size=line_size,
            color=self.color
        )
        line_2.rotate(45)
        line_2_rect = line_2.rect

        self.calculate_rect(line_1_rect, line_2_rect)
        self.all_sprites.add(line_1, line_2)


    def get_sprites(self):
        return self.all_sprites.sprites()
    

    def calculate_rect(self, line_1, line_2):
        self.rect = line_1.union(line_2)

        