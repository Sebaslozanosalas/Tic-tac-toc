import pygame


class GUI:

    def __init__(self):
        self.width = 500
        self.height = 700

        self.bg = '#262626'
        self.bg_ligth = '#2C2C2C'

        self.screen = None
        self.clock = None
        self.running = True
        self.dt = 0
        self.fps = 60


    def setup(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()


    def handle_events(self):
        """pygame.QUIT event means the user clicked X to close your window"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def run(self):
        self.setup()
        while self.running:
            self.handle_events()
            self.screen.fill(self.bg)
            self.draw_rect()
            pygame.display.flip()
            self.dt = self.clock.tick(self.fps) / 1000
        pygame.quit()


    def draw_rect(self):
        # game area square
        screen_width, screen_height = self.screen.get_width(), self.screen.get_height()
        margin = 0.03

        box_size = screen_width - ((screen_width * margin) * 2)
        # calcular posicion centrada
        left_pos = (screen_width * margin)
        top_pos = screen_height - (box_size + (screen_width * margin))

        my_rect = pygame.Rect(left_pos, top_pos, box_size, box_size)

        pygame.draw.rect(self.screen, self.bg_ligth, my_rect)
