import pygame
from pygame.locals import *
from map_attributes import Map
from pygame.time import Clock
from character import Character
from scoreboard import Score
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
        self.background_color = (0, 0, 0)
        self.finished = False

        self.collisionChecking = True

        self.map = Map(self)
        self.player = Character(self, 13, 17)

        self.red = Enemy(self, 12, 11)
        self.red.corner = vector(23,29)
        self.red.chasing = True
        self.red.spawning = False
        self.red.load_images()

        self.orange = Enemy(self, 14, 14, 42)
        self.orange.corner = vector(23,1)
        self.orange.current_dirrection = vector(-1,0)
        self.orange.color = 'orange'
        self.orange.load_images()

        self.blue = Enemy(self, 13,14, 84)
        self.blue.corner = vector(4,29)
        self.blue.current_dirrection = vector(1,0)
        self.blue.color = 'blue'
        self.blue.load_images()

        self.pink = Enemy(self, 12, 14,135)
        self.pink.corner = vector(4,1)
        self.pink.current_dirrection = vector(1,0)
        self.pink.color = 'pink'
        self.pink.load_images()

        self.Ghosts = pygame.sprite.Group()
        self.Ghosts.add(self.red)
        self.Ghosts.add(self.blue)
        self.Ghosts.add(self.orange)
        self.Ghosts.add(self.pink)

        self.score = Score(self)

        self.fps = pygame.time.Clock()

        self.healthlock = False
    def limit_on_screen(self, rect):
        rect.left = max(0, rect.left)
        rect.right = min(rect.right, self.WINDOW_WIDTH)
        rect.top = max(0, rect.top)
        rect.bottom = min(rect.bottom, self.WINDOW_WIDTH)

    def update(self):
        self.screen.fill(self.background_color)
        self.map.update()
        if self.collisionChecking:
            self.check_collisions()
        self.player.update()
        self.check_collisions()
        self.update_ghosts()
        self.map.draw_portals()
        self.score.update()

    def reset_board(self):
        self.red.reset()
        self.red.chasing = True
        self.red.spawning = False
        self.blue.reset()
        self.blue.current_dirrection = vector(1,0)
        self.pink.reset()
        self.pink.current_dirrection = vector(1,0)
        self.orange.reset()
        self.orange.current_dirrection = vector(-1,0)

        self.healthlock = False
        #self.player.reset()

    def death_animation(self):
        self.player.dead = True
        self.player.still = True
        self.red.still = True
        self.blue.still = True
        self.orange.still = True
        self.pink.still = True
    def stop_checking_collisions(self):
        self.collisionChecking = False

    def check_collisions(self):

        pellet = pygame.sprite.spritecollideany(self.player, self.map.Pellets)
        if pellet != None:
            self.map.Pellets.remove(pellet)
            self.score.score += 10
        fruit = pygame.sprite.spritecollideany(self.player, self.map.Fruits)
        if fruit != None:
            print (fruit.points)
            self.score.score += fruit.points
            self.map.Fruits.remove(fruit)
            self.map.canFruit = True
            self.map.fruitTimer = 0
        powerPellet = pygame.sprite.spritecollideany(self.player, self.map.PowerPellets)

        self.map.PowerPellets.remove(powerPellet)
        if powerPellet != None:
            self.score.score += 50
            for ghost in self.Ghosts:
                ghost.start_fleeing()

        ghost_collision = pygame.sprite.spritecollideany(self.player, self.Ghosts)
        if ghost_collision != None:
            if ghost_collision.fleeing == True:
                ghost_collision.start_respawning()
                self.score.score += ghost_collision.POINT_VAL
            if ghost_collision.fleeing == False and ghost_collision.respawning == False:
                self.player.lives -= 1
                if self.player.lives > 0:
                    self.reset_board()
                else:
                    self.stop_checking_collisions()
                    self.death_animation()
                    self.score.update_highscore()
        portal_collision = pygame.sprite.spritecollideany(self.player, self.map.Portals)
        if portal_collision != None:
            self.player.teleport(portal_collision)
        ghost_left_portal = pygame.sprite.spritecollideany(self.map.tunnel_left, self.Ghosts)


        if ghost_left_portal != None:
            print(ghost_left_portal)
            ghost_left_portal.position.x = 675
        ghost_right_portal = pygame.sprite.spritecollideany(self.map.tunnel_right, self.Ghosts)
        if ghost_right_portal != None:
            print(ghost_right_portal)
            ghost_right_portal.position.x = 50


    def update_ghosts(self):

        self.red.update(self.player.coordinate)

        self.orange.update(self.player.coordinate)

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
