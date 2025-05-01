from ...main_classes import Enemy, Block
from ...interface import interface
from ...resourses import Discarded_Item

class Chick(Enemy, Block):
    def __init__(self, x, y, width, height, image, hp, speed, sprite_frequency_chick, is_dead, death_count):
        self.vector_move = -1
        self.run_count = 0
        self.sprite_frequency_chick = sprite_frequency_chick
        self.is_dead = is_dead
        self.death_count = death_count
        self.spawn_count = 0
        self.player_visibility = False
        Enemy.__init__(self, x, y, width, height, image, hp, speed)

    def move_vector(self, player):
        distance = player.x - self.x
        if distance <= 0:
            self.vector_move = 0
        else:
            self.vector_move = 1

    def move(self, player, blocks, chests, boxes):
        if self.spawn_count >= 5:
            if self.vector_move == 0:
                if player.hide == False:
                    answer = player.check_collision_right(self.x, self.y, self.x + self.width, self.y + self.height)
                    if answer:
                        player.damage_player()

                    for block in blocks: #CHECKING IF THERE IS SOIL AT THE FUTURE LOCATION OF THE POINT
                        answer = block.check_collision_top_wall(self.x - 15, self.y, self.x + self.width - 15, self.y + self.height + 20)
                        if answer:
                            break
                        
                    if answer:
                        list_of_all_blocks = []
                        list_of_all_blocks += blocks
                        list_of_all_blocks += chests
                        list_of_all_blocks += boxes

                        for block in list_of_all_blocks: #CHECK TOUCH RIGHT WALL OF BLOCK
                            answer = block.check_collision_right_wall(self.x, self.y, 
                                                                    self.x + self.width, self.y + self.height)
                            if answer:
                                if self.run_count == 3: 
                                    self.run_count = 0
                                else:
                                    if self.sprite_frequency_chick >= 10: 
                                        self.run_count += 1
                                        self.sprite_frequency_chick = 0
                                    else: self.sprite_frequency_chick += 1
                                return

                        if answer != True:
                            self.x -= self.speed

                            if self.run_count == 3: 
                                self.run_count = 0
                            else:
                                if self.sprite_frequency_chick >= 10: 
                                    self.run_count += 1
                                    self.sprite_frequency_chick = 0
                                else: self.sprite_frequency_chick += 1
            elif self.vector_move == 1:
                if player.hide == False:
                    answer = player.check_collision_left(self.x, self.y, self.x + self.width, self.y + self.height)
                    if answer:
                        player.damage_player()

                    for block in blocks: #CHECKING IF THERE IS SOIL AT THE FUTURE LOCATION OF THE POINT
                        answer = block.check_collision_top_wall(self.x + 15, self.y, self.x + self.width + 15, self.y + self.height + 20)
                        if answer:
                            break
                        
                    if answer:
                        list_of_all_blocks = []
                        list_of_all_blocks += blocks
                        list_of_all_blocks += chests
                        list_of_all_blocks += boxes

                        for block in list_of_all_blocks: #CHECK TOUCH RIGHT WALL OF BLOCK
                            answer = block.check_collision_left_wall(self.x, self.y, 
                                                                    self.x + self.width, self.y + self.height)
                            if answer:
                                if self.run_count == 3: 
                                    self.run_count = 0
                                else:
                                    if self.sprite_frequency_chick >= 10: 
                                        self.run_count += 1
                                        self.sprite_frequency_chick = 0
                                    else: self.sprite_frequency_chick += 1
                                return

                        if answer != True:
                            self.x += self.speed

                            if self.run_count == 3: 
                                self.run_count = 0
                            else:
                                if self.sprite_frequency_chick == 10: 
                                    self.run_count += 1
                                    self.sprite_frequency_chick = 0
                                else: self.sprite_frequency_chick += 1
            else:
                self.move_vector(player)
        else:
            if self.player_visibility:
                self.appearance_count()
    
    def check_death(self, player, boxes, move_bottom, task_enemy): #CHECK DEATH opossum
        if self.is_dead == False:
            for box in boxes:
                answer = box.check_collision_bottom_wall(self.x, self.y, #CHECK BOX FOR DEATH
                                                        self.x + self.width, self.y + self.height)
                if answer:
                    self.is_dead = True
                    interface[6].count += 1
                    task_enemy -= 1

            if move_bottom == True:
                right_x = self.x + self.width
                bottom_y = self.y + self.height

                bottom_y_p = player.y + player.height
                left_x_p = player.x
                right_x_p = player.x + player.width
                top_y_p = player.y
                #left angle
                if bottom_y_p >= self.y:
                    if left_x_p + 33 <= self.x:
                        if right_x_p - 30 >= self.x:
                            if top_y_p + 20 <= self.y:
                                if bottom_y_p + 10 <= bottom_y:
                                    self.is_dead = True
                                    interface[6].count += 1
                                    task_enemy -= 1

                #middle (golden)
                if bottom_y_p >= self.y:
                    if left_x_p + 33 >= self.x:
                        if right_x_p - 30 <= right_x:
                            if top_y_p + 20 <= self.y:
                                if bottom_y_p + 10 <= bottom_y:
                                    self.is_dead = True
                                    interface[6].count += 1
                                    task_enemy -= 1
                                            
                #right angle
                if bottom_y_p >= self.y:
                    if left_x_p + 33 <= right_x:
                        if right_x_p - 30 >= right_x:
                            if top_y_p + 20 <= self.y:
                                if bottom_y_p + 10 <= bottom_y:
                                    self.is_dead = True
                                    interface[6].count += 1
                                    task_enemy -= 1
        return task_enemy
    
    def dead_count(self, list_chick, droped_resources): #CHANGE SPRITE DEATH AND THEN DROPE A MEAT
        if self.death_count == 6:
            meat1 = Discarded_Item(x = self.x, y = self.y, width = 50, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
            droped_resources.append(meat1)
            list_chick.remove(self)
            self.x = 10000
            self.y = 10000
        else:
            if self.sprite_frequency_chick >= 10: 
                self.death_count += 1
                self.sprite_frequency_chick = 0
            else: self.sprite_frequency_chick += 1

    def appearance_count(self): #CHANGE SPRITE DEATH AND THEN DROPE A MEAT
        if self.spawn_count != 5:
            if self.sprite_frequency_chick >= 10: 
                self.spawn_count += 1
                self.sprite_frequency_chick = 0
            else: self.sprite_frequency_chick += 1