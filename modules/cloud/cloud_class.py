from ..main_classes import Settings

import random

class Cloud(Settings):
    """
    ### Cloud class
    """
    def __init__(self, x, y, width, height, image):
        self.speed = random.randint(1, 2)
        super().__init__(x, y, width, height, image)
    
    def move(self):
        if self.x  + self.width <= 0:
            return True

        if self.speed == 1:
            self.x -= self.speed - 0.5
        else:
            self.x -= self.speed - 1.3