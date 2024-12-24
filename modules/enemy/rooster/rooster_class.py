from ...main_classes import Enemy
from ...screen import blocks
from ...box import boxes
from ...chest import chests
from ...resourses import droped_resources, Discarded_Item

import random

list_run_rooster = ["images/enemy/rooster/run/0.png", "images/enemy/rooster/run/1.png", 
                    "images/enemy/rooster/run/2.png", "images/enemy/rooster/run/3.png"]

list_jump = []

class Rooster(Enemy):
    def __init__(self, x, y, width, height, image, hp, speed, vector_move, sprite_frequency_rooster, is_dead, death_count):
        self.vector_move = vector_move
        self.run_count = 0
        self.random_idle = 0
        self.random_move = 0
        self.sprite_frequency_rooster = sprite_frequency_rooster
        self.is_dead = is_dead
        self.death_count = death_count
        self.player_visibility = False
        super().__init__(x, y, width, height, image, hp, speed)

    def move(self, player): #RUN ROOSTER
        if self.player_visibility:
            if player.hide == False:
                if self.random_move <= 0:
                    distance = player.x - self.x
                    if distance <= 0:
                        self.random_move = 200
                        self.vector_move = 0
                    else:
                        self.random_move = 200
                        self.vector_move = 1

        left_x_p = player.x
        right_x_p = player.x + player.width
        top_y_p = player.y
        bottom_y_p = player.y + player.height
        right_x = self.x + self.width
        bottom_y = self.y + self.height
        if self.random_move >= 0:
            if self.vector_move == 0:

                if left_x_p + 15 <= right_x:
                    if top_y_p + 30 <= self.y:
                        if bottom_y_p - 5 >= self.y:
                            if right_x_p - 20 >= right_x:
                                if player.hide == False:
                                    player.damage_player()
            
                #middle (golden)
                if left_x_p + 15 <= right_x:
                    if top_y_p + 30 >= self.y:
                        if bottom_y_p <= bottom_y:
                            if right_x_p - 20 >= right_x:
                                    if player.hide == False:
                                        player.damage_player()

                #bottom corner                            
                if left_x_p + 15 <= right_x:
                    if top_y_p + 30 <= bottom_y:
                        if bottom_y_p >= bottom_y:
                            if right_x_p - 20 >= right_x:
                                if player.hide == False:
                                    player.damage_player()

                for block in blocks: #CHECKING IF THERE IS SOIL AT THE FUTURE LOCATION OF THE POINT
                    answer = block.check_collision_top_wall(self.x - 15, self.y, self.x + self.width - 15, self.y + self.height + 20)
                    if answer:
                        break
                    
                if answer:
                    for block in blocks: #CHECK TOUCH RIGHT WALL OF BLOCK
                        answer = block.check_collision_right_wall(self.x, self.y, 
                                                                self.x + self.width, self.y + self.height)
                        if answer:
                            if self.run_count == 3: 
                                self.run_count = 0
                            else:
                                if self.sprite_frequency_rooster >= 10: 
                                    self.run_count += 1
                                    self.sprite_frequency_rooster = 0
                                else: self.sprite_frequency_rooster += 1
                            self.random_move =- 1
                            return
                    
                    for chest in chests: #CHECK TOUCH RIGHT WALL OF CHEST
                        answer = chest.check_collision_right_wall(self.x, self.y, 
                                                                self.x + self.width, self.y + self.height)
                        if answer:
                            if self.run_count == 3: 
                                self.run_count = 0
                            else:
                                if self.sprite_frequency_rooster >= 10: 
                                    self.run_count += 1
                                    self.sprite_frequency_rooster = 0
                                else: self.sprite_frequency_rooster += 1
                            self.random_move =- 1
                            return

                    if answer != True:
                        self.x -= self.speed
                        self.random_move -= self.speed

                        if self.run_count == 3: 
                            self.run_count = 0
                        else:
                            if self.sprite_frequency_rooster >= 10: 
                                self.run_count += 1
                                self.sprite_frequency_rooster = 0
                            else: self.sprite_frequency_rooster += 1
                else:
                    self.random_move = -1
            else:
                #top corner
                if left_x_p + 20 <= self.x:
                    if top_y_p + 30 <= self.y:
                        if bottom_y_p - 5 >= self.y:
                            if right_x_p - 15 >= self.x:
                                if player.hide == False:
                                    player.damage_player()
                
                #middle (golden)
                if left_x_p + 20 <= self.x:
                    if top_y_p + 30 >= self.y:
                        if bottom_y_p <= bottom_y:
                            if right_x_p - 15 >= self.x:
                                if player.hide == False:
                                    player.damage_player()
                                            
                #bottom corner
                if left_x_p + 20 <= self.x:
                    if top_y_p + 30 <= bottom_y:
                        if bottom_y_p >= bottom_y:
                            if right_x_p - 15 >= self.x:
                                if player.hide == False:
                                    player.damage_player()

                for block in blocks: #CHECKING IF THERE IS SOIL AT THE FUTURE LOCATION OF THE POINT
                    answer = block.check_collision_top_wall(self.x + 15, self.y, self.x + self.width + 15, self.y + self.height + 20)
                    if answer:
                        break
                    
                if answer:
                    for block in blocks: #CHECK TOUCH RIGHT WALL OF BLOCK
                        answer = block.check_collision_left_wall(self.x, self.y, 
                                                                self.x + self.width, self.y + self.height)
                        if answer:
                            if self.run_count == 3: 
                                self.run_count = 0
                            else:
                                if self.sprite_frequency_rooster >= 10: 
                                    self.run_count += 1
                                    self.sprite_frequency_rooster = 0
                                else: self.sprite_frequency_rooster += 1
                            self.random_move =- 1
                            return

                    for chest in chests: #CHECK TOUCH RIGHT WALL OF CHEST
                        answer = chest.check_collision_left_wall(self.x, self.y, 
                                                                self.x + self.width, self.y + self.height)
                        if answer:
                            if self.run_count == 3: 
                                self.run_count = 0
                            else:
                                if self.sprite_frequency_rooster >= 10: 
                                    self.run_count += 1
                                    self.sprite_frequency_rooster = 0
                                else: self.sprite_frequency_rooster += 1
                            self.random_move =- 1
                            return

                    if answer != True:
                        self.x += self.speed
                        self.random_move -= self.speed

                        if self.run_count == 3: 
                            self.run_count = 0
                        else:
                            if self.sprite_frequency_rooster == 10: 
                                self.run_count += 1
                                self.sprite_frequency_rooster = 0
                            else: self.sprite_frequency_rooster += 1
                else:
                    self.random_move = -1
        elif self.random_idle >= 0:
            self.random_idle -= 1
            return
        else:
            self.actions_rooster()

    def actions_rooster(self): #RANDOM ACTION
        random_antion = random.randint(0, 1)
        if random_antion == 0:
            self.random_idle = random.randint(120, 260)
        else:
            self.vector_move = random.randint(0, 1)
            self.random_move = random.randint(50, 250)
    
    def check_death(self, left_x_p, top_y_p, right_x_p, bottom_y_p): #CHECK DEATH ROOSTER
        for box in boxes:
            answer = box.check_collision_bottom_wall(self.x, self.y, #CHECKING TOUCH CHEST
                                                    self.x + self.width, self.y + self.height)
            if answer:
                self.is_dead = True

        right_x = self.x + self.width
        bottom_y = self.y + self.height
        #left angle
        if bottom_y_p >= self.y:
            if left_x_p + 33 <= self.x:
                if right_x_p - 30 >= self.x:
                    if top_y_p + 20 <= self.y:
                        if bottom_y_p + 10 <= bottom_y:
                            self.is_dead = True

        #middle (golden)
        if bottom_y_p >= self.y:
            if left_x_p + 33 >= self.x:
                if right_x_p - 30 <= right_x:
                    if top_y_p + 20 <= self.y:
                        if bottom_y_p + 10 <= bottom_y:
                            self.is_dead = True
                                    
        #right angle
        if bottom_y_p >= self.y:
            if left_x_p + 33 <= right_x:
                if right_x_p - 30 >= right_x:
                    if top_y_p + 20 <= self.y:
                        if bottom_y_p + 10 <= bottom_y:
                            self.is_dead = True

    def dead_count(self): #CHANGE SPRITE DEATH AND THEN DROPE A MEAT
        if self.death_count == 6:
            meat1 = Discarded_Item(x = self.x, y = self.y, width = 50, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
            droped_resources.append(meat1)
            list_rooster.remove(self)
        else:
            if self.sprite_frequency_rooster >= 10: 
                self.death_count += 1
                self.sprite_frequency_rooster = 0
            else: self.sprite_frequency_rooster += 1

list_rooster = []

rooster1 = Rooster(1025, 650, 40, 40, list_run_rooster[0], 3, 2, 0, 0, False, 0)

list_rooster.append(rooster1)