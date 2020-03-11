import pygame,sys
from pygame.locals import *
vector = pygame.math.Vector2

pygame.font.init()

class Score():

    def __init__(self, game):

        self.game = game
        self.screen = game.screen
        #self.position = vector(position)
        self.score = 0
        self.loaded_score = self.load_highscore()
        self.highscore = self.loaded_score
        self.fonts = pygame.font.get_fonts()

        self.font= pygame.font.SysFont('opensans', 24)
        self.text = self.font.render('High Score:', False, (255,255,255))
        self.textRect = self.text.get_rect()
        self.textRect.topleft = (250,8)
        self.highscoreText = self.font.render(f'{self.highscore}', False, (255,255,255))
        self.highscoreTextRect = self.highscoreText.get_rect()
        self.highscoreTextRect.topleft = (400, 8)
        self.scoreText = self.font.render(f'{self.score}', False, (255,255,255))
        self.scoreTextRect = self.scoreText.get_rect()
        self.scoreTextRect.topleft = (600,8)
        self.lives = self.font.render(f'Lives: {self.game.player.lives}', False, (255,255,255))
        self.livesRect = self.lives.get_rect()
        self.livesRect.topleft = (10,8)
        self.extraLife = False


    def draw(self):

        self.screen.blit(self.text,self.textRect)
        self.screen.blit(self.highscoreText, self.highscoreTextRect)
        self.screen.blit(self.scoreText, self.scoreTextRect)
        self.screen.blit(self.lives, self.livesRect)
    def update(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.highscoreText = self.font.render(f'{self.highscore}', False, (255,255,255))
        self.scoreText = self.font.render(f'{self.score}', False, (255,255,255))
        self.lives = self.font.render(f'Lives: {self.game.player.lives}', False, (255,255,255))
        self.draw()
        if self.extraLife == False and self.score >= 10000:
            self.game.player.lives += 1
            self.extraLife = True





    def load_highscore(self):
        file = open('scores.txt', 'r')
        loaded_score = int(file.readline())
        file.close()
        return loaded_score


    def update_highscore(self):

        if self.highscore > self.loaded_score:
            self.loaded_score = self.highscore
            output_file = open("scores.txt","w")
            output_file.write(str(self.highscore))
            output_file.close()
