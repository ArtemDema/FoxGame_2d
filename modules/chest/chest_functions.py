from ..main_classes import Block
from ..screen import blocks

chests = []

class Chest(Block):
    def __init__(self, x, y, width, height, image, open_chest):
        self.open_chest = open_chest
        super().__init__(x, y, width, height, image)
    
    def check_open(self, count_key, player):
        if self.open_chest == False:
            answer = self.check_collision_bottom_wall(left_x_p = player.x, top_y_p = player.y, 
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    return True
            answer = self.check_collision_left_wall(left_x_p = player.x, top_y_p = player.y, 
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    return True
            answer = self.check_collision_right_wall(left_x_p = player.x, top_y_p = player.y, 
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    return True
            answer = self.check_collision_top_wall(left_x_p = player.x, top_y_p = player.y, 
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    return True
        else:
            answer = self.check_collision_bottom_wall(left_x_p = player.x, top_y_p = player.y, 
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer: return False
            answer = self.check_collision_left_wall(left_x_p = player.x, top_y_p = player.y, 
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer: return False
            answer = self.check_collision_right_wall(left_x_p = player.x, top_y_p = player.y, 
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer: return False
            answer = self.check_collision_top_wall(left_x_p = player.x, top_y_p = player.y, 
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer: return False

    def check_up_the_chest(self, player):
        answer = self.check_collision_bottom_wall(left_x_p = player.x, top_y_p = player.y, 
                                        right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
        if answer: return True
        answer = self.check_collision_left_wall(left_x_p = player.x, top_y_p = player.y, 
                                        right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
        if answer: return True
        answer = self.check_collision_right_wall(left_x_p = player.x, top_y_p = player.y, 
                                        right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
        if answer: return True
        answer = self.check_collision_top_wall(left_x_p = player.x, top_y_p = player.y, 
                                        right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
        if answer: return True
        return False
    
    def throw_chest(self, angle, player):
        koef = player.speed / 90
        if angle >= 0 and angle <= 90:
            for block in blocks:
                answer = block.check_collision_bottom_wall(left_x_p = self.x, top_y_p = self.y, 
                                            right_x_p = self.x + self.width, bottom_y_p = self.y + self.height)
                if answer: break
                else:
                    for block in blocks:
                        answer = block.check_collision_left_wall(left_x_p = self.x, top_y_p = self.y, 
                                                right_x_p = self.x + self.width, bottom_y_p = self.y + self.height)
                        if answer: break
            if answer != True:
                speed_x = koef * angle
                speed_y = player.speed - (koef * angle)
                self.x += speed_x 
                self.y -= speed_y
        elif angle <= 0 and angle >= -90:
            for block in blocks:
                answer = block.check_collision_bottom_wall(left_x_p = self.x, top_y_p = self.y, 
                                            right_x_p = self.x + self.width, bottom_y_p = self.y + self.height)
                if answer: break
                else:
                    for block in blocks:
                        answer = block.check_collision_right_wall(left_x_p = self.x, top_y_p = self.y, 
                                                right_x_p = self.x + self.width, bottom_y_p = self.y + self.height)
                        if answer: break
            if answer != True:
                speed_x = koef * angle
                speed_y = player.speed - ((koef * angle) * -1)
                self.x += speed_x 
                self.y -= speed_y
        elif angle >= 90 and angle <= 180: 
            speed_x = koef * (angle - 90)
            speed_y = player.speed - (koef * (angle - 90))
            self.x += speed_x 
            self.y += speed_y
        elif angle <= -90 and angle >= -180: 
            speed_x = koef * (angle + 90)
            speed_y = player.speed - ((koef * (angle + 90)) * -1)
            self.x += speed_x 
            self.y += speed_y

    def gravity(self, player):
        for block in blocks:
            answer_fall_r = block.check_collision_top_wall(self.x - 15, self.y,
                                                        self.x + self.width + 15, self.y + self.height)
            if answer_fall_r:
                break
        if answer_fall_r != True: #if he does not
            self.y += player.speed

chest1 = Chest(900, 100, 50, 50, "images/chest/chest_lock.png", False)

chests.append(chest1)