import pygame
import pygame.math
vector = pygame.math.Vector2
from pygame.sprite import Sprite


class Node():

    def __init__(self, position, prevNode = None):

        self.position = vector(position)
        self.previous = prevNode



class Enemy(Sprite):

    POINT_VAL = 100

    def __init__(self, game, startX, startY, spawnTime = 0):
        super().__init__()

        self.game = game
        self.screen = self.game.screen
        self.map = self.game.map
        self.wall_list = self.map.wall_list
        self.coordinate = vector(startX, startY)
        self.position = vector((startX * self.map.cell_width) + self.map.left, (startY * self.map.cell_height) + self.map.top)
        self.startPosition = vector(self.position)
        self.startCoordinate = vector(self.coordinate)
        self.color = 'red'
        self.image = pygame.image.load(f'images/red-right-reg-1.bmp')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.spawntimer = spawnTime
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        self.intersection_list = intersectionList
        self.current_dirrection = vector(0,0)




        self.can_move = True
        self.chasing = False
        self.shopping = False
        self.spawning = True
        self.fleeing = False
        self.respawning = False
        self.exiting = False
        self.entering = False
        self.portaling = False
        self.still = False

        self.corner = vector(23,29)
        self.defaultSpawnTimer = spawnTime
        self.steps = 0
        self.fleeing_counter = 40
        self.fleeing_image_counter = 0
        self.imageCounter = 0
        self.imagesRegular = []
        self.imagesFleeing = []
        self.imagesEyes = []


        self.direction_value = 0

    def load_images(self):
        self.imagesRegular.append( [pygame.image.load(f'images/{self.color}-left-reg-1.bmp'), pygame.image.load(f'images/{self.color}-left-reg-2.bmp')])
        self.imagesRegular.append( [pygame.image.load(f'images/{self.color}-right-reg-1.bmp'), pygame.image.load(f'images/{self.color}-right-reg-2.bmp')])
        self.imagesRegular.append( [pygame.image.load(f'images/{self.color}-up-reg-1.bmp'), pygame.image.load(f'images/{self.color}-up-reg-2.bmp')])
        self.imagesRegular.append( [pygame.image.load(f'images/{self.color}-down-reg-1.bmp'), pygame.image.load(f'images/{self.color}-down-reg-2.bmp')])

        self.imagesEyes.append(pygame.image.load('images/eyes-left.bmp'))
        self.imagesEyes.append(pygame.image.load('images/eyes-right.bmp'))
        self.imagesEyes.append(pygame.image.load('images/eyes-up.bmp'))
        self.imagesEyes.append(pygame.image.load('images/eyes-down.bmp'))

        self.imagesFleeing.append([pygame.image.load('images/fleeing-blue-1.bmp'), pygame.image.load('images/fleeing-blue-2.bmp')])
        self.imagesFleeing.append([pygame.image.load('images/fleeing-gray-1.bmp'), pygame.image.load('images/fleeing-gray-2.bmp')])

    def check_wall(self):
        for foo in range(0,len(self.wall_list)):
            if self.wall_list[foo] == vector(self.coordinate + self.current_dirrection):
                return False
        return True

    def draw(self):
        if self.fleeing:
            self.screen.blit(self.imagesFleeing[self.fleeing_image_counter][self.imageCounter], self.rect)
        elif self.respawning or self.entering:
            self.screen.blit(self.imagesEyes[self.direction_value],self.rect)
        else:
            self.screen.blit(self.imagesRegular[self.direction_value][self.imageCounter], self.rect)

    def reset(self):
        self.can_move = True
        self.chasing = False
        self.shopping = False
        self.spawning = True
        self.fleeing = False
        self.respawning = False
        self.exiting = False
        self.still = False
        self.entering = False
        self.portaling = False
        self.spawntimer = self.defaultSpawnTimer
        self.current_dirrection = vector(0,0)

        self.position = vector(self.startPosition)
        self.coordinate = vector(self.startCoordinate)

        self.steps = 0
        self.fleeing_counter = 40
        self.fleeing_image_counter = 0
        self.direction_value = 0

    def chase(self, pac_pos):
        goal = vector(pac_pos)
        if goal != self.coordinate:
            visited = [vector(self.coordinate - self.current_dirrection), vector(self.coordinate)]
            queue = []
            queue.append(Node(self.coordinate))
            searchPosition = vector(self.coordinate)
            count = 0
            move_list = []

            while queue != []:
                node = queue.pop(0)


                if node.position == vector(goal):
                    while node.previous.previous != None:
                        move_list.append(vector(node.position))
                        node = node.previous
                    break


                if vector(node.position + vector(1,0)) not in self.wall_list:
                    if vector(node.position + vector(1,0)) not in visited:
                        queue.append(Node(vector(node.position + vector(1,0)),node))
                        visited.append(vector(node.position + vector(1,0)))
                if vector(node.position - vector(1,0)) not in self.wall_list:
                    if vector(node.position - vector(1,0)) not in visited:
                        queue.append(Node(vector(node.position + vector(-1,0)),node))
                        visited.append(vector(node.position + vector(-1,0)))
                if vector(node.position + vector(0,1)) not in self.wall_list:
                    if vector(node.position + vector(0,1)) not in visited:
                        queue.append(Node(vector(node.position + vector(0,1)),node))
                        visited.append(vector(node.position + vector(0,1)))
                if vector(node.position - vector(0,1)) not in self.wall_list:
                    if vector(node.position - vector(0,1)) not in visited:
                        queue.append(Node(vector(node.position - vector(0,1)),node))
                        visited.append(vector(node.position - vector(0,1)))

            if move_list != []:
                self.current_dirrection = .5 * vector(move_list.pop() - self.coordinate)
        else:
            self.current_dirrection = vector(0,0)

    def shop(self):
        goal = self.corner
        if goal != self.coordinate:
            visited = [vector(self.coordinate - self.current_dirrection), vector(self.coordinate)]
            queue = []
            queue.append(Node(self.coordinate))
            searchPosition = vector(self.coordinate)
            count = 0
            move_list = []

            while queue != []:
                node = queue.pop(0)


                if node.position == vector(goal):
                    while node.previous.previous != None:
                        move_list.append(vector(node.position))
                        node = node.previous
                    break


                if vector(node.position + vector(1,0)) not in self.wall_list:
                    if vector(node.position + vector(1,0)) not in visited:
                        queue.append(Node(vector(node.position + vector(1,0)),node))
                        visited.append(vector(node.position + vector(1,0)))
                if vector(node.position - vector(1,0)) not in self.wall_list:
                    if vector(node.position - vector(1,0)) not in visited:
                        queue.append(Node(vector(node.position + vector(-1,0)),node))
                        visited.append(vector(node.position + vector(-1,0)))
                if vector(node.position + vector(0,1)) not in self.wall_list:
                    if vector(node.position + vector(0,1)) not in visited:
                        queue.append(Node(vector(node.position + vector(0,1)),node))
                        visited.append(vector(node.position + vector(0,1)))
                if vector(node.position - vector(0,1)) not in self.wall_list:
                    if vector(node.position - vector(0,1)) not in visited:
                        queue.append(Node(vector(node.position - vector(0,1)),node))
                        visited.append(vector(node.position - vector(0,1)))

            if move_list != []:
                self.current_dirrection = .5 * vector(move_list.pop() - self.coordinate)

    def spawn(self):
        if self.check_wall() == False:
            self.current_dirrection = self.current_dirrection * -1
        self.spawntimer -= 1
        if self.spawntimer <= 0:
            self.steps = 0
            self.spawning = False
            self.exiting = True
            self.current_dirrection = vector(0,-1)

    def start_fleeing(self):

        Enemy.POINT_VAL = 100
        if self.chasing or self.shopping:
            self.chasing = False
            self.shopping = False
            self.current_dirrection = -1 * self.current_dirrection
            self.fleeing = True
            self.fleeing_image_counter = 0

    def flee(self):


        visited = [vector(self.coordinate - self.current_dirrection), vector(self.coordinate)]
        queue = []
        queue.append(Node(self.coordinate))
        searchPosition = vector(self.coordinate)
        count = 0
        move_list = []
        counter = 0
        while queue != []:
            node = queue.pop(0)

            if counter >= 8:
                while node.previous.previous != None:
                    move_list.append(vector(node.position))
                    node = node.previous
                break


            if vector(node.position + vector(1,0)) not in self.wall_list:
                if vector(node.position + vector(1,0)) not in visited:
                    queue.append(Node(vector(node.position + vector(1,0)),node))
                    visited.append(vector(node.position + vector(1,0)))
            if vector(node.position - vector(1,0)) not in self.wall_list:
                if vector(node.position - vector(1,0)) not in visited:
                    queue.append(Node(vector(node.position + vector(-1,0)),node))
                    visited.append(vector(node.position + vector(-1,0)))
            if vector(node.position + vector(0,1)) not in self.wall_list:
                if vector(node.position + vector(0,1)) not in visited:
                    queue.append(Node(vector(node.position + vector(0,1)),node))
                    visited.append(vector(node.position + vector(0,1)))
            if vector(node.position - vector(0,1)) not in self.wall_list:
                if vector(node.position - vector(0,1)) not in visited:
                    queue.append(Node(vector(node.position - vector(0,1)),node))
                    visited.append(vector(node.position - vector(0,1)))
            counter +=1
        if move_list != []:
            self.current_dirrection = .25 * (vector(move_list.pop() - self.coordinate))

        if self.fleeing_counter <= 0:
            self.shopping = True
            self.fleeing = False
            self.fleeing_counter = 40

    def start_respawning(self):
        Enemy.POINT_VAL = Enemy.POINT_VAL * 2
        self.fleeing = False
        self.respawning = True
        self.fleeing_counter = 40

    def respawn(self):
            goal = vector(13,11)
            goal2 = vector(14,11)
            if goal != self.coordinate and goal2 != self.coordinate:
                visited = [vector(self.coordinate - self.current_dirrection), vector(self.coordinate)]
                queue = []
                queue.append(Node(self.coordinate))
                searchPosition = vector(self.coordinate)
                count = 0
                move_list = []

                while queue != []:
                    node = queue.pop(0)


                    if node.position == vector(goal):
                        while node.previous.previous != None:
                            move_list.append(vector(node.position))
                            node = node.previous
                        break

                    if vector(node.position + vector(0,1)) not in self.wall_list:
                        if vector(node.position + vector(0,1)) not in visited:
                            queue.append(Node(vector(node.position + vector(0,1)),node))
                            visited.append(vector(node.position + vector(0,1)))
                    if vector(node.position + vector(1,0)) not in self.wall_list:
                        if vector(node.position + vector(1,0)) not in visited:
                            queue.append(Node(vector(node.position + vector(1,0)),node))
                            visited.append(vector(node.position + vector(1,0)))
                    if vector(node.position - vector(1,0)) not in self.wall_list:
                        if vector(node.position - vector(1,0)) not in visited:
                            queue.append(Node(vector(node.position + vector(-1,0)),node))
                            visited.append(vector(node.position + vector(-1,0)))
                    if vector(node.position - vector(0,1)) not in self.wall_list:
                        if vector(node.position - vector(0,1)) not in visited:
                            queue.append(Node(vector(node.position - vector(0,1)),node))
                            visited.append(vector(node.position - vector(0,1)))


                if move_list != []:
                    self.current_dirrection =  vector(move_list.pop() - self.coordinate)
            else:
                self.respawning = False
                self.entering = True
                self.current_dirrection = vector(0,1)


    def check_wall(self):
        for foo in range(0,len(self.wall_list)):
            if self.wall_list[foo] == vector(self.coordinate + self.current_dirrection):
                return False
        return True

    def move(self, pac_pos):
        if self.still:
            return
        if self.exiting is True:
            if self.position.y == 320:
                self.exiting = False
                self.shopping = True
                self.current_dirrection = vector(1,0)
        elif self.entering is True:
            if self.position.y == 385:
                self.exiting = True
                self.entering = False
                self.current_dirrection = vector(0,-1)
        else:
            if ((self.position.x - self.map.left) % 25  == 0) and ((self.position.y - self.map.top) % 25  == 0):
                if self.imageCounter == 1:
                    self.imageCounter = 0
                else:
                    self.imageCounter = 1
                if self.fleeing == True:
                    self.fleeing_counter -= 1
                    if self.fleeing_counter < 12:
                        if self.fleeing_image_counter == 1:
                            self.fleeing_image_counter = 0
                        else:
                            self.fleeing_image_counter = 1
                else:
                    if self.fleeing == False:
                        self.steps += 1
                    if self.steps > 75:
                        if self.shopping == True:
                            self.swap_modes()
                    if self.steps > 100:
                        if self.chasing == True:
                            self.swap_modes()
                    if self.spawning == True:
                        self.spawn()
                    if self.respawning == True:
                        self.respawn()


                if self.coordinate in self.intersection_list:
                    if self.chasing == True:
                        self.chase(pac_pos)

                    elif self.shopping == True:
                        self.shop()

                    elif self.spawning == True:
                        self.spawn()
                    elif self.fleeing == True:
                        self.flee()


        if self.can_move:
            if self.current_dirrection == vector(1,0):
                self.direction_value = 1
            if self.current_dirrection == vector(-1,0):
                self.direction_value = 0
            if self.current_dirrection == vector(0,-1):
                self.direction_value = 2
            if self.current_dirrection == vector(0,1):
                self.direction_value = 3
            self.position +=  self.current_dirrection
            self.rect.topleft = self.position
            self.coordinate = (int((self.position.x - self.map.left)/ 25), int((self.position.y - self.map.top )/ 25))

    def swap_modes(self):
        self.steps = 0
        if self.chasing is True:
            self.chasing = False
            self.shopping = True
            self.current_dirrection = self.current_dirrection * -1
            return
        if self.shopping is True:
            self.shopping = False
            self.chasing = True
            self.current_dirrection = self.current_dirrection * -1
            return

    def update(self, pac_pos):
        self.move(pac_pos)
        self.draw()


