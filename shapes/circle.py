import pygame

class Circle(pygame.sprite.Sprite):
    
    def __init__(self, position, size, line_width, color='white'):
        super().__init__()
        self.position = position
        self.size = size
        self.line_width = line_width
        self.color = color
        self.create()
        self.rect.center = position

    def create(self):
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)

        pygame.draw.ellipse(
            surface=self.image,
            color=self.color,
            rect=(0, 0, self.size, self.size),
            width=self.line_width
        )
        self.rect = self.image.get_rect()