from pygame import Surface
from pygame.sprite import Sprite

from dino_runner.utils.constants import BIRD, SCREEN_WIDTH #import completo

class Obstacle(Sprite): #nuestra clase hereda de la clase Sprite -> CHija(CPadre):
    def __init__(self, images, type):
        self.images = images
        self.type = type
        self.rect = self.images[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width: #tiene que recorrer el ancho de la imagen
            obstacles.pop()
    
    def draw(self, screen):
        screen.blit(self.images[self.type], self.rect) #self.rect.x, self.rect.y)
