import pygame
from pygame.locals import *
from map_attributes import Map
from character import Character
vector = pygame.math.Vector2
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
        print(self.map.wall_list)
        self.map.create_grid()
        self.player = Character(self, 1, 2)


    def limit_on_screen(self, rect):
        rect.left = max(0, rect.left)
        rect.right = min(rect.right, self.WINDOW_WIDTH)
        rect.top = max(0, rect.top)
        rect.bottom = min(rect.bottom, self.WINDOW_WIDTH)

    def update(self):
        self.screen.fill(self.background_color)
        #self.node.update()
        self.map.update()
        self.player.update()





    def check_for_events(self):
        for event in pygame.event.get():
            e_type = event.type
            if e_type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #self.player.current_dirrection = "LEFT"
                    print('left')
                    self.player.change_direction(vector(-1,0))
                if event.key == pygame.K_RIGHT:
                    #self.player.current_dirrection = "RIGHT"
                    self.player.change_direction(vector(1,0))
                if event.key == pygame.K_UP:
                    #self.player.current_dirrection = "UP"
                    self.player.change_direction(vector(0,-1))
                if event.key == pygame.K_DOWN:
                    #self.player.current_dirrection = "DOWN"
                    self.player.change_direction(vector(0,1 ))
            elif e_type == QUIT:
                self.finished = True


    def run(self):
        while not self.finished:
            self.check_for_events()
        #    self.check_on_map()
            self.update()
            pygame.display.update()
            #print(self.player.current_dirrection)
