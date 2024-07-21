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

        screen_width, screen_height = self.screen.get_width(), self.screen.get_height()

        # Constants
        GRID_MARGIN_RATIO = 0.02
        GRID_COLOR = '#2F2F2F'

        # Game grid
        grid_margin = screen_width * GRID_MARGIN_RATIO

        grid_size = screen_width - (grid_margin * 2)
        grid_line_width = grid_margin

        # Calculate positions for horizontal lines
        left_pos = grid_margin
        top_positions = [
            screen_height - grid_line_width - ((grid_size / 3) * 2) - (grid_line_width / 2),
            screen_height - grid_line_width - ((grid_size / 3) * 1)  - (grid_line_width / 2)
        ]

        # Draw horizontal lines
        for top_pos in top_positions:
            grid_line = pygame.Rect(left_pos, top_pos, grid_size, grid_line_width)
            pygame.draw.rect(self.screen, GRID_COLOR, grid_line)

        # Calculate positions for vertical lines
        top_pos = screen_height - grid_margin - grid_size
        left_positions = [
            grid_line_width + ((grid_size / 3) * 1) - (grid_line_width / 2),
            grid_line_width + ((grid_size / 3) * 2) - (grid_line_width / 2)
        ]

        # Draw vertical lines
        for left_pos in left_positions:
            grid_line = pygame.Rect(left_pos, top_pos, grid_line_width, grid_size)
            pygame.draw.rect(self.screen, GRID_COLOR, grid_line)            

    def draw_title(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        title = font.render('Tic Tac Toe', True, self.color_accent)
        titleRect = title.get_rect()
        titleRect.center = (self.width // 2, 50)
        self.screen.blit(title, titleRect)