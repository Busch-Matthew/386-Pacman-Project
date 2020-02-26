import pygame
from pygame.locals import *
from map_attributes import Map

import time

class Game():

    MOVE_SPEED = 2
    WINDOW_HEIGHT = 1000
    WINDOW_WIDTH = 1000
    MAZE_WIDTH = 600
    MAZE_HEIGHT = 800
    LIVES = 3

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT))
        pygame.display.set_caption('PacMan!')
        self.background_color = (40, 40, 40)
        self.finished = False

        #self.node = Node(self, 500 ,600)
        self.map = Map(self)
        self.map.create_grid()



    def limit_on_screen(self, rect):
        rect.left = max(0, rect.left)
        rect.right = min(rect.right, self.WINDOW_WIDTH)
        rect.top = max(0, rect.top)
        rect.bottom = min(rect.bottom, self.WINDOW_WIDTH)

    def update(self):
        self.screen.fill(self.background_color)
        #self.node.update()
        self.map.update()
       # self.player.update()





    def check_for_events(self):
        for event in pygame.event.get():
            e_type = event.type

            if e_type == QUIT:
                self.finished = True

    def check_on_map(self):
        collision = pygame.sprite.spritecollideany(self.player, self.map.nodes)
        if collision:
            print(collision)
            node = collision
            if self.player.current_dirrection == 'LEFT':
                if not node.left:
                    self.player.velocity = Vector()
            if self.player.current_dirrection == 'RIGHT':
                if not node.right:
                    self.player.velocity = Vector()
            if self.player.current_dirrection == 'UP':
                if not node.up:
                    self.player.velocity = Vector()
            if self.player.current_dirrection == 'DOWN':
                if not node.down:
                    self.player.velocity = Vector()



    def run(self):
        while not self.finished:
            self.check_for_events()
        #    self.check_on_map()
            self.update()
            pygame.display.update()
            #print(self.player.current_dirrection)
