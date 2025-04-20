from ..main_classes import BackGround, TileBlock, Settings
from .screen import WIDTH, HEIGHT
from ..tree import Tree
from ..box import Box
from ..chest import Chest
from ..enemy import Frog, Chicken, Rooster, Opossum
from ..bush import Bush
from ..water import Water
from ..resourses import Discarded_Item

import random, pytmx, os

map = [ [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","e"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","e"," "," "," ","b"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," ","e","5"," "," "," "," "," "," "," "," "," ","e"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","b"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","e"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," ","b","7"," "," "," "," "," "," "," "," "," ","b"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","5","b","e"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","6","b"," "," "," "," "," "," "," "," ","e"," "," ","e"," "," "," "," ","e","6"," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," ","h"," "," "," "," "," ","b"," "," "," "," "," "," "," "," "," "," "," "," "," ","e"," ","h"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","b","e"," "," "," "," "," "," "," ","b"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","e","6"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","e"," "," "," "," "," "," "," "," ","7","b"," "," "," "," "," "," ","f","6"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["e"," "," "," "," ","h"," "," ","s","e"," "," "," "," "," "," "," "," "," "," "," ","e"," "," ","7","7"," "," "," "," "," "," "," "," "," "," "," "," ","e","6"," "," "," "," "," "," "," "," "," "," "," "," ","b"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["b","b"," "," "," ","s","b"," "," "," "," "," "," ","b"," "," "," "," "," "," "," "," ","b","e","6"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","b"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["6","b"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","b"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," ","e"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","e"," "," "," "," "," "," "," "," "," "," ","b","e"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," ","b"," "," "," "," ","e","b"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","6"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","7","7"," "," "," "," "," "," "],
        [" "," ","b"," ","h","s"," ","b","b","b"," "," "," "," "," "," "," ","8","r"," "," "," ","h"," "," ","f"," "," ","8"," "," "," "," ","s","f"," "," "," "," "," "," "," ","8","f"," "," "," "," "," "," "," ","s"," "," ","r"," "," "," ","8"," ","b"," "," ","s","h"," "," ","b"," "," "," ","b","7","8"," ","f","c"," "," ","r"," ","e","b","b","6"," ","s","h","n"," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","w","w"," "," "," "," "," "," "," "," ","w","w","w","w","w","w"," "," "," ","w","w","w"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","w","w","w"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","d","d"," "," "," "," "," "," "," "," ","d","d","d","d","d","d"," "," "," ","d","d","d"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","d","d","d"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]

blocks = []
list_trees = []
list_of_clouds = []
chests = []
boxes = []
list_rooster = []
list_chicken = []
list_opossum = []
list_frog = []
list_enemy = []
list_bush = []
list_big_boss_tree = []
droped_resources = []
list_water = []

# - Nothing
#8 - tree
#o - opossum
#c - chest
#b - box
#7 - box with egg
#6 - box with meat
#5 - box with key
#f - frog
#r - rooster
#h - chicken/hen
#s - shrub
#m - meat
#t - heart
#e - egg
#k - key
#w - water
#d - deep water
#n - end of level

path = os.path.abspath(__file__ + "\..\..\..\levels")

level = pytmx.load_pygame(path + "/first_screen.tmx")

layer = level.get_layer_by_name("Слой тайлов 1")

for x, y, tileSurface in layer.tiles():
    tile =  TileBlock(x = x * 50, y = y * 50, width = 50, height = 50, image = tileSurface)
    blocks.append(tile)


background = BackGround(x = 0, y = 0, width = WIDTH, height = HEIGHT, image = "images/screen/first.jpg")

for idy, row in enumerate(map):
    for idx, column in enumerate(row):       
        if column == "8":
            tree = Tree(x = 50 * idx - 5, y = 50 * idy - 234, width = 0, height = 0, #change size in load_all_image.py
                        image ="images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0000.png", 
                        random_egg = random.randint(0, 1), sprite_frequency_tree=random.randint(0, 10))
            list_trees.append(tree)

        elif column == "c":
            chest = Chest(x = 50 * idx, y = 50 * idy, width = 50, height = 50, image = "images/chest/chest_lock.png", open_chest = False)
            chests.append(chest)

        elif column == "b":
            box = Box(x = 50 * idx, y = 50 * idy, width = 50, height = 50, image = "images/box/box_lock.png", random_item = " ")
            boxes.append(box)
        
        elif column == "7":
            box = Box(x = 50 * idx, y = 50 * idy, width = 50, height = 50, image = "images/box/box_lock.png", random_item = "egg")
            boxes.append(box)

        elif column == "6":
            box = Box(x = 50 * idx, y = 50 * idy, width = 50, height = 50, image = "images/box/box_lock.png", random_item = "meat")
            boxes.append(box)
        
        elif column == "5":
            box = Box(x = 50 * idx, y = 50 * idy, width = 50, height = 50, image = "images/box/box_lock.png", random_item = "key")
            boxes.append(box)

        elif column == "f":
            frog = Frog(50 * idx, 50 * idy - 10, 60, 60, "images/enemy/frog/idle/0.png", 3, 2, 2, 0, 0, False)
            list_frog.append(frog)
            list_enemy.append(frog)

        elif column == "o":
            opossum = Opossum(50 * idx, 50 * idy - 40, 60, 60, "images/enemy/opossum/0.png", 3, 2, 2, 0, 0, False)
            list_opossum.append(opossum)
            list_enemy.append(opossum)

        elif column == "r":
            rooster = Rooster(50 * idx, 50 * idy - 10, 63, 63, "images/enemy/rooster/idle/0.png", 3, 2, 0, 0, False, 0)
            list_rooster.append(rooster)
            list_enemy.append(rooster)

        elif column == "h":
            chicken = Chicken(50 * idx, 50 * idy, 40, 50, "images/enemy/chicken/run/0.png", 3, 2, 2, 0, 0, 0, 0, False, 0)
            list_chicken.append(chicken)
            list_enemy.append(chicken)
        
        elif column == "s":
            bush = Bush(50 * idx, 50 * idy - 13, 105, 65, f"images/bush/{random.randint(0,6)}.png")
            list_bush.append(bush)

        elif column == "m":
            meat1 = Discarded_Item(x = 50 * idx, y = 50 * idy, width = 40, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
            droped_resources.append(meat1)

        elif column == "t":
            heart1 = Discarded_Item(x = 50 * idx, y = 50 * idy, width = 25, height = 25, image = "images/resources/heart.png", whatIsThis= "heart")
            droped_resources.append(heart1)

        elif column == "e":
            egg1 = Discarded_Item(x = 50 * idx + 13, y = 50 * idy, width = 25, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
            droped_resources.append(egg1)

        elif column == "k":
            key1 = Discarded_Item(x = 50 * idx, y = 50 * idy, width = 30, height = 22, image = "images/resources/key.png", whatIsThis= "key")
            droped_resources.append(key1)
        
        elif column == "w":
            water = Water(x = 50 * idx, y = 50 * idy, width = 50, height = 50, image = "images/water/0.png")
            list_water.append(water)
        
        elif column == "d":
            water = Water(x = 50 * idx, y = 50 * idy, width = 50, height = 50, image = "images/water/2.png")
            list_water.append(water)
        
        elif column == "n":
            end_of_level = Settings(x = 50 * idx, y = 50 * idy - 50, width = 80, height = 100, image = "images/screen/end.png")
