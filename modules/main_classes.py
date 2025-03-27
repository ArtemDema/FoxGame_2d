import pygame
import os

pygame.init()

class Settings:
    """
    ### A class that contains all base values
    """
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.load_image()
    def load_image(self):
        absolute_path = os.path.abspath(__file__ +"/../../")
        absolute_path = os.path.join(absolute_path,self.image)
        image = pygame.image.load(absolute_path)
        scaled_image = pygame.transform.scale(image, (self.width, self.height))
        self.image = scaled_image

    def draw_image(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))


class Enemy(Settings):
    """
    ### Class for enemies
    """
    def __init__(self, x, y, width, height, image, hp, speed):
        self.hp = hp
        self.speed = speed
        super().__init__(x, y, width, height, image)
    
    def idle(self, idle_count, screen, last_side, list_idle): #DRAWING A IDLE
        if last_side == 0:
            self.image = list_idle[idle_count]
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            self.image = list_idle[idle_count]
            self.draw_image(screen)

    def run(self, run_count, screen, last_side, list_run): #DRAWING A RUN
        if last_side == 0:
            self.image = list_run[run_count]
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            self.image = list_run[run_count]
            self.draw_image(screen)

    def fall(self, screen, last_side, list_jump): #DRAWING A FALL
        if last_side == 0:
            self.image = list_jump[1]
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            self.image = list_jump[1]
            self.draw_image(screen)
    
    def jump(self, screen, last_side, list_jump): #DRAWING A FALL
        if last_side == 0:
            self.image = list_jump[0]
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.draw_image(screen)
        else:
            self.image = list_jump[0]
            self.draw_image(screen)
    
    def death(self, death_count, screen: pygame.Surface, list_death): #DRAWING A DEATH
        self.image = list_death[death_count]
        self.load_image()
        self.draw_image(screen)
        
    def gravity(self, player, blocks): #CHECKING IF THE ENEMY IS TOUCHING THE FLOOR
        for block in blocks:
            answer_fall_r = block.check_collision_top_wall(self.x + 10, self.y,
                                                        self.x + self.width - 10, self.y + self.height)
            if answer_fall_r:
                break
        if answer_fall_r != True: #if he does not
            self.y += player.speed

    def player_visibility_zone(self, player):
        #left
        if player.x >= self.x - 350:
            if player.x <= self.x:
                if player.y <= self.y + self.height:
                    if player.y >= self.y - 70:
                        return True
                
        #right
        if player.x <= self.x + self.width + 350:
            if player.x >= self.x + self.width:
                if player.y <= self.y + self.height:
                    if player.y >= self.y - 70:
                        return True
        return False

class Block(Settings):
    """
    ### Class for create blocks with check collision function
    """
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.rect = self.image.get_rect(midtop = (self.x + self.width // 2, self.y), 
                                        midbottom = (self.x + self.width // 2, self.y + self.height),
                                        midleft = (self.x, self.y + self.height // 2), 
                                        midright = (self.x + self.width, self.y + self.height // 2),
                                        topleft = (self.x, self.y),
                                        topright = (self.x + self.width, self.y),
                                        bottomleft = (self.x, self.y + self.height),
                                        bottomright = (self.x + self.width, self.y + self.height))
        
        self.top_rect = pygame.Rect((self.x), (self.y), (self.width), (10))

    def check_collision_right_wall(self, player): #CHECKING FOR TOUCHING THE RIGHT WALL
        if self.rect.collidepoint(player.rect.topleft):
            return True
        if self.rect.collidepoint(player.rect.midleft):
            return True
    
    def check_collision_left_wall(self, player): #CHECKING FOR TOUCHING THE LEFT WALL
        if self.rect.collidepoint(player.rect.topright):
            return True
        if self.rect.collidepoint(player.rect.midright):
            return True
    
    def check_collision_top_wall(self, player): #CHECKING FOR TOUCHING THE TOP WALL
        if self.top_rect.collidepoint(player.rect.midbottom):
            return True
        if self.top_rect.collidepoint(player.rect.bottomleft):
            return True
        if self.top_rect.collidepoint(player.rect.bottomright):
            return True

    def check_collision_bottom_wall(self, player): #CHECKING FOR TOUCHING THE BOTTOM WALL
        if self.rect.collidepoint(player.rect.midtop):
            return True
                    
class BackGround(Settings):
    def __init__(self, x, y, width, height, image):
        super().__init__(x = x, y = y, width = width, height = height, image = image)