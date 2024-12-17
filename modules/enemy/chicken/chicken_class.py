from ...main_classes import Enemy
from ...screen import blocks
from ...chest import chests

import random

list_idle = []

list_run_chicken = ["images/enemy/chicken/run/0.png", "images/enemy/chicken/run/1.png", 
                    "images/enemy/chicken/run/2.png", "images/enemy/chicken/run/3.png"]

list_jump = []

class Chicken(Enemy):
    def __init__(self, x, y, width, height, image, hp, speed, 
                 vector_move, run_count, sprite_frequency_chicken,
                 random_idle, random_move):
        self.vector_move = vector_move
        self.run_count = run_count
        self.sprite_frequency_chicken = sprite_frequency_chicken
        self.random_idle = random_idle
        self.random_move = random_move
        super().__init__(x, y, width, height, image, hp, speed)

    def move(self):
        if self.random_move >= 0:
            if self.vector_move == 0:
                # for block in blocks:
                #     answer = block.check_collision_top_wall(self.x, self.y, self.x + self.width, self.y + self.height)
                #     if answer != True:
                #         self.random_move = 0

                for block in blocks:
                    answer = block.check_collision_right_wall(self.x, self.y, 
                                                            self.x + self.width, self.y + self.height)
                    if answer:
                        self.vector_move = 1

                        if self.run_count == 3: 
                            self.run_count = 0
                        else:
                            if self.sprite_frequency_chicken >= 10: 
                                self.run_count += 1
                                self.sprite_frequency_chicken = 0
                            else: self.sprite_frequency_chicken += 1
                
                for chest in chests:
                    answer = chest.check_collision_right_wall(self.x, self.y, 
                                                            self.x + self.width, self.y + self.height)
                    if answer:
                        self.vector_move = 1

                        if self.run_count == 3: 
                            self.run_count = 0
                        else:
                            if self.sprite_frequency_chicken >= 10: 
                                self.run_count += 1
                                self.sprite_frequency_chicken = 0
                            else: self.sprite_frequency_chicken += 1

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
                # for block in blocks:
                #     answer = block.check_collision_top_wall(self.x, self.y, self.x + self.width, self.y + self.height)
                #     if answer != True:
                #         self.random_move = 0

                for block in blocks:
                    answer = block.check_collision_left_wall(self.x, self.y, 
                                                            self.x + self.width, self.y + self.height)
                    if answer:
                        self.vector_move = 0

                        if self.run_count == 3: 
                            self.run_count = 0
                        else:
                            if self.sprite_frequency_chicken >= 10: 
                                self.run_count += 1
                                self.sprite_frequency_chicken = 0
                            else: self.sprite_frequency_chicken += 1

                for chest in chests:
                    answer = chest.check_collision_left_wall(self.x, self.y, 
                                                            self.x + self.width, self.y + self.height)
                    if answer:
                        self.vector_move = 0

                        if self.run_count == 3: 
                            self.run_count = 0
                        else:
                            if self.sprite_frequency_chicken >= 10: 
                                self.run_count += 1
                                self.sprite_frequency_chicken = 0
                            else: self.sprite_frequency_chicken += 1

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
        elif self.random_idle >= 0:
            self.random_idle -= 1
            return
        else:
            self.actions_chicken()

    def actions_chicken(self):
        random_antion = random.randint(0, 1)
        if random_antion == 0:
            self.random_idle = random.randint(120, 260)
        else:
            self.vector_move = random.randint(0, 1)
            self.random_move = random.randint(50, 250)

    def check_death(self):
        for chest in chests:
            answer = chest.check_collision_bottom_wall(self.x, self.y, 
                                                    self.x + self.width, self.y + self.height)
            if answer:
                print("dead")
                self.x = 10000
                self.y = 10000

list_chicken = []

chicken1 = Chicken(300, 710, 40, 40, "images/enemy/chicken/run/0.png", 3, 2, 2, 0, 0, 0, 0)

list_chicken.append(chicken1)