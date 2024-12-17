from ...main_classes import Enemy
from ...screen import blocks
from ...chest import chests

list_run_rooster = ["images/enemy/rooster/run/0.png", "images/enemy/rooster/run/1.png", 
                    "images/enemy/rooster/run/2.png", "images/enemy/rooster/run/3.png"]

list_jump = []

class Rooster(Enemy):
    def __init__(self, x, y, width, height, image, hp, speed, vector_move, run_count, sprite_frequency_rooster):
        self.vector_move = vector_move
        self.run_count = run_count
        self.sprite_frequency_rooster = sprite_frequency_rooster
        super().__init__(x, y, width, height, image, hp, speed)

    def move(self):
        if self.vector_move == 0:
            for block in blocks:
                answer = block.check_collision_right_wall(self.x, self.y, 
                                                        self.x + self.width, self.y + self.height)
                if answer:
                    self.vector_move = 1

                    if self.run_count == 3: 
                        self.run_count = 0
                    else:
                        if self.sprite_frequency_rooster == 10: 
                            self.run_count += 1
                            self.sprite_frequency_rooster = 0
                        else: self.sprite_frequency_rooster += 1
            
            for chest in chests:
                answer = chest.check_collision_right_wall(self.x, self.y, 
                                                        self.x + self.width, self.y + self.height)
                if answer:
                    self.vector_move = 1

                    if self.run_count == 3: 
                        self.run_count = 0
                    else:
                        if self.sprite_frequency_rooster == 10: 
                            self.run_count += 1
                            self.sprite_frequency_rooster = 0
                        else: self.sprite_frequency_rooster += 1

            if answer != True:
                self.x -= self.speed

                if self.run_count == 3: 
                    self.run_count = 0
                else:
                    if self.sprite_frequency_rooster == 7: 
                        self.run_count += 1
                        self.sprite_frequency_rooster = 0
                    else: self.sprite_frequency_rooster += 1
        else:
            for block in blocks:
                answer = block.check_collision_left_wall(self.x, self.y, 
                                                        self.x + self.width, self.y + self.height)
                if answer:
                    self.vector_move = 0

                    if self.run_count == 3: 
                        self.run_count = 0
                    else:
                        if self.sprite_frequency_rooster == 7: 
                            self.run_count += 1
                            self.sprite_frequency_rooster = 0
                        else: self.sprite_frequency_rooster += 1

            for chest in chests:
                answer = chest.check_collision_left_wall(self.x, self.y, 
                                                        self.x + self.width, self.y + self.height)
                if answer:
                    self.vector_move = 0

                    if self.run_count == 3: 
                        self.run_count = 0
                    else:
                        if self.sprite_frequency_rooster == 10: 
                            self.run_count += 1
                            self.sprite_frequency_rooster = 0
                        else: self.sprite_frequency_rooster += 1

            if answer != True:
                self.x += self.speed

                if self.run_count == 3: 
                    self.run_count = 0
                else:
                    if self.sprite_frequency_rooster == 10: 
                        self.run_count += 1
                        self.sprite_frequency_rooster = 0
                    else: self.sprite_frequency_rooster += 1
    
    def check_death(self):
        for chest in chests:
            answer = chest.check_collision_bottom_wall(self.x, self.y, 
                                                    self.x + self.width, self.y + self.height)
            if answer:
                print("dead")
                self.x = 10000
                self.y = 10000

list_rooster = []

rooster1 = Rooster(1025, 650, 40, 40, list_run_rooster[0], 3, 3, 0, 0, 0)

list_rooster.append(rooster1)