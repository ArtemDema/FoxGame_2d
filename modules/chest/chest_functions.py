from ..main_classes import Block

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

chest1 = Chest(900, 700, 50, 50, "images/chest/chest_lock.png", False)

chests.append(chest1)