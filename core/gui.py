from shapes.cross import Cross
from shapes.circle import Circle
from shapes.grid import Grid

import pygame
from random import choice


class GUI:

    @staticmethod
    def draw_title(screen, title, color, position, font_size=32):
        font = pygame.font.Font('freesansbold.ttf', font_size)
        title = font.render(title, True, color)
        titleRect = title.get_rect()
        titleRect.center = (position)
        screen.blit(title, titleRect)


    @staticmethod
    def draw_background(screen, color):
        screen.fill(color)


    @staticmethod
    def draw_cross(position, line_size, color):
        cross = Cross(
            position=position,
            line_size=line_size,
            color=color
        )
        return cross
    

    @staticmethod
    def draw_circle(position, size, line_width, color):
        circle = Circle(
            position=position,
            size=size,
            line_width=line_width,
            color=color
        )
        return circle

    # def __init__(self):
    #     self.width = 500
    #     self.height = 700

    #     self.color_darker = '#262626'
    #     self.color_dark = '#4C4C4C'
    #     self.color_accent = "#FF914D"

    #     self.screen = None
    #     self.clock = None
    #     self.running = True
    #     self.dt = 0
    #     self.fps = 60



    # def setup(self):
    #     pygame.init()
    #     pygame.display.set_caption('Tic Tac Toe by Seb')
    #     self.screen = pygame.display.set_mode((self.width, self.height))
    #     self.clock = pygame.time.Clock()
    #     self.all_sprites = pygame.sprite.Group()
    #     self.draw_grid()
    #     self.draw_shapes()


    # def run(self):
    #     self.setup()
    #     while self.running:
    #         self.handle_events()
    #         self.screen.fill(self.color_darker)
    #         self.draw_title()
    #         self.update()
    #         self.dt = self.clock.tick(self.fps) / 1000
    #     pygame.quit()


    # def handle_events(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             self.running = False


    # def update(self):
    #     self.all_sprites.update(self.dt)
    #     self.all_sprites.draw(self.screen)
    #     pygame.display.update()

    # @staticmethod
    # def draw_grid():
    #     screen_width, screen_height = self.screen.get_width(), self.screen.get_height()

    #     # Constants
    #     GRID_MARGIN_RATIO = 0.05
    #     GRID_COLOR = self.color_accent

    #     # Game grid
    #     grid_margin = int(screen_width * GRID_MARGIN_RATIO)

    #     grid_size = screen_width - (grid_margin * 2)
    #     grid_line_width = grid_margin // 2
    #     grid_xpos = grid_margin
    #     grid_ypos = int(screen_height - grid_margin - grid_size)

    #     self.grid = Grid(
    #         grid_xpos = grid_xpos,
    #         grid_ypos = grid_ypos,
    #         grid_size = grid_size,
    #         grid_margin = grid_margin,
    #         grid_line_width = grid_line_width,
    #         grid_color = GRID_COLOR
    #     )
    #     self.all_sprites.add(self.grid.get_sprites())


    # @staticmethod
    # def draw_shapes():
    #     for position in self.grid.get_cell_coordinates():
    #         if choice([True, False]):
    #             cross = Cross(
    #                 position=position,
    #                 line_size=(self.grid.grid_size // 3, self.grid.grid_line_width),
    #                 color=self.color_accent
    #             )
    #             self.all_sprites.add(cross.get_sprites())
    #         else:
    #             circle = Circle(
    #                 position=position,
    #                 size=(self.grid.grid_cell_size - (self.grid.grid_line_width) * 3),
    #                 line_width=self.grid.grid_line_width,
    #                 color=self.grid.grid_color
    #             )
    #             self.all_sprites.add(circle)



