import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Map():

    def __init__(self, game):
        self.zone = pygame.Rect(50, 25, 700, 825)
        self.game = game
        self.screen = game.screen
        self.grid = map_input
        self.lines = []

        self.width = self.zone.width
        self.height = self.zone.height
        self.left = self.zone.left
        self.top = self.zone.top

        self.cell_width = (self.width/28)
        self.cell_height = (self.height/33)





    def create_grid(self):
        for foo in range(0, 38):
            pygame.draw.line(self.screen, (255, 255, 20), (self.left, self.top + (foo * self.cell_height)), (self.width, self.top + (foo * self.cell_height)), 1)

    def update(self):
        for foo in range(0, 38):
            pygame.draw.line(self.screen, (255, 255, 20), (self.left, self.top + (foo * self.cell_height)), (self.width, self.top + (foo * self.cell_height)), 1)


        pass








map_input = [   [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 1],
                [1, 1, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0]]
