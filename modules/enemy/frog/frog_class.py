from ...main_classes import Enemy
from ...resourses import Discarded_Item
from ...interface import interface

import random, math

class Frog(Enemy):
    """
    ### Class of frogs with aggressive character
    """
    def __init__(self, x, y, width, height, image, hp, speed, 
                 vector_move, idle_count, sprite_frequency_frog, is_dead):
        self.vector_move = vector_move
        self.idle_count = idle_count
        self.sprite_frequency_frog = sprite_frequency_frog
        self.random_idle = 0
        self.angle = 0
        self.is_dead = is_dead
        self.death_count = 0
        self.player_visibility = False
        self.frequency_jump = 300
        self.move_bottom = False
        self.move_jump = False
        self.count_jump = 5
        super().__init__(x, y, width, height, image, hp, speed)

    def jump_frog(self, blocks, chests, boxes):
        list_of_all_blocks = []
        list_of_all_blocks += blocks
        list_of_all_blocks += chests
        list_of_all_blocks += boxes

        if self.count_jump > 0:
            if self.angle == -45:
                for block in list_of_all_blocks:
                    answer = block.check_collision_left_wall(self.x + 10 * math.cos(self.angle * (math.pi / 180)), 
                                                             self.y + 10 * math.cos(self.angle * (math.pi / 180)), 
                                                             self.x + 10 * math.cos(self.angle * (math.pi / 180)) + self.width, 
                                                             self.y + 10 * math.cos(self.angle * (math.pi / 180)) + self.height - 10)
                    if answer:
                        self.move_jump = False
                        self.count_jump = 5
                        self.angle = 0
                        return
                    
            else:
                for block in list_of_all_blocks:
                    answer = block.check_collision_right_wall(self.x + 10 * math.cos(self.angle * (math.pi / 180)), 
                                                             self.y + 10 * math.cos(self.angle * (math.pi / 180)), 
                                                             self.x + 10 * math.cos(self.angle * (math.pi / 180)) + self.width, 
                                                             self.y + 10 * math.cos(self.angle * (math.pi / 180)) + self.height - 10)
                    if answer:
                        self.move_jump = False
                        self.count_jump = 5
                        self.angle = 0
                        return
                    
            self.x = self.x + 10 * math.cos(self.angle * (math.pi / 180))
            self.y = self.y + 10 * math.sin(self.angle * (math.pi / 180))
            self.count_jump -= 1
        else:
            self.move_jump = False
            self.count_jump = 5
            self.angle = 0
        return

    def move(self, player, blocks, chests, boxes): #MOVE JUMP
        if self.move_jump:
            self.jump_frog(blocks, chests, boxes)

        self.check_state(blocks)

        if self.idle_count == 3: 
            self.idle_count = 0
        else:
            if self.sprite_frequency_frog >= 50: 
                self.idle_count += 1
                self.sprite_frequency_frog = 0
            else: self.sprite_frequency_frog += 1

        if self.player_visibility:
            if player.hide == False:
                if self.frequency_jump == 0:
                    if self.angle == 0:
                        distance = player.x - self.x
                        if distance <= 0:
                            self.angle = -135
                            self.vector_move = 1
                        else:
                            self.angle = -45
                            self.vector_move = 0
                else:
                    self.frequency_jump -= 1

        if player.hide == False:
            answer = player.check_collision_left(self.x, self.y, self.x + self.width, self.y + self.height)
            if answer:
                player.damage_player()
        
            answer = player.check_collision_right(self.x, self.y, self.x + self.width, self.y + self.height)
            if answer:
                player.damage_player()

        if self.angle < 0:
            if self.frequency_jump <= 0:
                if self.angle == -135:
                    if self.vector_move == 1:

                        for block in blocks: #CHECKING IF THERE IS SOIL AT THE FUTURE LOCATION OF THE POINT
                            answer = block.check_collision_top_wall(self.x - 76, self.y - 15, self.x + self.width - 30, self.y + self.height + 15)
                            if answer:
                                break
                        
                        
                        if answer:
                            self.move_jump = True
                            self.frequency_jump = 300
                        else:
                            self.angle = 0
                    else:
                        self.angle = 0
                else:
                    if self.vector_move == 0:
                        for block in blocks: #CHECKING IF THERE IS SOIL AT THE FUTURE LOCATION OF THE POINT
                            answer = block.check_collision_top_wall(self.x + 60, self.y - 15, self.x + self.width + 60, self.y + self.height + 15)
                            if answer:
                                break
                            
                        if answer:
                            self.move_jump = True
                            self.frequency_jump = 300
                        else:
                            self.angle = 0
                    else:
                        self.angle = 0
            else:
                self.frequency_jump -= 1
        else:
            self.actions_frog()

    def actions_frog(self): #RANDOM ACTION
        random_antion = random.randint(0, 1)
        if random_antion == 0:
            self.random_idle = random.randint(120, 260)
        else:
            self.vector_move = random.randint(0, 1)
            random_antion = random.randint(0, 1)
            if random_antion == 0: self.angle = -135
            else: self.angle = -45

    def check_state(self, blocks):
        for block in blocks:
            answer = block.check_collision_top_wall(self.x - 12, self.y, self.x + self.width + 12, self.y + self.height)
            if answer:
                break
        
        if answer:
            self.move_bottom = False
        else:
            if self.move_jump == False:
                self.move_bottom = True

    def check_death(self, player, boxes, move_bottom): #CHECK DEATH CHICKEN
        if self.is_dead == False:
            for box in boxes:
                answer = box.check_collision_bottom_wall(self.x, self.y, #CHECK BOX FOR DEATH
                                                        self.x + self.width, self.y + self.height)
                if answer:
                    self.is_dead = True
                    interface[3].count += 1

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
                                    interface[3].count += 1

                #middle (golden)
                if bottom_y_p >= self.y:
                    if left_x_p + 33 >= self.x:
                        if right_x_p - 30 <= right_x:
                            if top_y_p + 20 <= self.y:
                                if bottom_y_p + 10 <= bottom_y:
                                    self.is_dead = True
                                    interface[3].count += 1
                                            
                #right angle
                if bottom_y_p >= self.y:
                    if left_x_p + 33 <= right_x:
                        if right_x_p - 30 >= right_x:
                            if top_y_p + 20 <= self.y:
                                if bottom_y_p + 10 <= bottom_y:
                                    self.is_dead = True
                                    interface[3].count += 1


    def dead_count(self, list_frog, droped_resources): #CHANGE SPRITE DEATH AND THEN DROPE A MEAT
        if self.death_count == 6:
            meat1 = Discarded_Item(x = self.x, y = self.y, width = 50, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
            droped_resources.append(meat1)
            list_frog.remove(self)
        else:
            if self.sprite_frequency_frog >= 10: 
                self.death_count += 1
                self.sprite_frequency_frog = 0
            else: self.sprite_frequency_frog += 1