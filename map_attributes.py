import pygame
from pygame.sprite import Sprite
from pygame.locals import *
vector = pygame.math.Vector2

class Pellet(Sprite):
    IMAGE = pygame.transform.scale(pygame.image.load(f'images/RedGhostRight.png'), (25, 25))
    YELLOW = (255, 255,0)
    def __init__(self, game, map, position):

        super().__init__()

        self.game = game
        self.map = map
        self.screen = game.screen
        self.position = position
        #self.image = Pellet.IMAGE
        #self.rect = self.image.get_rect()
        #self.rect.topleft = self.position

    def draw(self):
        pygame.draw.circle(self.screen, Pellet.YELLOW,(int(self.position.x + 13),int(self.position.y + 13)) , 2)

class Map():

    def __init__(self, game):
        self.zone = pygame.Rect(25, 20, 700, 775)
        self.game = game
        self.screen = game.screen



        self.right = self.zone.right
        self.bottom = self.zone.bottom
        self.left = self.zone.left
        self.top = self.zone.top

        self.cell_width = 25
        self.cell_height = 25

        self.Pellets = pygame.sprite.Group()
        self.wall_list = self.setLayout()


    def setFood(self, x ,y):
        position = vector((x * self.cell_width) + self.left, (y * self.cell_height) + self.top)
        pellet = Pellet(self.game, self, position)
        self.Pellets.add(pellet)

    def setLayout(self):
        wallList = []
        for foo in range(0,len(map_input)):
            for bar in range(0,len(map_input[foo])):
                if map_input[foo][bar] == 2:
                    wallList.append(vector(bar,foo))
                if map_input[foo][bar] == 1:
                    self.setFood(bar, foo)
        return wallList



    def update(self):

        for pellet in self.Pellets.sprites():
            pellet.draw()
        for foo in self.wall_list:
            pygame.draw.rect(self.screen,(112,50,165), ((foo.x*25) + self.left, (foo.y*25) + self.top , 25,25) )

        pass






map_input = [   [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                [2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
                [2,1,2,2,2,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,2,2,2,1,2],
                [2,1,2,0,0,2,1,2,0,0,0,2,1,2,2,1,2,0,0,0,2,1,2,0,0,2,1,2],
                [2,1,2,2,2,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,2,2,2,1,2],
                [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                [2,1,2,2,2,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,1,2],
                [2,1,2,2,2,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,1,2],
                [2,1,1,1,1,1,1,2,2,1,1,1,1,2,2,1,1,1,1,2,2,1,1,1,1,1,1,2],
                [2,2,2,2,2,2,1,2,2,2,2,2,0,2,2,0,2,2,2,2,2,1,2,2,2,2,2,2],
                [0,0,0,0,0,2,1,2,2,2,2,2,0,2,2,0,2,2,2,2,2,1,2,0,0,0,0,0],
                [0,0,0,0,0,2,1,2,2,0,0,0,0,0,0,0,0,0,0,2,2,1,2,0,0,0,0,0],
                [0,0,0,0,0,2,1,2,2,0,2,2,2,0,0,2,2,2,0,2,2,1,2,0,0,0,0,0],
                [2,2,2,2,2,2,1,2,2,0,2,0,0,0,0,0,0,2,0,2,2,1,2,2,2,2,2,2],
                [0,0,0,0,0,0,1,1,1,0,2,0,0,0,0,0,0,2,0,1,1,1,0,0,0,0,0,0],
                [2,2,2,2,2,2,1,2,2,0,2,0,0,0,0,0,0,2,0,2,2,1,2,2,2,2,2,2],
                [0,0,0,0,0,2,1,2,2,0,2,2,2,2,2,2,2,2,0,2,2,1,2,0,0,0,0,0],
                [0,0,0,0,0,2,1,2,2,0,0,0,0,0,0,0,0,0,0,2,2,1,2,0,0,0,0,0],
                [0,0,0,0,0,2,1,2,2,0,2,2,2,2,2,2,2,2,0,2,2,1,2,0,0,0,0,0],
                [2,2,2,2,2,2,1,2,2,0,2,2,2,2,2,2,2,2,0,2,2,1,2,2,2,2,2,2],
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
