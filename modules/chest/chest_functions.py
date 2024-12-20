from ..main_classes import Block
from ..screen import blocks

import math, random

chests = []

class Chest(Block):
    def __init__(self, x, y, width, height, image, open_chest, random_key):
        self.open_chest = open_chest
        self.random_key = random_key
        print(f"chest: {self.random_key}")
        super().__init__(x, y, width, height, image)
    
    def check_open(self, count_key, player): #CHECK OPEN
        if self.open_chest == False:
            answer = self.check_collision_bottom_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE BOTTOM
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    return True
            answer = self.check_collision_left_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE LEFT
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    return True
            answer = self.check_collision_right_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE RIGHT
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    return True
            answer = self.check_collision_top_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE TOP
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    return True
        else:
            answer = self.check_collision_bottom_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE BOTTOM
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer: return False
            answer = self.check_collision_left_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE LEFT
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer: return False
            answer = self.check_collision_right_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE RIGHT
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer: return False
            answer = self.check_collision_top_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE TOP
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer: return False

    def check_up_the_chest(self, player): #
        answer = self.check_collision_bottom_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE BOTTOM
                                        right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
        if answer: return True
        answer = self.check_collision_left_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE LEFT
                                        right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
        if answer: return True
        answer = self.check_collision_right_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE RIGHT
                                        right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
        if answer: return True
        answer = self.check_collision_top_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE TOP
                                        right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
        if answer: return True
        return False
    
    def throw_chest(self, angle): #CHEST THROW
        for_jump = math.pi / 180
        if angle == -45:
            for block in blocks: #DOES THE PLAYER TOUCH THE BOTTOM COLLISION BLOCK
                answer = block.check_collision_bottom_wall(left_x_p = self.x, top_y_p = self.y, 
                                            right_x_p = self.x + self.width, bottom_y_p = self.y + self.height)
                if answer: break
                else:
                    for block in blocks: #IS THE PLAYER TOUCHING THE LEFT WALL
                        answer = block.check_collision_left_wall(left_x_p = self.x, top_y_p = self.y, 
                                                right_x_p = self.x + self.width, bottom_y_p = self.y + self.height)
                        if answer: break
            if answer != True:
                self.x = self.x + 150 * math.cos(angle * for_jump)
                self.y = self.y + 150 * math.sin(angle * for_jump)
        else:
            for block in blocks: #IS THE PLAYER TOUCHING THE BOTTOM WALL
                answer = block.check_collision_bottom_wall(left_x_p = self.x, top_y_p = self.y, 
                                            right_x_p = self.x + self.width, bottom_y_p = self.y + self.height)
                if answer: break
                else:
                    for block in blocks: #IS THE PLAYER TOUCHING THE RIGHT WALL
                        answer = block.check_collision_right_wall(left_x_p = self.x, top_y_p = self.y, 
                                                right_x_p = self.x + self.width, bottom_y_p = self.y + self.height)
                        if answer: break
            if answer != True:
                self.x = self.x + 150 * math.cos(angle * for_jump)
                self.y = self.y + 150 * math.sin(angle * for_jump)

    def gravity(self, player): #GRAVITY CHEST
        for block in blocks: #DOES THE CHEST TOUCH THE FLOOR
            answer_fall_r = block.check_collision_top_wall(self.x - 15, self.y,
                                                        self.x + self.width + 15, self.y + self.height)
            if answer_fall_r:
                break
        if answer_fall_r != True: #if he does not
            self.y += player.speed

chest1 = Chest(750, 500, 50, 50, "images/chest/chest_lock.png", False, random_key = random.randint(0, 1))

chests.append(chest1)