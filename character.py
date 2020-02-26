import pygame
import pygame.math
vector = pygame.math.Vector2

class Character():

    def __init__(self, game, startX, startY):
        self.game = game
        self.screen = self.game.screen
        self.map = self.game.map
        self.wall_list = self.map.wall_list
        self.coordinate = vector(startX, startY)
        self.position = vector((startX * self.map.cell_width) + self.map.left, (startY * self.map.cell_height) + self.map.top)

        self.image = pygame.image.load(f'images/PacManRight.png')
        self.image = pygame.transform.scale(self.image, (25, 25))

        self.rect = self.image.get_rect()
        self.rect.topleft = self.position

        self.current_dirrection = vector(0,0)
        self.next_dirrection = vector(0,0)

        self.can_move = True

        print(self.coordinate)
        print(self.position)
        print(self.wall_list)

    def check_wall(self):
        for foo in range(0,len(self.wall_list)):
            if self.wall_list[foo] == vector(self.coordinate + self.current_dirrection):
                return False
        return True

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def change_direction(self, direction):
        self.next_dirrection =  direction

    def move(self):

        if self.can_move:

            self.position +=  .5 * self.current_dirrection

        self.rect.topleft = self.position
        self.coordinate = (int((self.position.x - self.map.left)/ 25), int((self.position.y - self.map.top )/ 25))
        if self.current_dirrection == vector(0,0):
            self.current_dirrection = self.next_dirrection
        if ((self.position.x - self.map.left) % 25  == 0) and self.current_dirrection in [vector(1,0), vector(-1,0)]:

            if self.next_dirrection != vector(0,0):
                self.current_dirrection = self.next_dirrection

            self.can_move = self.check_wall()
        if ((self.position.y - self.map.top) % 25  == 0) and self.current_dirrection in [vector(0,1), vector(0,-1)]:
            if self.next_dirrection != vector(0,0):
                self.current_dirrection = self.next_dirrection
            self.can_move = self.check_wall()



    def update(self):
        self.move()
        self.draw()
        #print(self.coordinate)
