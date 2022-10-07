import pygame

from dino_runner.utils.constants import FONT_STYLE


class Score:
    def __init__(self):
        self.score = 0

    def update(self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2

    def draw(self, draw_message):
        draw_message(f"Points: {self.score}", 1000, 50, 22)

    def reset_score(self):
        self.score = 0
