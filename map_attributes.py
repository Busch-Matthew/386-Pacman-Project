import pygame
from pygame.sprite import Sprite
from pygame.locals import *
vector = pygame.math.Vector2



class Pellet(Sprite):

    YELLOW = (255, 255,0)

    def __init__(self, game, map, position):

        super().__init__()

        self.game = game
        self.map = map
        self.screen = game.screen
        self.position = position
        self.rect = pygame.Rect((self.position),(2,2))
        #self.image = Pellet.IMAGE
        #self.rect = self.image.get_rect()
        #self.rect.topleft = self.position

    def draw(self):
        pygame.draw.circle(self.screen, Pellet.YELLOW,(int(self.position.x + 13),int(self.position.y + 13)) , 2)

class PowerPellet(Sprite):

    YELLOW = (255, 255,0)

    def __init__(self, game, map, position):

        super().__init__()

        self.game = game
        self.map = map
        self.screen = game.screen
        self.position = position
        self.rect = pygame.Rect((self.position),(7,7))
        self.draw_index = 0
        #self.image = Pellet.IMAGE
        #self.rect = self.image.get_rect()
        #self.rect.topleft = self.position

    def draw(self):
        self.draw_index +=1
        if self.draw_index < 50:
            pygame.draw.circle(self.screen, Pellet.YELLOW,(int(self.position.x + 13),int(self.position.y + 13)) , 7)
        self.draw_index +=1
        if self.draw_index > 100:
            self.draw_index = 0

class Portal(Sprite):
    def __init__(self, game, map, position, exit_position, exit_velocity):
        super().__init__()

        self.game = game
        self.map = map
        #self.screen = game.screen
        self.x_position = position.x * 25 + self.map.left
        self.y_position = position.y * 25 + self.map.top

        self.rect = pygame.Rect(self.x_position, self.y_position, 25, 25)
        self.imageRect = pygame.Rect(self.x_position, self.y_position,80,30)
        self.exit_location = vector(exit_position.x * 25 + self.map.left, exit_position.y * 25 + self.map.top)

        self.exit_velocity = vector(exit_velocity)

    def get_transport_location(self):

        return self.transport_location


class Fruit(Sprite):
    FRUIT_INDEX = 0
    FRUIT_LIST = ['cherry', 'cherry', 'cherry', 'cherry', 'berry', 'berry', 'oran','apple']

    def __init__(self, game, map):
        super().__init__()

        self.game = game
        self.screen = game.screen
        self.map = map

        self.fruit = Fruit.FRUIT_LIST[min(7,Fruit.FRUIT_INDEX)]
        Fruit.FRUIT_INDEX += 1

        self.points = 0

        self.image = pygame.image.load(f'images/{self.fruit}.bmp')
        self.rect = self.image.get_rect()
        self.rect.topleft = (360,470)

        self.draw_index = 0

        if self.fruit == 'cherry':
            self.points = 5000
        elif self.fruit =='berry':
            self.points = 1000
        elif self.fruit == 'oran':
            self.points = 1500
        elif self.fruit == 'apple':
            self.points = 3000

    def draw(self):
        self.draw_index +=1
        if self.draw_index < 375:
            self.screen.blit(self.image, self.rect)
        self.draw_index +=1
        if self.draw_index > 500:
            self.draw_index = 0




