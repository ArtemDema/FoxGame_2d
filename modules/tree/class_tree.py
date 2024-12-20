from ..main_classes import Settings
from ..resourses import droped_resources, Discarded_Item

import random

list_bubble_tree = ["images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0000.png","images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0001.png",
                    "images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0002.png","images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0003.png",
                    "images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0004.png","images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0005.png",
                    "images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0006.png","images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0007.png",
                    "images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0008.png","images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0009.png",
                    "images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0010.png"]



class Tree(Settings):
    def __init__(self, x, y, width, height, image, random_egg):
        self.ramdom_egg = random_egg
        self.idle_count = 0
        self.sprite_frequency_tree = 0
        print(f"tree: {self.ramdom_egg}")
        super().__init__(x, y, width, height, image)
    
    def idle(self): #DRAWING A IDLE
            self.image = list_bubble_tree[self.idle_count]
            self.load_image()
            if self.idle_count == 10: 
                self.idle_count = 0
            else:
                if self.sprite_frequency_tree >= 10: 
                    self.idle_count += 1
                    self.sprite_frequency_tree = 0
                else: self.sprite_frequency_tree += 1

    def drop_egg(self, player):
        left_x_p = player.x
        right_x_p = player.x + player.width
        top_y_p = player.y
        bottom_y_p = player.y + player.height
        right_x = self.x + self.width
        bottom_y = self.y + self.height - 80

        #left angle
        if bottom_y_p >= bottom_y:
            if left_x_p + 20 <= self.x + 80:
                if right_x_p - 20 >= self.x + 80:
                    if top_y_p + 20 <= bottom_y:
                        if self.ramdom_egg == 1:
                            egg1 = Discarded_Item(x = self.x + 70, y = self.y - 30, width = 20, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
                            droped_resources.append(egg1)
                            self.ramdom_egg = 0
                        
        #middle (golden)
        if bottom_y_p >= bottom_y:
            if left_x_p + 20 >= self.x + 80:
                if right_x_p - 20 <= right_x - 80:
                    if top_y_p + 20 <= bottom_y:
                        if self.ramdom_egg == 1:
                            egg1 = Discarded_Item(x = self.x + 70, y = self.y - 30, width = 20, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
                            droped_resources.append(egg1)
                            self.ramdom_egg = 0
        
        #right angle
        if bottom_y_p >= bottom_y:
            if right_x_p - 20 >= right_x - 80:
                if left_x_p + 20 <= right_x - 80:
                    if top_y_p + 20 <= bottom_y:
                        if self.ramdom_egg == 1:
                            egg1 = Discarded_Item(x = self.x + 70, y = self.y - 30, width = 20, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
                            droped_resources.append(egg1)
                            self.ramdom_egg = 0

list_trees = []

tree1 = Tree(845, 510, 160, 190, "images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0000.png", random_egg = random.randint(0, 1))
list_trees.append(tree1)