from random import randint
import pygame
from pygame.sprite import Sprite
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.constants import DEFAULT_TYPE, RUNNING, RUNNING_SHIELD, SHIELD_TYPE

THROW_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}

class DinoEnemy(Sprite):  #tira nubes cada tiempo random 
    X_POS = 1000
    Y_POS = 310
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = THROW_IMG[self.type][0]
        self.enemy_rect = self.image.get_rect()
        self.enemy_rect.x = self.X_POS
        self.enemy_rect.y = self.Y_POS
        self.step_index = 0

        self.when_appears = 0
        self.start_time_appear = 0
        self.duration_enemy = randint(10, 20)

        self.obstacle = ObstacleManager()
    
    def appear(self, score):
        if self.when_appears == score:
            self.when_appears += randint(400, 500)

    def throw(self):
        self.image = THROW_IMG[self.type][self.step_index //5]
        self.enemy_rect = self.image.get_rect()
        self.enemy_rect.x = self.X_POS
        self.enemy_rect.y = self.Y_POS

        self.step_index += 1

    def update(self, score, game_speed, player, on_death): 
        self.appear(score)   
        self.start_time_appear = pygame.time.get_ticks()
        self.throw()  

        self.obstacle.update(game_speed, player, on_death)
        
        if self.step_index >= 9:
            self.step_index = 0  

    def draw(self, screen):
        self.obstacle.draw(screen)
        screen.blit(self.image, (self.enemy_rect.x, self.enemy_rect.y))   