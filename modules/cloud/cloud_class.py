from ..main_classes import Settings

import random

class Cloud(Settings):
    def __init__(self, x, y, width, height, image):
        self.time_life = random.randint(1000, 2000)
        self.speed = random.randint(1, 2)
        super().__init__(x, y, width, height, image)
    
    def move(self):
        if self.time_life <= 0:
            return True
        else: self.time_life -= 1

        self.x -= self.speed