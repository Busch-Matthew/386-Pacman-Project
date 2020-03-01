import pygame
import pygame.math
vector = pygame.math.Vector2
from pygame.sprite import Sprite

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

        self.image = pygame.image.load(f'images/PacManRight.bmp')
        self.image = pygame.transform.scale(self.image, (25, 25))

        self.rect = self.image.get_rect()
        self.rect.topleft = self.position

        self.current_dirrection = vector(0,0)
        self.next_dirrection = vector(0,0)

        self.intersection_list = intersectionList

        self.can_move = True


        #print(self.coordinate)
        #print(self.position)
        #print(self.wall_list)

    def check_wall(self):
        for foo in range(0,len(self.wall_list)):
            if self.wall_list[foo] == vector(self.coordinate + self.current_dirrection):
                return False
        return True

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def change_direction(self, direction):
        self.next_dirrection =  vector(direction)

    def move(self):

        if self.can_move:

            self.position +=  .5 * self.current_dirrection

        self.rect.topleft = self.position
        self.coordinate = (int((self.position.x - self.map.left)/ 25), int((self.position.y - self.map.top )/ 25))
        if self.current_dirrection == vector(0,0):
            self.current_dirrection = self.next_dirrection
        if self.next_dirrection == -1 * self.current_dirrection:
            self.current_dirrection = self.next_dirrection
        if ((self.position.x - self.map.left) % 25  == 0) and self.current_dirrection in [vector(1,0), vector(-1,0)]:
            if self.next_dirrection != vector(0,0) and self.coordinate in self.intersection_list :
                self.current_dirrection = self.next_dirrection
            self.can_move = self.check_wall()
        if ((self.position.y - self.map.top) % 25  == 0) and self.current_dirrection in [vector(0,1), vector(0,-1)]:
            if self.next_dirrection != vector(0,0) and self.coordinate in self.intersection_list:
                self.current_dirrection = self.next_dirrection
            self.can_move = self.check_wall()




    def update(self):
        self.move()
        self.draw()

        #print(self.coordinate)

intersectionList =[ vector(1,1), vector(1,5), vector(1,8), vector(6,1), vector(6,5), vector(6,8), vector(12,1), vector(12,5),
                    vector(21,1), vector(21,5), vector(21,8), vector(26,1), vector(26,5), vector(26,8), vector(15,1), vector(15,5),
                    vector(9,5), vector(18,5),
                    vector(9,8), vector(12,8), vector(15,8), vector(18,8), vector(9,11), vector(12,11), vector(15,11), vector(18,11),
                    vector(6,14), vector(9,14), vector(18, 14), vector(21,14), vector(9,17), vector(18,17), vector(1,20), vector(6,20), vector(9,20),
                    vector(12,20), vector(15,20),vector(18,20), vector(21,20), vector(26,20), vector(1,23), vector(3,23), vector(6,23),vector(9,23), vector(12,23),
                    vector(15,23), vector(18,23), vector(21,23), vector(24,23), vector(26,23), vector(1,26), vector(3,26), vector(6,26), vector(9,26), vector(12,26),
                    vector(15,26), vector(18,26), vector(21,26), vector(24,26), vector(26,26), vector(1,29), vector(12,29), vector(15,29), vector(26,29)]
