from ..main_classes import Settings

import pygame

interface = []

class Column_Meat_Egg_Hp_Key(Settings):
    """
    ### Class for viewing items of player
    """
    def __init__(self, x, y, width, height, image, count, number_y):
        self.number_y = number_y
        self.count = count
        super().__init__(x, y, width, height, image)
    
    def print_text(self, screen): #DRAWING NUMBER IN INTERFACE
        if self.count != 99:
            f1 = pygame.font.Font(None, 32)
            text1 = f1.render(f"{self.count}", 1, (255, 255, 255))
            screen.blit(text1, (self.x + self.width + 10, self.number_y))

meat = Column_Meat_Egg_Hp_Key(220, 25, 55, 30, "images/resources/meat.png", 0, 32)
egg = Column_Meat_Egg_Hp_Key(340, 24, 23, 30, "images/resources/egg.png", 19, 32)
key = Column_Meat_Egg_Hp_Key(420, 28, 35, 25, "images/resources/key.png", 0, 32)
frog = Column_Meat_Egg_Hp_Key(1115, 18, 40, 40, "images/enemy/frog/idle/0.png", 0, 32)
chicken = Column_Meat_Egg_Hp_Key(1015, 18, 40, 40, "images/enemy/chicken/idle/0.png", 0, 32)
rooster = Column_Meat_Egg_Hp_Key(915, 18, 40, 40, "images/enemy/rooster/idle/0.png", 0, 32)
chick = Column_Meat_Egg_Hp_Key(825, 25, 30, 30, "images/enemy/chick/0.png", 0, 32)

interface.append(meat)
interface.append(egg)
interface.append(key)
interface.append(frog)
interface.append(chicken)
interface.append(rooster)
interface.append(chick)

hearts = []