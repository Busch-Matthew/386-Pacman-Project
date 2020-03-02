import pygame
from pygame.locals import *
from map_attributes import Map
from pygame.time import Clock
from character import Character

from enemy import Enemy
vector = pygame.math.Vector2


class Game():

    MOVE_SPEED = 2
    WINDOW_HEIGHT = 825
    WINDOW_WIDTH = 750
    LIVES = 3

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT))
        pygame.display.set_caption('PacMan!')
        self.background_color = (40, 40, 40)
        self.finished = False

        self.map = Map(self)
        self.player = Character(self, 13, 17)
        self.red = Enemy(self, 12, 11)
        self.red.corner = vector(23,29)
        self.red.chasing = True
        self.red.spawning = False
        self.yellow = Enemy(self, 14, 14, 25)
        self.yellow.corner = vector(23,1)
        self.yellow.spawning = True
        self.yellow.current_dirrection = vector(-1,0)
        self.blue = Enemy(self, 13,14, 52)
        self.blue.corner = vector(4,29)
        self.blue.current_dirrection = vector(1,0)
        self.pink = Enemy(self, 12, 14,89)
        self.pink.corner = vector(4,1)
        self.pink.current_dirrection = vector(1,0)

        self.Ghosts = pygame.sprite.Group()

        self.Ghosts.add(self.red)
        self.Ghosts.add(self.blue)
        self.Ghosts.add(self.yellow)
        self.Ghosts.add(self.pink)

        self.fps = pygame.time.Clock()


    def limit_on_screen(self, rect):
        rect.left = max(0, rect.left)
        rect.right = min(rect.right, self.WINDOW_WIDTH)
        rect.top = max(0, rect.top)
        rect.bottom = min(rect.bottom, self.WINDOW_WIDTH)

    def update(self):
        #self.screen.fill(self.background_color)

        self.map.update()
        self.player.update()
        self.update_ghosts()
        self.check_collisions()

    def check_collisions(self):
        pellet = pygame.sprite.spritecollideany(self.player, self.map.Pellets)
        self.map.Pellets.remove(pellet)

        if pygame.sprite.spritecollideany(self.player, self.Ghosts):
            print('COLLISION')


    def update_ghosts(self):

        self.red.update(self.player.coordinate)

        self.yellow.update(self.player.coordinate)

        self.blue.update(self.player.coordinate)

        self.pink.update(self.player.coordinate)


    def check_for_events(self):
        for event in pygame.event.get():
            e_type = event.type
            if e_type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #self.player.current_dirrection = "LEFT"
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
            self.fps.tick(200)
            self.check_for_events()
        #    self.check_on_map()
            self.update()
            pygame.display.update()
            #print(self.player.current_dirrection)
