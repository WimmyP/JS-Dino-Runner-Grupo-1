import pygame
import random
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

from .cactus import Cactus


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        cactus_type = random.randint(0,1)
        if len(self.obstacles) == 0:
            if cactus_type == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            else:
                self.obstacles.append(Cactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False 
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
