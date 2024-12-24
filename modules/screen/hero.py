from ..main_classes import Enemy
from ..interface import hp

import pygame

list_idle = ["images/player/idle/0.png", "images/player/idle/1.png", 
             "images/player/idle/2.png", "images/player/idle/3.png"]

list_idle_with_chest = ["images/player/idle/with_chest/0.png", "images/player/idle/with_chest/1.png", 
                        "images/player/idle/with_chest/2.png", "images/player/idle/with_chest/3.png"]

list_run = ["images/player/run/0.png", "images/player/run/1.png", 
            "images/player/run/2.png", "images/player/run/3.png",
            "images/player/run/4.png", "images/player/run/5.png"]

list_run_with_chest = ["images/player/run/with_chest/0.png", "images/player/run/with_chest/1.png", 
                        "images/player/run/with_chest/2.png", "images/player/run/with_chest/3.png",
                        "images/player/run/with_chest/4.png", "images/player/run/with_chest/5.png"]

list_jump = ["images/player/jump/player-jump-1.png","images/player/jump/player-jump-2.png",]

list_jump_with_chest = ["images/player/jump/with_chest/0.png",]

list_crouch = ["images/player/crouch/player-crouch-1.png","images/player/crouch/player-crouch-2.png"]


move_left = False
move_right = False
move_bottom = False
move_jump = False
move_crouch = False
hide = False
with_box = False
push_box = False

class Hero(Enemy):
    def __init__(self, x, y, width, height, image, hp, speed, strength_jump):
        self.strength_jump = strength_jump
        self.timer_damage = 0
        super().__init__(x, y, width, height, image, hp, speed)
        
    def idle(self, idle_count, screen, last_side, with_chest): #DRAWING IDLE POSITION
        if last_side == 0:
            if with_chest: self.image = list_idle_with_chest[idle_count]
            else: self.image = list_idle[idle_count]
            self.load_image()
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            if with_chest: self.image = list_idle_with_chest[idle_count]
            else: self.image = list_idle[idle_count]
            self.load_image()
            self.draw_image(screen)

    def run(self, run_count, screen, last_side, with_chest): #DRAWING RUN POSITION
        if last_side == 0:
            if with_chest: self.image = list_run_with_chest[run_count]
            else: self.image = list_run[run_count]
            self.load_image()
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            if with_chest: self.image = list_run_with_chest[run_count]
            else: self.image = list_run[run_count]
            self.load_image()
            self.draw_image(screen)

    def jump(self, screen, last_side): #DRAWING JUMP POSITION
        if last_side == 0:
            self.image = list_jump[0]
            self.load_image()
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            self.image = list_jump[0]
            self.load_image()
            self.draw_image(screen)

    def fall(self, screen, last_side, with_chest): #DRAWING FALL POSITION
        if last_side == 0:
            if with_chest: self.image = list_jump_with_chest[0]
            else: self.image = list_jump[1]
            self.load_image()
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            if with_chest: self.image = list_jump_with_chest[0]
            else: self.image = list_jump[1]
            self.load_image()
            self.draw_image(screen)

    def crouch(self, crouch_count, screen, last_side): #DRAWING CROUCH POSITION
        if last_side == 0:
            self.image = list_crouch[crouch_count]
            self.load_image()
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            self.image = list_crouch[crouch_count]
            self.load_image()
            self.draw_image(screen)
    
    def damage_player(self):
        if self.timer_damage == 0:
            self.hp -= 1
            hp.count -= 1
            self.timer_damage = 360

player = Hero(x = 600, y = 400, width = 80, height = 80, image=list_idle[0], hp = 3, speed = 4, strength_jump = 17)