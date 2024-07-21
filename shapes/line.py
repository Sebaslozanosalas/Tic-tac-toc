import pygame

class Line(pygame.sprite.Sprite):

    def __init__(self, position: tuple, line_size: tuple, color='white'):
        super().__init__()
        self.color = color
        self.create_line_shape(line_size)
        self.rect.center = position
        
        
    def create_line_shape(self, line_size):
        length, width = line_size
        self.image = pygame.Surface((length, width), pygame.SRCALPHA)
        
        # Dibujar el rectángulo 
        pygame.draw.rect(
            surface=self.image,
            color=self.color,
            rect=(0, 0, length, width),
            border_radius=width // 2
        )
        self.rect = self.image.get_rect()


    def rotate(self, angle):
        old_center = self.rect.center
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=old_center)
    