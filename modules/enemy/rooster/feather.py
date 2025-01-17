from ...main_classes import Settings
import math

class Feather(Settings):
    def __init__(self, x, y, width, height, image, angle):
        self.angle = angle
        super().__init__(x, y, width, height, image)

    def move(self, WIDTH, HEIGHT):
        self.x = self.x + 4 * math.cos(self.angle * math.pi / 180)
        self.y = self.y + 4 * math.sin(self.angle * math.pi / 180)

        if self.x + self.width <= 0 or self.x >= WIDTH or self.y >= HEIGHT or self.y + self.height <= 0:
            list_feather.remove(self)


list_feather = []