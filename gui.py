import pygame

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

BG_COLOR = '#262626'
OTHER_COLOR = '#2C2C2C'

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500,  700))
clock = pygame.time.Clock()
running = True
dt = 0

while running:

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    # game area square
    screen_width, screen_height = screen.get_width(), screen.get_height()
    margin = 0.03

    box_size = screen_width - ((screen_width * margin) * 2)
    # calcular posicion centrada
    left_pos = (screen_width * margin)
    top_pos = screen_height - (box_size + (screen_width * margin))

    my_rect = pygame.Rect(left_pos, top_pos, box_size, box_size)

    pygame.draw.rect(screen, OTHER_COLOR, my_rect)
    pygame.display.flip()



    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()