import pygame
import os

pygame.init()

class Settings:
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
    def __init__(self, x, y, width, height, image, hp, speed):
        self.hp = hp
        self.speed = speed
        super().__init__(x, y, width, height, image)

class Block(Settings):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)

    def check_collision_right_wall(self, left_x_p, top_y_p, right_x_p, bottom_y_p):
        right_x = self.x + self.width
        bottom_y = self.y + self.height

        #top corner
        if left_x_p + 15 <= right_x:
            if top_y_p + 30 <= self.y:
                if bottom_y_p - 5 >= self.y:
                    if right_x_p - 20 >= right_x:
                        return True
        
        #middle (golden)
        if left_x_p + 15 <= right_x:
            if top_y_p + 30 >= self.y:
                if bottom_y_p <= bottom_y:
                    if right_x_p - 20 >= right_x:
                            return True

        #bottom corner                            
        if left_x_p + 15 <= right_x:
            if top_y_p + 30 <= bottom_y:
                if bottom_y_p >= bottom_y:
                    if right_x_p - 20 >= right_x:
                        return True
    
    def check_collision_left_wall(self, left_x_p, top_y_p, right_x_p, bottom_y_p):
        right_x = self.x + self.width
        bottom_y = self.y + self.height
        
        #top corner
        if left_x_p + 20 <= self.x:
            if top_y_p + 30 <= self.y:
                if bottom_y_p - 5 >= self.y:
                    if right_x_p - 15 >= self.x:
                        return True
        
        #middle (golden)
        if left_x_p + 20 <= self.x:
            if top_y_p + 30 >= self.y:
                if bottom_y_p <= bottom_y:
                    if right_x_p - 15 >= self.x:
                        return True
                                    
        #bottom corner
        if left_x_p + 20 <= self.x:
            if top_y_p + 30 <= bottom_y:
                if bottom_y_p >= bottom_y:
                    if right_x_p - 15 >= self.x:
                        return True
    
    def check_collision_top_wall(self, left_x_p, top_y_p, right_x_p, bottom_y_p):

        right_x = self.x + self.width
        bottom_y = self.y + self.height
        
        #левый угол
        if bottom_y_p >= self.y:
            if left_x_p + 23 <= self.x:
                if right_x_p - 20 >= self.x:
                    if top_y_p + 20 <= self.y:
                        return True

        #middle (golden)
        if bottom_y_p >= self.y:
            if left_x_p + 23 >= self.x:
                if right_x_p - 20 <= right_x:
                    if top_y_p + 20 <= self.y:
                        return True
                                    
        #правый угол
        if bottom_y_p >= self.y:
            if left_x_p + 23 <= right_x:
                if right_x_p - 20 >= right_x:
                    if top_y_p + 20 <= self.y:
                        return True

    def check_collision_bottom_wall(self, left_x_p, top_y_p, right_x_p, bottom_y_p):
        right_x = self.x + self.width
        bottom_y = self.y + self.height

        #левый угол
        if bottom_y_p >= bottom_y:
            if left_x_p + 20 <= self.x:
                    if right_x_p - 20 >= self.x:
                        if top_y_p + 20 <= bottom_y:
                            return True
                        
        #middle (golden)
        if bottom_y_p >= bottom_y:
            if left_x_p + 20 >= self.x:
                if right_x_p - 20 <= right_x:
                        if top_y_p + 20 <= bottom_y:
                            return True
        
        #правый угол
        if bottom_y_p >= bottom_y:
            if right_x_p - 20 >= right_x:
                if left_x_p + 20 <= right_x:
                    if top_y_p + 20 <= bottom_y:
                        return True