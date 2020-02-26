import pygame
from pygame.sprite import Sprite
from pygame.locals import *
vector = pygame.math.Vector2


class Map():

    def __init__(self, game):
        self.zone = pygame.Rect(100, 100, 700, 775)
        self.game = game
        self.screen = game.screen
        self.wall_list = self.getWalls()


        self.right = self.zone.right
        self.bottom = self.zone.bottom
        self.left = self.zone.left
        self.top = self.zone.top

        self.cell_width = 25
        self.cell_height = 25

        print(self.left)
        print(self.right)


    def getWalls(self):
        wallList = []
        for foo in range(0,len(map_input)):
            for bar in range(0,len(map_input[foo])):
                if map_input[foo][bar] == 2:
                    wallList.append(vector(bar,foo))
        return wallList

    def create_grid(self):
        for foo in range(0, 31):
            pygame.draw.line(self.screen, (255, 255, 0), (self.left, self.top + (foo * self.cell_height)), (self.right, self.top + (foo * self.cell_height)), 1)
        for bar in range(0,28):
            pygame.draw.line(self.screen, (255,255,0), (self.left + (bar * self.cell_width), self.top), (self.left + (bar* self.cell_width), self.bottom), 1)

    def update(self):
        for foo in range(0, 31):
            pygame.draw.line(self.screen, (255, 255, 0), (self.left, self.top + (foo * self.cell_height)), (self.right, self.top + (foo * self.cell_height)), 1)
        for bar in range(0,28):
            pygame.draw.line(self.screen, (255,255,0), (self.left + (bar * self.cell_width), self.top), (self.left + (bar* self.cell_width), self.bottom), 1)

        for foo in self.wall_list:
            pygame.draw.rect(self.screen,(112,50,165), ((foo.x*25) + self.top, (foo.y*25) + self.left , 25,25) )

        pass






map_input = [   [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                [2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
                [2,1,2,2,2,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,2,2,2,1,2],
                [2,1,2,1,1,2,1,2,1,1,1,2,1,2,2,1,2,1,1,1,2,1,2,1,1,2,1,2],
                [2,1,2,2,2,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,2,2,2,1,2],
                [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                [2,1,2,2,2,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,1,2],
                [2,1,2,2,2,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,1,2],
                [2,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,2],
                [2,2,2,2,2,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,2,2,2,2,2],
                [2,1,1,1,1,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,1,1,1,1,2],
                [2,1,1,1,1,2,1,2,2,1,1,1,1,1,1,1,1,1,1,2,2,1,2,1,1,1,1,2],
                [2,1,1,1,1,2,1,2,2,1,2,2,2,1,1,2,2,2,1,2,2,1,2,1,1,1,1,2],
                [2,2,2,2,2,2,1,2,2,1,2,1,1,1,1,1,1,2,1,2,2,1,2,2,2,2,2,2],
                [2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2],
                [2,2,2,2,2,2,1,2,2,1,2,1,1,1,1,1,1,2,1,2,2,1,2,2,2,2,2,2],
                [2,1,1,1,1,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,1,1,1,1,2],
                [2,1,1,1,1,2,1,2,2,1,1,1,1,1,1,1,1,1,1,2,2,1,2,1,1,1,1,2],
                [2,1,1,1,1,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,1,1,1,1,2],
                [2,2,2,2,2,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,2,2],
                [2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
                [2,1,2,2,2,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,2,2,2,1,2],
                [2,1,2,2,2,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,2,2,2,1,2],
                [2,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,2],
                [2,2,2,1,2,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,1,2,2,2],
                [2,2,2,1,2,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,1,2,2,2],
                [2,1,1,1,1,1,1,2,2,1,1,1,1,2,2,1,1,1,1,2,2,1,1,1,1,1,1,2],
                [2,1,2,2,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,2,2,2,2,2,2,1,2],
                [2,1,2,2,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,2,2,2,2,2,2,1,2],
                [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]   ]
