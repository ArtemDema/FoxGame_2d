import os, pygame


#PLAYER----------------------------------------------------------------------------------------------------------------------

list_idle = ["images/player/idle/0.png", "images/player/idle/1.png", 
             "images/player/idle/2.png", "images/player/idle/3.png"]

list_idle_with_chest = ["images/player/idle/with_chest/0.png", "images/player/idle/with_chest/1.png", 
                        "images/player/idle/with_chest/2.png", "images/player/idle/with_chest/3.png"]

list_run = ["images/player/run/0.png", "images/player/run/1.png", 
            "images/player/run/2.png", "images/player/run/3.png",
            "images/player/run/4.png", "images/player/run/5.png"]

list_run_with_chest = ["images/player/run/with_chest/0.png", "images/player/run/with_chest/1.png", 
                        "images/player/run/with_chest/2.png", "images/player/run/with_chest/3.png",
                        "images/player/run/with_chest/4.png", "images/player/run/with_chest/5.png"]

list_jump = ["images/player/jump/player-jump-1.png","images/player/jump/player-jump-2.png",]

list_jump_with_chest = ["images/player/jump/with_chest/0.png",]

list_crouch = ["images/player/crouch/player-crouch-1.png","images/player/crouch/player-crouch-2.png"]

#TREE----------------------------------------------------------------------------------------------------------------------
list_bubble_tree = ["images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0000.png","images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0001.png",
                    "images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0002.png","images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0003.png",
                    "images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0004.png","images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0005.png",
                    "images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0006.png","images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0007.png",
                    "images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0008.png","images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0009.png",
                    "images/tree/Pine tree/Bubble Pine Tree - YELLOW - 0010.png"]

#ROOSTER----------------------------------------------------------------------------------------------------------------------
list_idle_rooster = ["images/enemy/rooster/idle/0.png", "images/enemy/rooster/idle/1.png", 
                    "images/enemy/rooster/idle/2.png", "images/enemy/rooster/idle/3.png"]

list_run_rooster = ["images/enemy/rooster/run/0.png", "images/enemy/rooster/run/1.png", 
                    "images/enemy/rooster/run/2.png", "images/enemy/rooster/run/3.png"]

#FROG----------------------------------------------------------------------------------------------------------------------
list_idle_frog = ["images/enemy/frog/idle/0.png","images/enemy/frog/idle/1.png","images/enemy/frog/idle/2.png","images/enemy/frog/idle/3.png"]

list_jump_frog = ["images/enemy/frog/jump/0.png","images/enemy/frog/jump/1.png"]

#Opossum----------------------------------------------------------------------------------------------------------------------
list_run_opossum = ["images/enemy/opossum/0.png", "images/enemy/opossum/1.png", 
                    "images/enemy/opossum/2.png", "images/enemy/opossum/3.png",
                    "images/enemy/opossum/4.png", "images/enemy/opossum/5.png"]

#CHICKEN----------------------------------------------------------------------------------------------------------------------
list_idle_chicken = ["images/enemy/chicken/idle/0.png", "images/enemy/chicken/idle/1.png", 
            "images/enemy/chicken/idle/2.png", "images/enemy/chicken/idle/3.png"]

list_run_chicken = ["images/enemy/chicken/run/0.png", "images/enemy/chicken/run/1.png", 
                    "images/enemy/chicken/run/2.png", "images/enemy/chicken/run/3.png"]

#WATER----------------------------------------------------------------------------------------------------------------------
list_water_images = ["images/water/0.png","images/water/1.png","images/water/2.png","images/water/3.png","images/water/4.png"]

#CHICK----------------------------------------------------------------------------------------------------------------------
list_chick_image = ["images/enemy/chick/0.png","images/enemy/chick/1.png","images/enemy/chick/2.png","images/enemy/chick/3.png"]

list_chick_egg_image = ["images/resources/imposter_egg/0.png","images/resources/imposter_egg/1.png",
                        "images/resources/imposter_egg/2.png","images/resources/imposter_egg/3.png",
                        "images/resources/imposter_egg/4.png","images/resources/imposter_egg/5.png"]

##LOAD_IMAGE----------------------------------------------------------------------------------------------------------------------

def load_list_image(list_images, width, height):
    for i in range(len(list_images)):
        absolute_path = os.path.abspath(__file__ +"/../../../../")
        absolute_path = os.path.join(absolute_path, list_images[i])
        image = pygame.image.load(absolute_path)
        scaled_image = pygame.transform.scale(image, (width, height))
        image = scaled_image
        list_images[i] = image

load_list_image(list_idle, 80, 80)
load_list_image(list_idle_with_chest, 80, 80)
load_list_image(list_run, 80, 80)
load_list_image(list_run_with_chest, 80, 80)
load_list_image(list_jump, 80, 80)
load_list_image(list_jump_with_chest, 80, 80)
load_list_image(list_crouch, 80, 80)
load_list_image(list_bubble_tree, 159, 284)
load_list_image(list_idle_rooster, 63, 63)
load_list_image(list_run_rooster, 63, 63)
load_list_image(list_run_opossum, 83, 83)
load_list_image(list_idle_frog, 60, 60)
load_list_image(list_jump_frog, 60, 60)
load_list_image(list_idle_chicken, 50, 50)
load_list_image(list_run_chicken, 50, 50)
load_list_image(list_water_images, 50, 50)
load_list_image(list_chick_image, 30, 30)
load_list_image(list_chick_egg_image, 35, 34)