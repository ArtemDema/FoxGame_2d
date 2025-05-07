from ...main_classes import Enemy, Block
from ...resourses import Discarded_Item
from ...interface import interface

import random

list_jump = []

class Chicken(Enemy, Block):
    """
    ### Chicken class
    """
    def __init__(self, x, y, width, height, image, hp, speed, sound):
        self.vector_move = 0
        self.run_count = 0
        self.sprite_frequency_chicken = 2
        self.random_idle = 0
        self.random_move = 0
        self.is_dead = False
        self.death_count = 0
        self.player_visibility = False
        self.idle_count = 0
        self.random_sound = random.randint(600, 2600)
        self.sound = sound
        Enemy.__init__(self, x, y, width, height, image, hp, speed)

    def move(self, player, blocks, chests, boxes, sound_damage): #FUNCTION MOVE
        list_of_all_blocks = []
        list_of_all_blocks += blocks
        list_of_all_blocks += chests
        list_of_all_blocks += boxes
        self.play_chicken_sound()

        if self.player_visibility:
            if self.random_move <= 0:
                distance = player.x - self.x
                if distance <= 0:
                    self.random_move = 200
                    self.vector_move = 1
                else:
                    self.random_move = 200
                    self.vector_move = 0


        if self.random_move >= 0:
            if self.vector_move == 0:
                for block in blocks: #CHECKING IF THERE IS SOIL AT THE FUTURE LOCATION OF THE POINT
                    answer = block.check_collision_top_wall(self.x - 15, self.y, self.x + self.width - 15, self.y + self.height + 20)
                    if answer:
                        break
                    
                if answer:
                    for block in list_of_all_blocks: #CHECK TOUCH RIGHT WALL OF BLOCK
                        answer = block.check_collision_right_wall(self.x, self.y, 
                                                                self.x + self.width, self.y + self.height)
                        if answer:
                            if self.run_count == 3: 
                                self.run_count = 0
                            else:
                                if self.sprite_frequency_chicken >= 10: 
                                    self.run_count += 1
                                    self.sprite_frequency_chicken = 0
                                else: self.sprite_frequency_chicken += 1
                            self.random_move =- 1
                            return

                    if answer != True:
                        self.x -= self.speed
                        self.random_move -= self.speed

                        if self.run_count == 3: 
                            self.run_count = 0
                        else:
                            if self.sprite_frequency_chicken >= 10: 
                                self.run_count += 1
                                self.sprite_frequency_chicken = 0
                            else: self.sprite_frequency_chicken += 1
                else:
                    self.random_move = -1
            else:
                for block in blocks: #CHECKING IF THERE IS SOIL AT THE FUTURE LOCATION OF THE POINT
                    answer = block.check_collision_top_wall(self.x + 15, self.y, self.x + self.width + 15, self.y + self.height + 20)
                    if answer:
                        break
                    
                if answer:
                    for block in list_of_all_blocks: #CHECK TOUCH LEFT WALL OF BLOCK
                        answer = block.check_collision_left_wall(self.x, self.y, 
                                                                self.x + self.width + 15, self.y + self.height)
                        if answer:
                            if self.run_count == 3: 
                                self.run_count = 0
                            else:
                                if self.sprite_frequency_chicken >= 10: 
                                    self.run_count += 1
                                    self.sprite_frequency_chicken = 0
                                else: self.sprite_frequency_chicken += 1
                            self.random_move =- 1
                            return

                    if answer != True:
                        self.x += self.speed
                        self.random_move -= self.speed

                        if self.run_count == 3: 
                            self.run_count = 0
                        else:
                            if self.sprite_frequency_chicken == 10: 
                                self.run_count += 1
                                self.sprite_frequency_chicken = 0
                            else: self.sprite_frequency_chicken += 1
                else:
                    self.random_move = -1
        elif self.random_idle >= 0:
            self.random_idle -= 1
            if self.idle_count == 3: 
                self.idle_count = 0
            else:
                if self.sprite_frequency_chicken >= 10: 
                    self.idle_count += 1
                    self.sprite_frequency_chicken = 0
                else: self.sprite_frequency_chicken += 1
            return
        else:
            self.actions_chicken()

    def actions_chicken(self): #RANDOM ACTION
        random_antion = random.randint(0, 1)
        if random_antion == 0:
            self.random_idle = random.randint(120, 260)
        else:
            self.vector_move = random.randint(0, 1)
            self.random_move = random.randint(50, 250)
    
    def play_chicken_sound(self):
        if self.random_sound == 0:
            self.sound.set_volume(0.09)
            self.sound.play(loops = 0)
            self.random_sound = random.randint(600, 2600)
        else:
            self.random_sound -= 1

    def check_death(self, player, boxes, move_bottom, task_enemy, death_enemy): #CHECK DEATH opossum
        if self.is_dead == False:
            for box in boxes:
                answer = box.check_collision_bottom_wall(self.x, self.y, #CHECK BOX FOR DEATH
                                                        self.x + self.width, self.y + self.height)
                if answer:
                    self.is_dead = True
                    interface[4].count += 1
                    task_enemy -= 1
                    death_enemy.set_volume(0.1)
                    death_enemy.play(loops = 0)

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
                                    interface[4].count += 1
                                    task_enemy -= 1
                                    death_enemy.set_volume(0.1)
                                    death_enemy.play(loops = 0)

                #middle (golden)
                if bottom_y_p >= self.y:
                    if left_x_p + 33 >= self.x:
                        if right_x_p - 30 <= right_x:
                            if top_y_p + 20 <= self.y:
                                if bottom_y_p + 10 <= bottom_y:
                                    self.is_dead = True
                                    interface[4].count += 1
                                    task_enemy -= 1
                                    death_enemy.set_volume(0.1)
                                    death_enemy.play(loops = 0)
                                            
                #right angle
                if bottom_y_p >= self.y:
                    if left_x_p + 33 <= right_x:
                        if right_x_p - 30 >= right_x:
                            if top_y_p + 20 <= self.y:
                                if bottom_y_p + 10 <= bottom_y:
                                    self.is_dead = True
                                    interface[4].count += 1
                                    task_enemy -= 1
                                    death_enemy.set_volume(0.1)
                                    death_enemy.play(loops = 0)
        return task_enemy

    def dead_count(self, list_chicken, droped_resources): #CHANGE SPRITE DEATH AND THEN DROPE A MEAT
        if self.death_count == 6:
            meat1 = Discarded_Item(x = self.x, y = self.y, width = 50, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
            droped_resources.append(meat1)
            list_chicken.remove(self)
            self.x = 10000
            self.y = 10000
        else:
            if self.sprite_frequency_chicken >= 10: 
                self.death_count += 1
                self.sprite_frequency_chicken = 0
            else: self.sprite_frequency_chicken += 1