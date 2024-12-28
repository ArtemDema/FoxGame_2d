from ...main_classes import Enemy
from ...resourses import droped_resources, Discarded_Item
from ...chest import chests
from ...screen import blocks
from ...interface import interface

import random, math

list_idle_frog = ["images/enemy/frog/idle/0.png","images/enemy/frog/idle/1.png","images/enemy/frog/idle/2.png","images/enemy/frog/idle/3.png"]

list_jump_frog = ["images/enemy/frog/jump/0.png","images/enemy/frog/jump/1.png"]


class Frog(Enemy):
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
        self.frequency_jump = 60
        super().__init__(x, y, width, height, image, hp, speed)

    def move(self, player): #MOVE JUMP
        left_x_p = player.x
        right_x_p = player.x + player.width
        top_y_p = player.y
        bottom_y_p = player.y + player.height
        right_x = self.x + self.width
        bottom_y = self.y + self.height

        if self.player_visibility:
            if player.hide == False:
                if self.frequency_jump == 0:
                    if self.angle == 0:
                        distance = player.x - self.x
                        if distance <= 0:
                            self.angle = -135
                            self.vector_move = 0
                        else:
                            self.angle = -45
                            self.vector_move = 1
                        self.frequency_jump = 60
                else:
                    self.frequency_jump -= 1

        #top corner
        if left_x_p + 20 <= self.x:
            if top_y_p + 30 <= self.y:
                if bottom_y_p - 5 >= self.y:
                    if right_x_p - 15 >= self.x:
                        player.damage_player()
        
        #middle (golden)
        if left_x_p + 20 <= self.x:
            if top_y_p + 30 >= self.y:
                if bottom_y_p <= bottom_y:
                    if right_x_p - 15 >= self.x:
                        player.damage_player()
                                    
        #bottom corner
        if left_x_p + 20 <= self.x:
            if top_y_p + 30 <= bottom_y:
                if bottom_y_p >= bottom_y:
                    if right_x_p - 15 >= self.x:
                        player.damage_player()
        
        #top corner
        if left_x_p + 15 <= right_x:
            if top_y_p + 30 <= self.y:
                if bottom_y_p - 5 >= self.y:
                    if right_x_p - 20 >= right_x:
                        player.damage_player()
        
        #middle (golden)
        if left_x_p + 15 <= right_x:
            if top_y_p + 30 >= self.y:
                if bottom_y_p <= bottom_y:
                    if right_x_p - 20 >= right_x:
                            player.damage_player()

        #bottom corner                            
        if left_x_p + 15 <= right_x:
            if top_y_p + 30 <= bottom_y:
                if bottom_y_p >= bottom_y:
                    if right_x_p - 20 >= right_x:
                        player.damage_player()

        if self.angle < 0:
            for_jump = math.pi / 180
            if self.angle == -135:
                if self.vector_move == 0:

                    for block in blocks: #CHECKING IF THERE IS SOIL AT THE FUTURE LOCATION OF THE POINT
                        answer = block.check_collision_top_wall(self.x - 55, self.y, self.x + self.width - 55, self.y + self.height + 20)
                        if answer:
                            break
                        
                    if answer:
                        self.x = self.x + 90 * math.cos(self.angle * for_jump)
                        self.y = self.y + 90 * math.sin(self.angle * for_jump)
                        self.angle = 0
                    else:
                        self.angle = 0
                else:
                    self.angle = 0
            else:
                if self.vector_move == 1:
                    for block in blocks: #CHECKING IF THERE IS SOIL AT THE FUTURE LOCATION OF THE POINT
                        answer = block.check_collision_top_wall(self.x + 55, self.y, self.x + self.width + 55, self.y + self.height + 20)
                        if answer:
                            break
                        
                    if answer:
                        self.x = self.x + 90 * math.cos(self.angle * for_jump)
                        self.y = self.y + 90 * math.sin(self.angle * for_jump)
                        self.angle = 0
                    else:
                        self.angle = 0
                else:
                    self.angle = 0

        elif self.random_idle >= 0:
            self.random_idle -= 1
            if self.idle_count == 3: 
                self.idle_count = 0
            else:
                if self.sprite_frequency_frog == 10: 
                    self.idle_count += 1
                    self.sprite_frequency_frog = 0
                else: self.sprite_frequency_frog += 1
            return
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

    def check_death(self, left_x_p, top_y_p, right_x_p, bottom_y_p): #CHECK DEATH CHICKEN
        if self.is_dead == False:
            for chest in chests:
                answer = chest.check_collision_bottom_wall(self.x, self.y, #CHECK CHEST FOR DEATH
                                                        self.x + self.width, self.y + self.height)
                if answer:
                    self.is_dead = True
                    interface[4].count += 1

            right_x = self.x + self.width
            bottom_y = self.y + self.height
            #left angle
            if bottom_y_p >= self.y:
                if left_x_p + 33 <= self.x:
                    if right_x_p - 30 >= self.x:
                        if top_y_p + 20 <= self.y:
                            if bottom_y_p + 10 <= bottom_y:
                                self.is_dead = True
                                interface[4].count += 1

            #middle (golden)
            if bottom_y_p >= self.y:
                if left_x_p + 33 >= self.x:
                    if right_x_p - 30 <= right_x:
                        if top_y_p + 20 <= self.y:
                            if bottom_y_p + 10 <= bottom_y:
                                self.is_dead = True
                                interface[4].count += 1
                                        
            #right angle
            if bottom_y_p >= self.y:
                if left_x_p + 33 <= right_x:
                    if right_x_p - 30 >= right_x:
                        if top_y_p + 20 <= self.y:
                            if bottom_y_p + 10 <= bottom_y:
                                self.is_dead = True
                                interface[4].count += 1


    def dead_count(self): #CHANGE SPRITE DEATH AND THEN DROPE A MEAT
        if self.death_count == 6:
            meat1 = Discarded_Item(x = self.x, y = self.y, width = 50, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
            droped_resources.append(meat1)
            list_frog.remove(self)
        else:
            if self.sprite_frequency_frog >= 10: 
                self.death_count += 1
                self.sprite_frequency_frog = 0
            else: self.sprite_frequency_frog += 1

list_frog = []

frog1 = Frog(400, 660, 45, 45, "images/enemy/frog/idle/0.png", 3, 2, 2, 0, 0, False)

list_frog.append(frog1)