class Map():

    def __init__(self, game):
        self.zone = pygame.Rect(25, 45, 700, 775)
        self.game = game
        self.screen = game.screen

        self.image = pygame.image.load('images/maze.bmp')


        self.right = self.zone.right
        self.bottom = self.zone.bottom
        self.left = self.zone.left
        self.top = self.zone.top

        self.cell_width = 25
        self.cell_height = 25

        self.Pellets = pygame.sprite.Group()
        self.PowerPellets = pygame.sprite.Group()

        self.Fruits = pygame.sprite.Group()
        self.fruitTimer = 0
        self.canFruit = True

        self.wall_list = self.setLayout()
        self.tunnel_left = Portal(self.game, self, vector(0,14), vector(26,14), vector(-1,0))
        self.tunnel_left.imageRect.left = self.tunnel_left.imageRect.left
        self.tunnel_right = Portal(self.game, self, vector(27,14), vector(1,14), vector(1,0))
        self.tunnel_right.imageRect.left = self.tunnel_right. imageRect.left - 30
        self.Portals = pygame.sprite.Group()
        self.Portals.add(self.tunnel_left)
        self.Portals.add(self.tunnel_right)

    def setFood(self, x ,y):
        position = vector((x * self.cell_width) + self.left, (y * self.cell_height) + self.top)
        pellet = Pellet(self.game, self, position)
        self.Pellets.add(pellet)

    def setPower(self, x, y):
        position = vector((x * self.cell_width) + self.left, (y * self.cell_height) + self.top)
        powerPellet = PowerPellet(self.game, self, position)
        self.PowerPellets.add(powerPellet)

    def setLayout(self):
        wallList = []
        for foo in range(0,len(map_input)):
            for bar in range(0,len(map_input[foo])):
                if map_input[foo][bar] == 2:
                    wallList.append(vector(bar,foo))
                if map_input[foo][bar] == 1:
                    self.setFood(bar, foo)
                if map_input[foo][bar] == 3:
                    self.setPower(bar, foo)
        return wallList


    def draw_portals(self):
        pygame.draw.rect(self.screen, (0,0,0), self.tunnel_left.imageRect)
        pygame.draw.rect(self.screen,(0,0,0), self.tunnel_right.imageRect)


    def update(self):
        self.screen.blit(self.image, self.zone)
        self.fruitTimer +=1

        if self.fruitTimer >= 1000:
            if self.canFruit == True:
                self.Fruits.add(Fruit(self.game, self))
                self.canFruit = False
                self.fruitTimer = 0
        for pellet in self.Pellets.sprites():
            pellet.draw()
        for powerPellet in self.PowerPellets.sprites():
            powerPellet.draw()
        for fruit in self.Fruits.sprites():
            fruit.draw()











map_input = [   [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                [2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
                [2,1,2,2,2,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,2,2,2,1,2],
                [2,3,2,0,0,2,1,2,0,0,0,2,1,2,2,1,2,0,0,0,2,1,2,0,0,2,3,2],
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
                [4,0,0,0,0,0,1,1,1,0,2,0,0,0,0,0,0,2,0,1,1,1,0,0,0,0,0,4],
                [2,2,2,2,2,2,1,2,2,0,2,0,0,0,0,0,0,2,0,2,2,1,2,2,2,2,2,2],
                [0,0,0,0,0,2,1,2,2,0,2,2,2,2,2,2,2,2,0,2,2,1,2,0,0,0,0,0],
                [0,0,0,0,0,2,1,2,2,0,0,0,0,0,0,0,0,0,0,2,2,1,2,0,0,0,0,0],
                [0,0,0,0,0,2,1,2,2,0,2,2,2,2,2,2,2,2,0,2,2,1,2,0,0,0,0,0],
                [2,2,2,2,2,2,1,2,2,0,2,2,2,2,2,2,2,2,0,2,2,1,2,2,2,2,2,2],
                [2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
                [2,1,2,2,2,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,2,2,2,1,2],
                [2,1,2,2,2,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,2,2,2,1,2],
                [2,3,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,3,2],
                [2,2,2,1,2,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,1,2,2,2],
                [2,2,2,1,2,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,1,2,2,2],
                [2,1,1,1,1,1,1,2,2,1,1,1,1,2,2,1,1,1,1,2,2,1,1,1,1,1,1,2],
                [2,1,2,2,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,2,2,2,2,2,2,1,2],
                [2,1,2,2,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,2,2,2,2,2,2,1,2],
                [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]   ]