intersectionList =[ vector(1,1), vector(1,5), vector(1,8), vector(6,1), vector(6,5), vector(6,8), vector(12,1), vector(12,5),
                    vector(21,1), vector(21,5), vector(21,8), vector(26,1), vector(26,5), vector(26,8), vector(15,1), vector(15,5),
                    vector(9,5), vector(18,5), vector(9,8), vector(12,8), vector(15,8), vector(18,8), vector(9,11), vector(12,11), vector(15,11),    vector(18,11),
                    vector(6,14), vector(9,14), vector(11,14),vector(12,14), vector(13,14), vector(14,14),vector(15,14),vector(16,14),
                    vector(18, 14), vector(21,14), vector(9,17), vector(18,17), vector(1,20), vector(6,20), vector(9,20),
                    vector(12,20), vector(15,20),vector(18,20), vector(21,20), vector(26,20), vector(1,23), vector(3,23), vector(6,23), vector(9,23), vector(12,23),
                    vector(15,23), vector(18,23), vector(21,23), vector(24,23), vector(26,23), vector(1,26), vector(3,26), vector(6,26), vector(9,26), vector(12,26),
                    vector(15,26), vector(18,26), vector(21,26), vector(24,26), vector(26,26), vector(1,29), vector(12,29), vector(15,29), vector(26,29)]
