from ..main_classes import Block
from ..screen import blocks

chests = []

class Chest(Block):
    def __init__(self, x, y, width, height, image, open_chest):
        self.open_chest = open_chest
        self.hide_in_him = False
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
            if answer: 
                self.hide_in_him = True
                return False
            answer = self.check_collision_left_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE LEFT
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer: 
                self.hide_in_him = True
                return False
            answer = self.check_collision_right_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE RIGHT
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer: 
                self.hide_in_him = True
                return False
            answer = self.check_collision_top_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE TOP
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer: 
                self.hide_in_him = True
                return False

chest1 = Chest(2075, 700, 50, 50, "images/chest/chest_lock.png", False)

chests.append(chest1)