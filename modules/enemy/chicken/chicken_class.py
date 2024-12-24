from ...main_classes import Enemy
from ...screen import blocks
from ...chest import chests
from ...resourses import Discarded_Item, droped_resources

import random

list_idle = []

list_run_chicken = ["images/enemy/chicken/run/0.png", "images/enemy/chicken/run/1.png", 
                    "images/enemy/chicken/run/2.png", "images/enemy/chicken/run/3.png"]

list_jump = []

class Chicken(Enemy):
    def __init__(self, x, y, width, height, image, hp, speed, 
                 vector_move, run_count, sprite_frequency_chicken,
                 random_idle, random_move, is_dead, death_count):
        self.vector_move = vector_move
        self.run_count = run_count
        self.sprite_frequency_chicken = sprite_frequency_chicken
        self.random_idle = random_idle
        self.random_move = random_move
        self.is_dead = is_dead
        self.death_count = death_count
        self.player_visibility = False
        super().__init__(x, y, width, height, image, hp, speed)

    def move(self, player): #FUNCTION MOVE
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
                    for block in blocks: #CHECK TOUCH RIGHT WALL OF BLOCK
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
                    
                    for chest in chests: #CHECK TOUCH RIGHT WALL OF CHEST
                        answer = chest.check_collision_right_wall(self.x, self.y, 
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
                    for block in blocks: #CHECK TOUCH RIGHT WALL OF BLOCK
                        answer = block.check_collision_left_wall(self.x, self.y, 
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

                    for chest in chests: #CHECK TOUCH RIGHT WALL OF CHEST
                        answer = chest.check_collision_left_wall(self.x, self.y, 
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

    def check_death(self, left_x_p, top_y_p, right_x_p, bottom_y_p): #CHECK DEATH CHICKEN
        for chest in chests: 
            answer = chest.check_collision_bottom_wall(self.x, self.y, #CHECK CHEST FOR DEATH
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
            list_chicken.remove(self)
        else:
            if self.sprite_frequency_chicken >= 10: 
                self.death_count += 1
                self.sprite_frequency_chicken = 0
            else: self.sprite_frequency_chicken += 1


list_chicken = []

chicken1 = Chicken(500, 680, 40, 40, "images/enemy/chicken/run/0.png", 3, 2, 2, 0, 0, 0, 0, False, 0)

list_chicken.append(chicken1)