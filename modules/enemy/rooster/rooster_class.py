from ...main_classes import Enemy
from ...screen import blocks

list_idle = []

list_run = []

list_jump = []


class Rooster(Enemy):
    def __init__(self, x, y, width, height, image, hp, speed, vector_move):
        self.vector_move = vector_move
        super().__init__(x, y, width, height, image, hp, speed)

    def move(self):
        if self.vector_move == "left":
            for block in blocks:
                answer = block.check_collision_right_wall(self.x, self.y, 
                                                        self.x + self.width, self.y + self.height)
                if answer:
                    self.vector_move = "right"
                    return
            if answer != True:
                self.x -= self.speed
        else:
            for block in blocks:
                answer = block.check_collision_left_wall(self.x, self.y, 
                                                        self.x + self.width, self.y + self.height)
                if answer:
                    self.vector_move = "left"
                    return
            if answer != True:
                self.x += self.speed

rooster1 = Rooster(1025, 650, 40, 40, "images/enemy/rooster/run/0.png", 3, 3, "right")