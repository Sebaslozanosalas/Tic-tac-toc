import pygame


class GUI:

    def __init__(self):
        self.width = 500
        self.height = 700

        self.color_darker = '#262626'
        self.color_dark = '#2C2C2C'
        self.color_accent = '#FF914D'

        self.screen = None
        self.clock = None
        self.running = True
        self.dt = 0
        self.fps = 60


    def setup(self):
        pygame.init()
        pygame.display.set_caption('Tic Tac Toe by Seb')
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
            self.screen.fill(self.color_darker)
            # self.draw_rect()
            self.draw_grid()
            self.draw_title()
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

        pygame.draw.rect(self.screen, self.color_dark, my_rect)

    def draw_grid(self):

        grid_color = '#2F2F2F'

        # game area square
        screen_width, screen_height = self.screen.get_width(), self.screen.get_height()
        margin = 0.02

        box_size = screen_width - ((screen_width * margin) * 2)
        grid_length = box_size
        grid_width = screen_width * margin

        # draw horizontal lines
        left_pos = margin * screen_width
        top_pos = screen_height - grid_width - ((box_size / 3) * 2) - (grid_width / 2)
        my_rect = pygame.Rect(left_pos, top_pos, grid_length, grid_width)
        pygame.draw.rect(self.screen, grid_color, my_rect)
        
        top_pos = screen_height - grid_width - ((box_size / 3) * 1)  - (grid_width / 2) # update
        my_rect = pygame.Rect(left_pos, top_pos, grid_length, grid_width)
        pygame.draw.rect(self.screen, grid_color, my_rect)


        # draw vertical lines
        left_pos = grid_width + ((box_size / 3) * 1) - (grid_width / 2)
        top_pos = screen_height - (box_size + (screen_width * margin))
        my_rect = pygame.Rect(left_pos, top_pos, grid_width, grid_length)
        pygame.draw.rect(self.screen, grid_color, my_rect)
        
        left_pos = grid_width + ((box_size / 3) * 2) - (grid_width / 2)
        my_rect = pygame.Rect(left_pos, top_pos, grid_width, grid_length)
        pygame.draw.rect(self.screen, grid_color, my_rect)


    def draw_title(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        title = font.render('Tic Tac Toe', True, self.color_accent)
        titleRect = title.get_rect()
        titleRect.center = (self.width // 2, 50)
        self.screen.blit(title, titleRect)