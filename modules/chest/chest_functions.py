from ..main_classes import Block
from ..resourses import droped_resources, Discarded_Item

import random

chests = []

class Chest(Block):
    """
    ### Class of chests with open, hide functions
    """
    def __init__(self, x, y, width, height, image, open_chest):
        self.open_chest = open_chest
        self.hide_in_him = False
        super().__init__(x, y, width, height, image)
    
    def check_open(self, count_key, player): #CHECK OPEN
        list_return = [None, " "]
        if self.open_chest == False:
            random_n = random.randint(0, 3)
            answer = self.check_collision_bottom_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE BOTTOM
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    list_return[0] = True
                    if random_n == 1:
                        egg = Discarded_Item(x = self.x + (self.width / 2) - 5, y = self.y + self.height + 15, width = 20, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
                        droped_resources.append(egg)
                        list_return[1] = "egg"
                        return list_return
                    elif random_n == 2:
                        meat = Discarded_Item(x = self.x + (self.width / 2), y = self.y + self.height + 15, width = 40, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
                        droped_resources.append(meat)
                        list_return[1] = "meat"
                        return list_return
                    elif random_n == 3:
                        heart = Discarded_Item(x = self.x + (self.width / 2), y = self.y + self.height + 15, width = 30, height = 25, image = "images/resources/heart.png", whatIsThis= "heart")
                        droped_resources.append(heart)
                        list_return[1] = "heart"
                        return list_return
                    list_return[1] = "nothing"
                    return list_return
            answer = self.check_collision_left_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE LEFT
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    list_return[0] = True
                    if random_n == 1:
                        egg = Discarded_Item(x = self.x - 15, y = self.y, width = 20, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
                        droped_resources.append(egg)
                        list_return[1] = "egg"
                        return list_return
                    elif random_n == 2:
                        meat = Discarded_Item(x = self.x - 15, y = self.y, width = 40, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
                        droped_resources.append(meat)
                        list_return[1] = "meat"
                        return list_return
                    elif random_n == 3:
                        heart = Discarded_Item(x = self.x - 15, y = self.y, width = 30, height = 25, image = "images/resources/heart.png", whatIsThis= "heart")
                        droped_resources.append(heart)
                        list_return[1] = "heart"
                        return list_return
                    list_return[1] = "nothing"
                    return list_return
            answer = self.check_collision_right_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE RIGHT
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    list_return[0] = True
                    if random_n == 1:
                        egg = Discarded_Item(x = self.x + self.width + 25, y = self.y - 10, width = 20, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
                        droped_resources.append(egg)
                        list_return[1] = "egg"
                        return list_return
                    elif random_n == 2:
                        meat = Discarded_Item(x = self.x + self.width + 25, y = self.y - 10, width = 40, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
                        droped_resources.append(meat)
                        list_return[1] = "meat"
                        return list_return
                    elif random_n == 3:
                        heart = Discarded_Item(x = self.x + self.width + 25, y = self.y - 10, width = 30, height = 25, image = "images/resources/heart.png", whatIsThis= "heart")
                        droped_resources.append(heart)
                        list_return[1] = "heart"
                        return list_return
                    list_return[1] = "nothing"
                    return list_return
            answer = self.check_collision_top_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE TOP
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer:
                if count_key >= 1:
                    self.open_chest = True
                    list_return[0] = True
                    if random_n == 1:
                        egg = Discarded_Item(x = self.x + 15, y = self.y - 40, width = 20, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
                        droped_resources.append(egg)
                        list_return[1] = "egg"
                        return list_return
                    elif random_n == 2:
                        meat = Discarded_Item(x = self.x + 15, y = self.y - 40, width = 40, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
                        droped_resources.append(meat)
                        list_return[1] = "meat"
                        return list_return
                    elif random_n == 3:
                        heart = Discarded_Item(x = self.x + 15, y = self.y - 40, width = 30, height = 25, image = "images/resources/heart.png", whatIsThis= "heart")
                        droped_resources.append(heart)
                        list_return[1] = "heart"
                        return list_return
                    list_return[1] = "nothing"
                    return list_return
        else:
            answer = self.check_collision_bottom_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE BOTTOM
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer: 
                self.hide_in_him = True
                list_return[0] = False
            answer = self.check_collision_left_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE LEFT
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer: 
                self.hide_in_him = True
                list_return[0] = False
            answer = self.check_collision_right_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE RIGHT
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer: 
                self.hide_in_him = True
                list_return[0] = False
            answer = self.check_collision_top_wall(left_x_p = player.x, top_y_p = player.y, #IS THE PLAYER STANDING NEXT TO THE CHEST ON THE TOP
                                            right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
            if answer: 
                self.hide_in_him = True
                list_return[0] = False
        return list_return