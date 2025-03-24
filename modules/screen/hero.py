from ..main_classes import Enemy
from ..json import get_info

import pygame

move_left = False
move_right = False
move_bottom = False
move_jump = False
move_crouch = False
hide = False
with_box = False
push_box = False

class Hero(Enemy):
    """
    ### Class of main person
    """
    def __init__(self, x, y, width, height, image, hp, speed, strength_jump):
        self.strength_jump = strength_jump
        self.timer_damage = 0
        self.hide = False
        super().__init__(x, y, width, height, image, hp, speed)
        
    def idle(self, idle_count, screen, last_side, with_chest, list_idle_with_chest, list_idle): #DRAWING IDLE POSITION
        if last_side == 0:
            if with_chest: self.image = list_idle_with_chest[idle_count]
            else: self.image = list_idle[idle_count]
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            if with_chest: self.image = list_idle_with_chest[idle_count]
            else: self.image = list_idle[idle_count]
            self.draw_image(screen)

    def run(self, run_count, screen, last_side, with_chest, list_run_with_chest, list_run): #DRAWING RUN POSITION
        if last_side == 0:
            if with_chest: self.image = list_run_with_chest[run_count]
            else: self.image = list_run[run_count]
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            if with_chest: self.image = list_run_with_chest[run_count]
            else: self.image = list_run[run_count]
            self.draw_image(screen)

    def jump(self, screen, last_side, list_jump): #DRAWING JUMP POSITION
        if last_side == 0:
            self.image = list_jump[0]
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            self.image = list_jump[0]
            self.draw_image(screen)

    def fall(self, screen, last_side, with_chest, list_jump_with_chest, list_jump): #DRAWING FALL POSITION
        if last_side == 0:
            if with_chest: self.image = list_jump_with_chest[0]
            else: self.image = list_jump[1]
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            if with_chest: self.image = list_jump_with_chest[0]
            else: self.image = list_jump[1]
            self.draw_image(screen)

    def crouch(self, crouch_count, screen, last_side, list_crouch): #DRAWING CROUCH POSITION
        if last_side == 0:
            self.image = list_crouch[crouch_count]
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            self.image = list_crouch[crouch_count]
            self.draw_image(screen)
    
    def damage_player(self):
        if self.timer_damage == 0:
            self.hp -= 1
            self.timer_damage = 360

    def check_collision_right(self, left_x_i, top_y_i, right_x_i, bottom_y_i): #CHECKING FOR TOUCHING THE RIGHT COLLISION
        right_x = self.x + self.width
        bottom_y = self.y + self.height

        #top corner
        if left_x_i <= right_x:
            if top_y_i <= self.y:
                if bottom_y_i >= self.y:
                    if right_x_i >= right_x:
                        return True
        
        #middle (golden)
        if left_x_i <= right_x:
            if top_y_i >= self.y:
                if bottom_y_i <= bottom_y:
                    if right_x_i >= right_x:
                            return True

        #bottom corner                            
        if left_x_i <= right_x:
            if top_y_i <= bottom_y:
                if bottom_y_i >= bottom_y:
                    if right_x_i >= right_x:
                        return True
    
    def check_collision_left(self, left_x_i, top_y_i, right_x_i, bottom_y_i): #CHECKING FOR TOUCHING THE LEFT COLLISION
        bottom_y = self.y + self.height
        
        #top corner
        if left_x_i <= self.x:
            if top_y_i <= self.y:
                if bottom_y_i >= self.y:
                    if right_x_i >= self.x:
                        return True
        
        #middle (golden)
        if left_x_i <= self.x:
            if top_y_i >= self.y:
                if bottom_y_i <= bottom_y:
                    if right_x_i >= self.x:
                        return True
                                    
        #bottom corner
        if left_x_i <= self.x:
            if top_y_i <= bottom_y:
                if bottom_y_i >= bottom_y:
                    if right_x_i >= self.x:
                        return True
    
    def check_collision_top(self, left_x_i, top_y_i, right_x_i, bottom_y_i): #CHECKING FOR TOUCHING THE TOP COLLISION
        right_x = self.x + self.width
        
        #left angle
        if bottom_y_i >= self.y:
            if left_x_i <= self.x:
                if right_x_i >= self.x:
                    if top_y_i <= self.y:
                        return True

        #middle (golden)
        if bottom_y_i >= self.y:
            if left_x_i >= self.x:
                if right_x_i <= right_x:
                    if top_y_i <= self.y:
                        return True
                                    
        #right angle
        if bottom_y_i >= self.y:
            if left_x_i <= right_x:
                if right_x_i >= right_x:
                    if top_y_i <= self.y:
                        return True

    def check_collision_bottom(self, left_x_i, top_y_i, right_x_i, bottom_y_i): #CHECKING FOR TOUCHING THE BOTTOM COLLISION
        right_x = self.x + self.width
        bottom_y = self.y + self.height

        #left angle
        if bottom_y_i >= bottom_y:
            if left_x_i <= self.x:
                if right_x_i >= self.x:
                    if top_y_i <= bottom_y:
                        return True
                        
        #middle (golden)
        if bottom_y_i >= bottom_y:
            if left_x_i >= self.x:
                if right_x_i <= right_x:
                    if top_y_i <= bottom_y:
                        return True
        
        #right angle
        if bottom_y_i >= bottom_y:
            if right_x_i >= right_x:
                if left_x_i <= right_x:
                    if top_y_i <= bottom_y:
                        return True


info = get_info()
player = Hero(x = 600, y = 620, width = 80, height = 80, image="images/player/idle/0.png", hp = info["hp"], speed = 4, strength_jump = 17)