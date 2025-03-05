from ..main_classes import Block

import math, random

class Box(Block):
    """
    ### Class of boxes with open, hide and push functions
    """
    def __init__(self, x, y, width, height, image, open_box):
        self.open_box = open_box
        self.random_key = random.randint(0, 1)
        self.hide_in_him = False
        super().__init__(x, y, width, height, image)

    def check_up_the_box(self, player): #
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
    
    def throw_box(self, angle, blocks): #CHEST THROW
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
                self.x = self.x + 150 * math.cos(angle * (math.pi / 180))
                self.y = self.y + 150 * math.sin(angle * (math.pi / 180))
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
                self.x = self.x + 150 * math.cos(angle * (math.pi / 180))
                self.y = self.y + 150 * math.sin(angle * (math.pi / 180))

    def gravity(self, player, blocks, chests, boxes): #GRAVITY CHEST
        list_of_all_blocks = []
        list_of_all_blocks += blocks
        list_of_all_blocks += chests
        list_of_all_blocks += boxes

        for block in list_of_all_blocks: #DOES THE CHEST TOUCH THE FLOOR
            answer_fall_r = block.check_collision_top_wall(self.x - 15, self.y,
                                                        self.x + self.width + 15, self.y + self.height + 1)
            if answer_fall_r:
                break
        if answer_fall_r != True:
            for chest in chests: #DOES THE CHEST TOUCH THE FLOOR
                answer_fall_r = chest.check_collision_top_wall(self.x - 15, self.y,
                                                            self.x + self.width + 15, self.y + self.height + 1)
                if answer_fall_r:
                    break

        if answer_fall_r != True: #if he does not
            self.y += player.speed