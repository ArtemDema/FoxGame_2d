from ..main_classes import Enemy

import pygame

list_idle = ["images/player/idle/0.png", "images/player/idle/1.png", 
             "images/player/idle/2.png", "images/player/idle/3.png"]

list_run = ["images/player/run/0.png", "images/player/run/1.png", 
            "images/player/run/2.png", "images/player/run/3.png",
            "images/player/run/4.png", "images/player/run/5.png"]

list_jump = ["images/player/jump/player-jump-1.png","images/player/jump/player-jump-2.png",]

list_crouch = ["images/player/crouch/player-crouch-1.png","images/player/crouch/player-crouch-2.png"]

class Hero(Enemy):
    def __init__(self, x, y, width, height, image, hp, speed, strength_jump):
        self.strength_jump = strength_jump
        super().__init__(x, y, width, height, image, hp, speed)
        
    def idle(self, idle_count, screen, last_side):
        if last_side == 0:
            self.image = list_idle[idle_count]
            self.load_image()
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            self.image = list_idle[idle_count]
            self.load_image()
            self.draw_image(screen)

    def run(self, run_count, screen, last_side):
        if last_side == 0:
            self.image = list_run[run_count]
            self.load_image()
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            self.image = list_run[run_count]
            self.load_image()
            self.draw_image(screen)

    def jump(self, screen, last_side):
        if last_side == 0:
            self.image = list_jump[0]
            self.load_image()
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            self.image = list_jump[0]
            self.load_image()
            self.draw_image(screen)

    def fall(self, screen, last_side):
        if last_side == 0:
            self.image = list_jump[1]
            self.load_image()
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            self.image = list_jump[1]
            self.load_image()
            self.draw_image(screen)

    def crouch(self, crouch_count, screen, last_side):
        if last_side == 0:
            self.image = list_crouch[crouch_count]
            self.load_image()
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            self.image = list_crouch[crouch_count]
            self.load_image()
            self.draw_image(screen)

player = Hero(x = 600, y = 400, width = 80, height = 80, image=list_idle[0], hp = 3, speed = 4, strength_jump = 17)