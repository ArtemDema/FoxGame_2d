from ..main_classes import Settings

import pygame

interface = []

class Column_Meat_Egg_Hp_Key(Settings):
    """
    ### Class for viewing items of player
    """
    def __init__(self, x, y, width, height, image, count):
        self.count = count
        super().__init__(x, y, width, height, image)
    
    def print_text(self, screen): #DRAWING NUMBER IN INTERFACE
        f1 = pygame.font.Font(None, 32)
        text1 = f1.render(f"{self.count}", 1, (255, 255, 255))
        screen.blit(text1, (self.x + self.width + 10, 23))

meat = Column_Meat_Egg_Hp_Key(20, 15, 55, 30, "images/resources/meat.png", 0)
egg = Column_Meat_Egg_Hp_Key(140, 14, 23, 30, "images/resources/egg.png", 0)
key = Column_Meat_Egg_Hp_Key(220, 18, 35, 25, "images/resources/key.png", 0)
hp = Column_Meat_Egg_Hp_Key(1100, 19, 27, 27, "images/resources/heart.png", 0)
frog = Column_Meat_Egg_Hp_Key(1000, 8, 40, 40, "images/enemy/frog/idle/0.png", 0)
chicken = Column_Meat_Egg_Hp_Key(900, 8, 40, 40, "images/enemy/chicken/idle/0.png", 0)
rooster = Column_Meat_Egg_Hp_Key(800, 8, 40, 40, "images/enemy/rooster/idle/0.png", 0)

interface.append(meat)
interface.append(egg)
interface.append(key)
interface.append(hp)
interface.append(frog)
interface.append(chicken)
interface.append(rooster)