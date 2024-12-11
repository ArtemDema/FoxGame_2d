import pygame
import modules as mod

pygame.init()

tick = pygame.time.Clock()

#saves the last motion vector (0 - left, 1 - right)
last_side = 0

reload_chest = 0

#counters (elements for the array) for changing the sprite:
idle_count = 0
run_count = 0
crouch_count = 0

#sprite change frequency
number_for_choose_sprite = 10

#getting information from the last session
mod.get_info(WIDTH = mod.WIDTH, HEIGHT = mod.HEIGHT, player_hp = mod.player.hp)

game_run = True
while game_run:
    tick.tick(60) #set the number of fps

    keys = pygame.key.get_pressed() #getting keys to process pressed keys

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mod.save_info(WIDTH = mod.WIDTH, HEIGHT = mod.HEIGHT, player_hp = mod.player.hp)
            game_run = False

    #CHEST 
      #OPEN AND HIDE IN HIM
    if keys[pygame.K_e]:
        if reload_chest == 2:
            if mod.with_chest == False:
                for chest in mod.chests:
                    answer = chest.check_open(mod.key.count, mod.player)
                    if answer: mod.key.count -= 1
                    elif answer == False: mod.hide = True
                reload_chest = 0
        else:
            reload_chest += 1
      #UP THE CHEST
    if keys[pygame.K_q]:
        for chest in mod.chests:
            answer = chest.check_up_the_chest(mod.player)
            if answer:
                if mod.with_chest == False:
                    mod.with_chest = True
                    mod.player.height = 140
                    for block in mod.blocks:
                        block.y += 60
                    for recource in mod.droped_resources:
                        recource.y += 60
                    for chest in mod.chests:
                        chest.y += 60



    #MOVE
      #LEFT
    if keys[pygame.K_a]:
        mod.move_crouch = False
        mod.hide = False
        dict_left = mod.check_run(mod.player.x, mod.player.y, mod.player.width, mod.player.height, mod.move_jump, mod.player.speed, "left")
        if "move_left" in dict_left: mod.move_left = dict_left["move_left"]
        last_side = dict_left["last_side"]
    else:
        mod.move_left = False
    
      #RIGHT
    if keys[pygame.K_d]:
        mod.move_crouch = False
        mod.hide = False
        dict_right = mod.check_run(mod.player.x, mod.player.y, mod.player.width, mod.player.height, mod.move_jump, mod.player.speed, "right")
        if "move_right" in dict_right: mod.move_right = dict_right["move_right"]
        last_side = dict_right["last_side"]
    else:
        mod.move_right = False

      #JUMP
    if mod.with_chest == False:
        if mod.move_jump == False:          #если игрок сейчас не прыгает
            if keys[pygame.K_SPACE]:    #и потом он нажимает space
                if mod.move_bottom == False: #если он сейчас не падает
                    mod.move_jump = True        #то мы говорим что он сейчас будет прыгать
                    mod.hide = False
        else:
            list = mod.player.strength_jump = mod.check_jump(mod.player.x, mod.player.y, mod.player.width, 
                                                    mod.player.height, mod.player.strength_jump, mod.blocks, mod.player.speed)
            if "move_jump" in list: mod.move_jump = list["move_jump"]
            if "player_strength_jump" in list: mod.player.strength_jump = list["player_strength_jump"]

      #SQUAT
    if keys[pygame.K_LSHIFT]:
        if mod.move_bottom == False and mod.move_jump == False and mod.move_right == False and mod.move_left == False and mod.hide == False and mod.with_chest == False:
            mod.move_crouch = True
    else:
        mod.move_crouch = False

    #GRAVITY
      #PLAYER GRAVITY
    for block in mod.blocks:
        answer_fall = block.check_collision_top_wall(mod.player.x, mod.player.y, #checking whether the player is standing on some block
                                                     mod.player.x + mod.player.width, mod.player.y + mod.player.height)
        if answer_fall: #if the player is standing on some block
            mod.move_bottom = False
            break
    if answer_fall != True: #if he does not
        if mod.move_jump == False:
            mod.move_bottom = True
            for block in mod.blocks:
                block.y -= mod.player.speed
            for recource in mod.droped_resources:
                recource.y -= mod.player.speed
            for chest in mod.chests:
                chest.y -= mod.player.speed
      #RESOURCES GRAVITY
    for recource in mod.droped_resources:
        recource.gravity(mod.player)


    #COLLECT RECOURCES
    for recource in mod.droped_resources:
        return_dict = recource.check_collect_recource(mod.player, mod.meat.count, mod.egg.count, mod.key.count)
        if "egg_count" in return_dict: mod.egg.count = return_dict["egg_count"]
        if "key_count" in return_dict: mod.key.count = return_dict["key_count"]
        if "meat_count" in return_dict: mod.meat.count = return_dict["meat_count"]

    #DRAWING
    return_dict = mod.render(mod.move_left, mod.move_right, mod.move_jump, mod.move_crouch, mod.move_bottom, mod.screen, 
                             mod.player, last_side, number_for_choose_sprite, idle_count, crouch_count, run_count, mod.hide, mod.with_chest)
    if "run_count" in return_dict: run_count = return_dict["run_count"]
    if "idle_count" in return_dict: idle_count = return_dict["idle_count"]
    if "crouch_count" in return_dict: crouch_count = return_dict["crouch_count"]
    if "number_for_choose_sprite" in return_dict: number_for_choose_sprite = return_dict["number_for_choose_sprite"]