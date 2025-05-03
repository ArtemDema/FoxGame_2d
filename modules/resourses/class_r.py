from ..main_classes import Block

class Discarded_Item(Block):
    """
    ### Class of discarded items
    """
    def __init__(self, x, y, width, height, image, whatIsThis):
        self.whatIsThis = whatIsThis
        super().__init__(x,y,width,height,image)

    def gravity(self,player, blocks, chests, boxes): #
        list_of_all_blocks = []
        list_of_all_blocks += blocks
        list_of_all_blocks += chests
        list_of_all_blocks += boxes
        for block in list_of_all_blocks:
            answer_fall_r = block.check_collision_top_wall(self.x, self.y, #
                                                        self.x + self.width, self.y + self.height)
            if answer_fall_r:
                break
        
        if answer_fall_r != True: #if he does not
            self.y += player.speed

    def check_collect_recource(self, player, meat_count, egg_count, key_count, heart_count, task_egg, task_meat, сollect_item): #CHECK COLLECT RESOURCES
        return_list = {}
        answer = self.check_collision_bottom_wall(left_x_p = player.x, top_y_p = player.y, #CHECKING IF THE PLAYER IS TOUCHING THE OBJECT BOTTOM
                                         right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
        if answer:
            self.x = 10000
            self.y = 10000
            if self.whatIsThis == "meat": 
                return_list["meat_count"] = meat_count + 1
                return_list["task_meat"] = task_meat - 1
                сollect_item.set_volume(0.1)
                сollect_item.play(loops = 0)
            elif self.whatIsThis == "egg": 
                return_list["egg_count"] = egg_count + 1
                return_list["task_egg"] = task_egg - 1
                сollect_item.set_volume(0.1)
                сollect_item.play(loops = 0)
            elif self.whatIsThis == "heart": 
                if player.hp < 5:
                    return_list["heart_count"] = heart_count + 1
                    сollect_item.set_volume(0.1)
                    сollect_item.play(loops = 0)
            else: 
                return_list["key_count"] = key_count + 1
                сollect_item.set_volume(0.1)
                сollect_item.play(loops = 0)
        answer = self.check_collision_left_wall(left_x_p = player.x - 10, top_y_p = player.y, #CHECKING IF THE PLAYER IS TOUCHING THE OBJECT LEFT
                                         right_x_p = player.x + player.width - 10, bottom_y_p = player.y + player.height)
        if answer:
            self.x = 10000
            self.y = 10000
            if self.whatIsThis == "meat": 
                return_list["meat_count"] = meat_count + 1
                return_list["task_meat"] = task_meat - 1
                сollect_item.set_volume(0.1)
                сollect_item.play(loops = 0)
            elif self.whatIsThis == "egg": 
                return_list["egg_count"] = egg_count + 1
                return_list["task_egg"] = task_egg - 1
                сollect_item.set_volume(0.1)
                сollect_item.play(loops = 0)
            elif self.whatIsThis == "heart": 
                if player.hp < 5:
                    return_list["heart_count"] = heart_count + 1
                    сollect_item.set_volume(0.1)
                    сollect_item.play(loops = 0)
            else: 
                return_list["key_count"] = key_count + 1
                сollect_item.set_volume(0.1)
                сollect_item.play(loops = 0)
        answer = self.check_collision_right_wall(left_x_p = player.x + 10, top_y_p = player.y, #CHECKING IF THE PLAYER IS TOUCHING THE OBJECT RIGHT
                                         right_x_p = player.x + player.width + 10, bottom_y_p = player.y + player.height)
        if answer:
            self.x = 10000
            self.y = 10000
            if self.whatIsThis == "meat": 
                return_list["meat_count"] = meat_count + 1
                return_list["task_meat"] = task_meat - 1
                сollect_item.set_volume(0.1)
                сollect_item.play(loops = 0)
            elif self.whatIsThis == "egg": 
                return_list["egg_count"] = egg_count + 1
                return_list["task_egg"] = task_egg - 1
                сollect_item.set_volume(0.1)
                сollect_item.play(loops = 0)
            elif self.whatIsThis == "heart": 
                if player.hp < 5:
                    return_list["heart_count"] = heart_count + 1
                    сollect_item.set_volume(0.1)
                    сollect_item.play(loops = 0)
            else: 
                return_list["key_count"] = key_count + 1
                сollect_item.set_volume(0.1)
                сollect_item.play(loops = 0)
        answer = self.check_collision_top_wall(left_x_p = player.x, top_y_p = player.y, #CHECKING IF THE PLAYER IS TOUCHING THE OBJECT TOP
                                         right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
        if answer:
            self.x = 10000
            self.y = 10000
            if self.whatIsThis == "meat": 
                return_list["meat_count"] = meat_count + 1
                return_list["task_meat"] = task_meat - 1
                сollect_item.set_volume(0.1)
                сollect_item.play(loops = 0)
            elif self.whatIsThis == "egg": 
                return_list["egg_count"] = egg_count + 1
                return_list["task_egg"] = task_egg - 1
                сollect_item.set_volume(0.1)
                сollect_item.play(loops = 0)
            elif self.whatIsThis == "heart": 
                if player.hp < 5:
                    return_list["heart_count"] = heart_count + 1
                    сollect_item.set_volume(0.1)
                    сollect_item.play(loops = 0)
            else: 
                return_list["key_count"] = key_count + 1
                сollect_item.set_volume(0.1)
                сollect_item.play(loops = 0)
        return return_list
        