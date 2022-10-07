import pygame
import random

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

from .cactus import Cactus


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, player, on_death): #me falta aniadir el ave
        if len(self.obstacles) == 0:
            obstacle_type = random.randint(0,1)
            if obstacle_type == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS, 320))
            else:
                self.obstacles.append(Cactus(LARGE_CACTUS, 300))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                if on_death():
                    self.obstacles.remove(obstacle)
                else:
                    break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []