from ..main_classes import Block
from ..resourses import droped_resources, Discarded_Item

import random

chests = []

class Chest(Block):
    def __init__(self, x, y, width, height, image, open_chest):
        self.open_chest = open_chest
        self.hide_in_him = False
        super().__init__(x, y, width, height, image)
    
    def check_open(self, count_key, player): #CHECK OPEN
        if self.open_chest == False:
            random_n = random.randint(0, 3)
            answer = self.check_collision_bottom_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE BOTTOM
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    if random_n == 1:
                        egg = Discarded_Item(x = self.x + (self.width / 2), y = self.y + self.width + 10, width = 20, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
                        droped_resources.append(egg)
                    elif random_n == 2:
                        meat = Discarded_Item(x = self.x + (self.width / 2), y = self.y + self.width + 10, width = 40, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
                        droped_resources.append(meat)
                    elif random_n == 3:
                        heart = Discarded_Item(x = self.x + (self.width / 2), y = self.y + self.width + 10, width = 30, height = 25, image = "images/resources/heart.png", whatIsThis= "heart")
                        droped_resources.append(heart)
                    return True
            answer = self.check_collision_left_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE LEFT
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    if random_n == 1:
                        egg = Discarded_Item(x = self.x - 10, y = self.y, width = 20, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
                        droped_resources.append(egg)
                    elif random_n == 2:
                        meat = Discarded_Item(x = self.x - 10, y = self.y, width = 40, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
                        droped_resources.append(meat)
                    elif random_n == 3:
                        heart = Discarded_Item(x = self.x - 10, y = self.y, width = 30, height = 25, image = "images/resources/heart.png", whatIsThis= "heart")
                        droped_resources.append(heart)
                    return True
            answer = self.check_collision_right_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE RIGHT
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    if random_n == 1:
                        egg = Discarded_Item(x = self.x + self.width + 10, y = self.y, width = 20, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
                        droped_resources.append(egg)
                    elif random_n == 2:
                        meat = Discarded_Item(x = self.x + self.width + 10, y = self.y, width = 40, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
                        droped_resources.append(meat)
                    elif random_n == 3:
                        heart = Discarded_Item(x = self.x + self.width + 10, y = self.y, width = 30, height = 25, image = "images/resources/heart.png", whatIsThis= "heart")
                        droped_resources.append(heart)
                    return True
            answer = self.check_collision_top_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE TOP
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    if random_n == 1:
                        egg = Discarded_Item(x = self.x + (self.width / 2), y = self.y - 20, width = 20, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
                        droped_resources.append(egg)
                    elif random_n == 2:
                        meat = Discarded_Item(x = self.x + (self.width / 2), y = self.y - 20, width = 40, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
                        droped_resources.append(meat)
                    elif random_n == 3:
                        heart = Discarded_Item(x = self.x + (self.width / 2), y = self.y - 20, width = 30, height = 25, image = "images/resources/heart.png", whatIsThis= "heart")
                        droped_resources.append(heart)
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