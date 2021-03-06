import pygame
import pygame.math
vector = pygame.math.Vector2
from pygame.sprite import Sprite
from map_attributes import Portal

class Bullet():
    ORANGE_LOACTION = None
    ORANGE_EXIT_DIR =  None
    ORANGE_COLOR = (255,69,0)
    BLUE_LOCATION = None
    BLUE_EXIT_DIR = None
    BLUE_COLOR = (0,0,255)
    def __init__ (self, game, pac, color):
        self.game = game
        self.map = game.map
        self.screen = game.screen
        self.position = vector(pac.position)
        self.current_dirrection = vector(pac.current_dirrection)
        self.coordinate = self.coordinate = (int((self.position.x - self.map.left)/ 25), int((self.position.y - self.map.top )/ 25))
        self.spawnedPortal = False
        self.tag = color
        for portal in self.map.Portals.sprites():
            if self.tag == portal.tag:
                self.map.Portals.remove(portal)
        if color == 'O':
            self.color = Bullet.ORANGE_COLOR
            Bullet.ORANGE_EXIT_DIR = -1 * self.current_dirrection
        elif color == 'B':
            self.color = Bullet.BLUE_COLOR
            Bullet.BLUE_EXIT_DIR = -1 * self.current_dirrection

    def move(self):
        self.position +=  self.current_dirrection
        #self.rect.topleft = self.position
        self.coordinate = (int((self.position.x - self.map.left)/ 25), int((self.position.y - self.map.top )/ 25))

    def draw(self):
        pygame.draw.circle(self.screen, self.color,(int(self.position.x + 13),int(self.position.y + 13)) , 2)

    def check_wall(self):
        if self.coordinate in self.map.wall_list:
                if self.spawnedPortal == False:
                    self.map.Portals.add(Portal(self.game, self.map, self.coordinate - vector(self.current_dirrection), vector(1,1), vector(-1* self.current_dirrection), tag = self.tag))
                    self.spawnedPortal = True
                    self.current_dirrection = vector(0,0)

    def update(self):
        self.move()
        self.draw()
        self.check_wall()

