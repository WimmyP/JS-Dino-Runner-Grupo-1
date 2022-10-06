import random
from .obstacle import Obstacle #import relativo -> when it's on the same file


class Cactus(Obstacle):
    def __init__(self, images, pos_y):
        type = random.randint(0, 2)
        super().__init__(images, type) #cuando usamos la CP, y luego al metodo -> pasamos datos
        self.rect.y = pos_y #un poco por debajo del dinosaurio, por que es mas pequenio
