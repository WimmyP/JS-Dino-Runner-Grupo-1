from random import randint
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self):
        self.image = BIRD[1]
        super().__init__(BIRD, 1)
        self.rect.y = 275

    

