import pygame

class Line(pygame.sprite.Sprite):
    def __init__(self, position, line_length, line_width, color='white'):
        super().__init__()
        self.color = color
        self.create(line_length, line_width)
        self.rect.center = position
        
        
    def create(self, line_length, line_width):
        self.image = pygame.Surface((line_length, line_width), pygame.SRCALPHA)
        
        pygame.draw.rect(
            surface=self.image,
            color=self.color,
            rect=(0, 0, line_length, line_width),
            border_radius=line_width // 2
        )
        self.rect = self.image.get_rect()


    def rotate(self, angle):
        old_center = self.rect.center
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=old_center)
    