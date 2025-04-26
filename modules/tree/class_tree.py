from ..main_classes import Settings

class Tree(Settings):
    """
    ### Class of tree
    """
    def __init__(self, x, y, width, height, image, random_egg, sprite_frequency_tree):
        self.ramdom_egg = random_egg
        self.idle_count = 0
        self.sprite_frequency_tree = sprite_frequency_tree
        super().__init__(x, y, width, height, image)

    def idle(self, list_bubble_tree): #DRAWING A IDLE
            self.image = list_bubble_tree[self.idle_count]
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
            if left_x_p + 60 <= self.x + 80:
                if right_x_p - 60 >= self.x + 80:
                    if top_y_p + 60 <= bottom_y:
                        if self.ramdom_egg == 1:
                            return True
                        
        #middle (golden)
        if bottom_y_p >= bottom_y:
            if left_x_p + 60 >= self.x + 80:
                if right_x_p - 60 <= right_x - 80:
                    if top_y_p + 60 <= bottom_y:
                        if self.ramdom_egg == 1:
                            return True
        
        #right angle
        if bottom_y_p >= bottom_y:
            if right_x_p - 60 >= right_x - 80:
                if left_x_p + 60 <= right_x - 80:
                    if top_y_p + 60 <= bottom_y:
                        if self.ramdom_egg == 1:
                            return True