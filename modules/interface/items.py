from ..main_classes import Settings
from ..screen.hero import player

import pygame

interface = []

class Column_Meat_Egg_Hp_Key(Settings):
    def __init__(self, x, y, width, height, image, count):
        self.count = count
        super().__init__(x, y, width, height, image)
    
    def print_text(self, screen):
        f1 = pygame.font.Font(None, 42)
        text1 = f1.render(f"{self.count}", 1, (255, 255, 255))
        screen.blit(text1, (self.x + self.width + 10, 33))

meat = Column_Meat_Egg_Hp_Key(20, 20, 80, 50, "images/resources/meat.png", 0)
egg = Column_Meat_Egg_Hp_Key(140, 20, 40, 50, "images/resources/egg.png", 0)
key = Column_Meat_Egg_Hp_Key(220, 25, 50, 40, "images/resources/key.png", 0)
hp = Column_Meat_Egg_Hp_Key(1100, 20, 50, 50, "images/resources/heart.png", player.hp)

interface.append(meat)
interface.append(egg)
interface.append(key)
interface.append(hp)