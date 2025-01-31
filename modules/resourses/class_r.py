from ..main_classes import Block

droped_resources = []

class Discarded_Item(Block):
    """
    ### Class of discarded items
    """
    def __init__(self, x, y, width, height, image, whatIsThis):
        self.whatIsThis = whatIsThis
        super().__init__(x,y,width,height,image)

    def gravity(self,player, blocks): #
        for block in blocks:
            answer_fall_r = block.check_collision_top_wall(self.x, self.y, #
                                                        self.x + self.width, self.y + self.height)
            if answer_fall_r:
                break
        if answer_fall_r != True: #if he does not
            self.y += player.speed

    def check_collect_recource(self, player, meat_count, egg_count, key_count, heart_count): #CHECK COLLECT RESOURCES
        return_list = {}
        answer = self.check_collision_bottom_wall(left_x_p = player.x, top_y_p = player.y, #CHECKING IF THE PLAYER IS TOUCHING THE OBJECT BOTTOM
                                         right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
        if answer:
            self.x = 10000
            self.y = 10000
            if self.whatIsThis == "meat": return_list["meat_count"] = meat_count + 1
            elif self.whatIsThis == "egg": return_list["egg_count"] = egg_count + 1
            elif self.whatIsThis == "heart": return_list["heart_count"] = heart_count + 1
            else: return_list["key_count"] = key_count + 1
        answer = self.check_collision_left_wall(left_x_p = player.x - 10, top_y_p = player.y, #CHECKING IF THE PLAYER IS TOUCHING THE OBJECT LEFT
                                         right_x_p = player.x + player.width - 10, bottom_y_p = player.y + player.height)
        if answer:
            self.x = 10000
            self.y = 10000
            if self.whatIsThis == "meat": return_list["meat_count"] = meat_count + 1
            elif self.whatIsThis == "egg": return_list["egg_count"] = egg_count + 1
            elif self.whatIsThis == "heart": return_list["heart_count"] = heart_count + 1
            else: return_list["key_count"] = key_count + 1
        answer = self.check_collision_right_wall(left_x_p = player.x + 10, top_y_p = player.y, #CHECKING IF THE PLAYER IS TOUCHING THE OBJECT RIGHT
                                         right_x_p = player.x + player.width + 10, bottom_y_p = player.y + player.height)
        if answer:
            self.x = 10000
            self.y = 10000
            if self.whatIsThis == "meat": return_list["meat_count"] = meat_count + 1
            elif self.whatIsThis == "egg": return_list["egg_count"] = egg_count + 1
            elif self.whatIsThis == "heart": return_list["heart_count"] = heart_count + 1
            else: return_list["key_count"] = key_count + 1
        answer = self.check_collision_top_wall(left_x_p = player.x, top_y_p = player.y, #CHECKING IF THE PLAYER IS TOUCHING THE OBJECT TOP
                                         right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
        if answer:
            self.x = 10000
            self.y = 10000
            if self.whatIsThis == "meat": return_list["meat_count"] = meat_count + 1
            elif self.whatIsThis == "egg": return_list["egg_count"] = egg_count + 1
            elif self.whatIsThis == "heart": return_list["heart_count"] = heart_count + 1
            else: return_list["key_count"] = key_count + 1
        return return_list
        
meat1 = Discarded_Item(x = 700, y = 0, width = 40, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
egg1 = Discarded_Item(x = 800, y = 100, width = 20, height = 30, image = "images/resources/egg.png",whatIsThis= "egg")
key1 = Discarded_Item(x = 900, y = 200, width = 30, height = 22, image = "images/resources/key.png",whatIsThis= "key")
key2 = Discarded_Item(x = 900, y = 200, width = 30, height = 22, image = "images/resources/key.png",whatIsThis= "key")
droped_resources.append(meat1)
droped_resources.append(egg1)
droped_resources.append(key1)
droped_resources.append(key2)