class Character(Sprite):

    def __init__(self, game, startX, startY):
        super().__init__()

        self.game = game
        self.screen = self.game.screen
        self.map = self.game.map
        self.wall_list = self.map.wall_list
        #adding walls for pacman at ghost spawn
        self.wall_list.append(vector(13,12))
        self.wall_list.append(vector(14,12))


        self.coordinate = vector(startX, startY)
        self.position = vector((startX * self.map.cell_width) + self.map.left, (startY * self.map.cell_height) + self.map.top)

        self.startPosition = self.position
        self.startCoordinate = self.coordinate
        self.image = pygame.image.load(f'images/PacManRight.bmp')
        self.image = pygame.transform.scale(self.image, (25, 25))

        self.rect = self.image.get_rect()
        self.rect.topleft = self.position

        self.current_dirrection = vector(0,0)
        self.next_dirrection = vector(0,0)

        self.intersection_list = intersectionList

        self.imagesRegular = []
        self.imagesDeath = []
        self.can_move = True

        self.steps = 0
        self.direction_value = 0
        self.imageCounter = 0
        self.lives = 3
        self.dead = False
        self.animation_counter = 0
        self.still = False

        self.bulletList = []
        #print(self.coordinate)
        #print(self.position)
        #print(self.wall_list)
        self.load_images()




    def load_images(self):
        self.imagesRegular.append( [pygame.image.load(f'images/pac-neutral.bmp'), pygame.image.load(f'images/pac-left-2.bmp'),pygame.image.load(f'images/pac-left-3.bmp'), pygame.image.load(f'images/pac-left-2.bmp')])
        self.imagesRegular.append( [pygame.image.load(f'images/pac-neutral.bmp'), pygame.image.load(f'images/pac-right-2.bmp'),pygame.image.load(f'images/pac-right-3.bmp'), pygame.image.load(f'images/pac-right-2.bmp')])
        self.imagesRegular.append( [pygame.image.load(f'images/pac-neutral.bmp'), pygame.image.load(f'images/pac-up-2.bmp'),pygame.image.load(f'images/pac-up-3.bmp'), pygame.image.load(f'images/pac-up-2.bmp')])
        self.imagesRegular.append( [pygame.image.load(f'images/pac-neutral.bmp'), pygame.image.load(f'images/pac-down-2.bmp'),pygame.image.load(f'images/pac-down-3.bmp'), pygame.image.load(f'images/pac-down-2.bmp')])

        self.imagesDeath.append(pygame.image.load(f'images/death-1.bmp'))
        self.imagesDeath.append(pygame.image.load(f'images/death-2.bmp'))
        self.imagesDeath.append(pygame.image.load(f'images/death-3.bmp'))
        self.imagesDeath.append(pygame.image.load(f'images/death-4.bmp'))
        self.imagesDeath.append(pygame.image.load(f'images/death-5.bmp'))
        self.imagesDeath.append(pygame.image.load(f'images/death-6.bmp'))
        self.imagesDeath.append(pygame.image.load(f'images/death-7.bmp'))
        self.imagesDeath.append(pygame.image.load(f'images/death-8.bmp'))
        self.imagesDeath.append(pygame.image.load(f'images/death-9.bmp'))
        self.imagesDeath.append(pygame.image.load(f'images/death-10.bmp'))
        self.imagesDeath.append(pygame.image.load(f'images/death-11.bmp'))


    def check_wall(self):
        for foo in range(0,len(self.wall_list)):
            if self.wall_list[foo] == vector(self.coordinate + self.current_dirrection):
                return False
        return True

    def reset(self):
        
        self.current_dirrection = vector(0,0)

        self.position = vector(self.startPosition)
        self.coordinate = vector(self.startCoordinate)

    def draw(self):
        #self.screen.blit(self.image, self.rect)
        if self.dead == True:
            print(self.animation_counter)
            image_selection = int(self.animation_counter / 100)
            self.screen.blit(self.imagesDeath[image_selection], self.rect)
            self.animation_counter += 1
            if self.animation_counter > 1099:
                self.game.finished = True
        else:
            self.screen.blit(self.imagesRegular[self.direction_value][self.imageCounter], self.rect)

        #self.screen.blit(self.imagesRegular[0][0], self.rect)

    def change_direction(self, direction):
        self.next_dirrection =  vector(direction)

    def move(self):
        if self.still:
            return
        if self.can_move:

            self.position +=  self.current_dirrection

        self.rect.topleft = self.position
        self.coordinate = (int((self.position.x - self.map.left)/ 25), int((self.position.y - self.map.top )/ 25))
        if self.current_dirrection == vector(0,0):
            self.current_dirrection = self.next_dirrection
        if self.next_dirrection == -1 * self.current_dirrection:
            self.current_dirrection = self.next_dirrection
        if ((self.position.x - self.map.left) % 25  == 0) and self.current_dirrection in [vector(1,0), vector(-1,0)]:
            if self.imageCounter >= 3:
                self.imageCounter = 0
            else:
                self.imageCounter  +=1
            if self.next_dirrection != vector(0,0) and self.coordinate in self.intersection_list :
                self.current_dirrection = self.next_dirrection
            self.can_move = self.check_wall()
        if ((self.position.y - self.map.top) % 25  == 0) and self.current_dirrection in [vector(0,1), vector(0,-1)]:
            if self.imageCounter >=3:
                self.imageCounter = 0
            else:
                self.imageCounter +=1
            if self.next_dirrection != vector(0,0) and self.coordinate in self.intersection_list:
                self.current_dirrection = self.next_dirrection
            self.can_move = self.check_wall()

        if self.current_dirrection == vector(1,0):
            self.direction_value = 1
        if self.current_dirrection == vector(-1,0):
            self.direction_value = 0
        if self.current_dirrection == vector(0,-1):
            self.direction_value = 2
        if self.current_dirrection == vector(0,1):
            self.direction_value = 3

    def teleport(self, portal):
        if portal.exit_location != None:
            self.position = portal.exit_location
            self.current_dirrection = portal.exit_velocity
        for portal in self.map.Portals.sprites():
            if portal.tag != None:
                self.map.Portals.remove(portal)
    def fire(self,color):
        self.bulletList.append(Bullet(self.game, self, color))

    def update(self):
        self.move()
        self.draw()
        for i in range(0,len(self.bulletList)):
            self.bulletList[i].update()
            if self.bulletList[i].spawnedPortal == True:
                del self.bulletList[i]




        #print(self.coordinate)

intersectionList =[ vector(1,1), vector(1,5), vector(1,8), vector(6,1), vector(6,5), vector(6,8), vector(12,1), vector(12,5),
                    vector(21,1), vector(21,5), vector(21,8), vector(26,1), vector(26,5), vector(26,8), vector(15,1), vector(15,5),
                    vector(9,5), vector(18,5),
                    vector(9,8), vector(12,8), vector(15,8), vector(18,8), vector(9,11), vector(12,11), vector(15,11), vector(18,11),
                    vector(6,14), vector(9,14), vector(18, 14), vector(21,14), vector(9,17), vector(18,17), vector(1,20), vector(6,20), vector(9,20),
                    vector(12,20), vector(15,20),vector(18,20), vector(21,20), vector(26,20), vector(1,23), vector(3,23), vector(6,23),vector(9,23), vector(12,23),
                    vector(15,23), vector(18,23), vector(21,23), vector(24,23), vector(26,23), vector(1,26), vector(3,26), vector(6,26), vector(9,26), vector(12,26),
                    vector(15,26), vector(18,26), vector(21,26), vector(24,26), vector(26,26), vector(1,29), vector(12,29), vector(15,29), vector(26,29)]
