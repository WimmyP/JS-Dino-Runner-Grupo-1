from uuid import RESERVED_FUTURE
import pygame
from dino_runner.components.dino_enemy import DinoEnemy
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.heart_manager import Heart_Manager
from dino_runner.components.powerups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score

from dino_runner.utils.constants import BG, DEFAULT_TYPE, HAMMER_TYPE, ICON, RESET, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD, SHIELD_TYPE, TITLE, FPS, FONT_STYLE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False 
        self.game_speed = 15
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.heart_manager = Heart_Manager()

        # self.enemy = DinoEnemy()

        self.death_count = 0
        self.score = Score()

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.game_speed = 20
        self.draw_background()
        self.obstacle_manager.reset_obstacles()
        self.score.reset_score()
        self.power_up_manager.reset_power_ups()
        self.heart_manager.reset_heart()



    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.power_up_manager.update(self.game_speed, self.player, self.score.score)
        self.score.update(self)

        # self.enemy.update(self.score.score, self.game_speed, self.player, self.on_death)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score.draw(self.draw_message)
        self.draw_power_up_active()
        self.heart_manager.draw(self.screen)

        # self.enemy.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed #usamos el game_speed recorre la imagen 

    def show_menu(self):
        self.screen.fill((255, 255, 255)) #pintar ventana 
        half_screen_heigth = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:  #dar mensaje de bienvenida
            self.draw_message("Press Any Key to Start", half_screen_width, half_screen_heigth, 50)
        else:
            self.draw_message(f"Deaths: {self.death_count}", 1000, 50, 30)
            self.draw_message(f"Last Score: {self.score.score}", 1000, 70, 30)
            self.draw_message("Do You Want to Play Again? ", half_screen_width,half_screen_heigth, 50)

            self.screen.blit(RESET, (half_screen_width - 30, half_screen_heigth +20) )
    
        self.screen.blit(RUNNING[0], (half_screen_width - 30, half_screen_heigth - 140)) #mostrar un icono
        pygame.display.update() #actualizar ventana
        self.handle_key_events_on_menu()  #escuchar eventos 

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if self.death_count >=1:
                    self. reset_game()
                self.run()

    def on_death(self):
        has_power_ups = self.player.type == SHIELD_TYPE or self.player.type == HAMMER_TYPE
        is_invencible = has_power_ups or self.heart_manager.heart_count > 0

        if not has_power_ups:
            self.heart_manager.reduce_heart()
        if not is_invencible:
            pygame.time.delay(500)
            self.playing = False
            self.death_count += 1 
        return is_invencible
    
    def draw_message(self, message, pos_x , pos_y, size):
        font =  pygame.font.SysFont(FONT_STYLE, size)
        text_component = font.render(message, True, (0, 0, 0))
        text_rect = text_component.get_rect()
        text_rect.center = (pos_x, pos_y)
        self.screen.blit(text_component, text_rect)

    def draw_power_up_active(self):
        self.player.has_power_up
        time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000, 2)
        if time_to_show >= 0:
            self.draw_message(f"{self.player.type.capitalize()} enabled for {time_to_show} seconds.", 500, 40,18)
        else:
            self.player.has_power_up = False
            self.player.type = DEFAULT_TYPE

