import pygame, random
import modules as mod

pygame.init()

tick = pygame.time.Clock()

#saves the last motion vector (0 - left, 1 - right)
last_side = 0

reload_chest = 0
box_player = 0
modal_window_info = False
pause = False

#counters (elements for the array) for changing the sprite:
idle_count = 0
run_count = 0
crouch_count = 0

#sprite change frequency
number_for_choose_sprite = 10
#getting information from the last session
info = mod.get_info()
WIDTH = info["width"]
HEIGHT = info["height"]
mod.player.hp = info["hp"]

#show menu
game_run = mod.main_menu.menu(screen = mod.screen)
while game_run:
    tick.tick(60) #set the number of fps

    if mod.player.hp <= 0:
        game_run = False

    # print(tick.get_fps())

    keys = pygame.key.get_pressed() #getting keys to process pressed keys

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #SAVES INFORMATION
            mod.save_info(WIDTH = mod.WIDTH, HEIGHT = mod.HEIGHT, player_hp = mod.player.hp)
            game_run = False
        
        if event.type == pygame.MOUSEMOTION:
                position_mouse = event.pos
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if modal_window_info:
                modal_window_info = mod.modal_w.check_click(position_mouse[0], position_mouse[1])
            if pause:
                pause = continue_b.check_click(position_mouse_x = position_mouse[0], position_mouse_y = position_mouse[1])
                game_run = exit_b.check_click(position_mouse_x = position_mouse[0], position_mouse_y = position_mouse[1])
                if game_run ==False:
                    mod.save_info(WIDTH = mod.WIDTH, HEIGHT = mod.HEIGHT, player_hp = mod.player.hp)

    #CLOUD--------------------------------------------
    if len(mod.list_of_clouds) < 5:
      for i in range(5 - len(mod.list_of_clouds)):
          cloud = mod.Cloud(x = 1430, 
                            y = -25, 
                            width = random.randint(80, 180),
                            height = random.randint(40, 140), 
                            image = f"images/cloud/cloud_{random.randint(0, 7)}.png")
          mod.list_of_clouds.append(cloud)

    for cloud in mod.list_of_clouds:
        answer = cloud.move()
        if answer:
            mod.list_of_clouds.remove(cloud)
    #--------------------------------------------

    #TREE--------------------------------------------
    for tree in mod.list_trees:
        tree.idle(mod.list_bubble_tree)
        answer = tree.drop_egg(mod.player)
        if answer:
            egg1 = mod.Discarded_Item(x = tree.x + 70, y = tree.y - 30, width = 20, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
            mod.droped_resources.append(egg1)
            tree.ramdom_egg = 0
    #--------------------------------------------

    #ENEMY--------------------------------------------
    for enemy in mod.list_enemy:
        enemy.check_death(mod.player.x, mod.player.y, mod.player.x + mod.player.width, mod.player.y + mod.player.height, mod.chests) #CHECKING IF THE PLAYER IS TRYING TO KILL THE ENEMY
        if enemy.is_dead == False:
            enemy.player_visibility = enemy.player_visibility_zone(mod.player)
            enemy.move(mod.player, mod.blocks, mod.chests, mod.boxes) #ENEMY MOVE

    if len(mod.list_feather) != 0:
        for feather in mod.list_feather:
            feather.move(mod.WIDTH, mod.HEIGHT, mod.player, mod.blocks, mod.chests, mod.boxes)
    #--------------------------------------------

    #CHEST AND BOX--------------------------------------------
      #OPEN AND HIDE IN CHEST
    if keys[pygame.K_e]:
        if reload_chest == 2:
            if mod.with_box == False:
                for chest in mod.chests: #CHECKING AN ATTEMPT TO OPEN A CHEST
                    answer = chest.check_open(mod.key.count, mod.player, mod.droped_resources) #
                    if answer[0]: 
                        mod.key.count -= 1
                        modal_window_info = True
                        claim = answer[1]
                    elif answer[0] == False: 
                        mod.player.hide = True
                        chest.hide_in_him = True
        else:
            reload_chest += 1
      #UP THE BOX
    if keys[pygame.K_q]:
        if mod.player.hide == False and mod.with_box == False:
            for box in mod.boxes: #CHECKING AN ATTEMPT TO UP A BOX 
                answer = box.check_up_the_box(mod.player) #
                if answer:
                    mod.with_box = True
                    box_player = box
                    if box.random_item == "key":
                        key1 = mod.Discarded_Item(x = box.x, y = box.y, width = 35, height = 25, image = "images/resources/key.png", whatIsThis= "key")
                        mod.droped_resources.append(key1)
                        box.random_item = " "
                    elif box.random_item == "egg":
                            egg1 = mod.Discarded_Item(x = box.x, y = box.y, width = 25, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
                            mod.droped_resources.append(egg1)
                            box.random_item = " "
                    elif box.random_item == "meat":
                            meat1 = mod.Discarded_Item(x = box.x, y = box.y, width = 40, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
                            mod.droped_resources.append(meat1)
                            box.random_item = " "
    if mod.with_box:
        box_player.x = mod.player.x + 18
        box_player.y = mod.player.y - 19

      #PUSH THE BOX
    if keys[pygame.K_r]:
        mod.push_box = mod.check_push_box(mod.player, last_side) #BOX PUSH TEST
      
      #DROPE BOX
    if keys[pygame.K_g]:
        if mod.with_box == True:
            mod.with_box = False
            if last_side == 0:
                box_player.throw = True
                box_player.angle = -125
            else:
                box_player.throw = True
                box_player.angle = -55
    #--------------------------------------------

    #MOVE--------------------------------------------
      #LEFT
    if keys[pygame.K_a]:
        mod.move_crouch = False
        mod.player.hide = False

        for chest in mod.chests:
            chest.hide_in_him = False
        if mod.player.x >= 1:
            dict_left = mod.move_left_player(mod.player, mod.move_jump, mod.push_box, mod.with_box, box_player) #FUNCTION FOR PLAYER WALKING TO THE LEFT
            if "move_left" in dict_left: mod.move_left = dict_left["move_left"]
            if "last_side" in dict_left: last_side = dict_left["last_side"]
            if "push_box" in dict_left: mod.push_box = dict_left["push_box"]
    else:
        mod.move_left = False
    
      #RIGHT
    if keys[pygame.K_d]:
        mod.move_crouch = False
        mod.player.hide = False

        for chest in mod.chests:
            chest.hide_in_him = False
        for box in mod.boxes:
            box.hide_in_him = False

        dict_right = mod.move_right_player(mod.player, mod.move_jump, 
                                           mod.push_box, mod.with_box, box_player, mod.WIDTH, mod.droped_resources) #FUNCTION FOR PLAYER WALKING TO THE RIGHT
        if "move_right" in dict_right: mod.move_right = dict_right["move_right"]
        if "last_side" in dict_right: last_side = dict_right["last_side"]
        if "push_box" in dict_right: mod.push_box = dict_right["push_box"]
    else:
        mod.move_right = False

      #JUMP
    if mod.move_jump == False:
        if mod.with_box == False:
            if keys[pygame.K_SPACE]:
                if mod.move_bottom == False:
                    mod.move_jump = True
                    mod.player.hide = False

                    for chest in mod.chests:
                        chest.hide_in_him = False
                    for box in mod.boxes:
                        box.hide_in_him = False
    else:
        list = mod.player.strength_jump = mod.check_jump(mod.player, mod.blocks)
        if "move_jump" in list: mod.move_jump = list["move_jump"]
        if "player_strength_jump" in list: mod.player.strength_jump = list["player_strength_jump"]

      #SQUAT
    if keys[pygame.K_LSHIFT]:
        if mod.move_bottom == False and mod.move_jump == False and mod.move_right == False and mod.move_left == False and mod.player.hide == False and mod.with_box == False:
            mod.move_crouch = True
    else:
        mod.move_crouch = False
    #--------------------------------------------

    #DAMAGE TO THE PLAYER--------------------------------------------
    if mod.player.timer_damage > 0:
        mod.player.timer_damage -= 1
    #--------------------------------------------

    #GRAVITY--------------------------------------------
      #PLAYER GRAVITY
    list_return = mod.gravity(mod.player, mod.move_jump) #PLAYER GRAVITY
    if "move_bottom" in list_return: mod.move_bottom = list_return["move_bottom"]

      #GRAVITY OF RESOURCES AND CHESTS
    mod.gravity_resources(mod.player) #RESOURCE GRAVITY
    mod.gravity_boxes(mod.player) #GRAVITY OF BOX
    mod.gravity_enemy(mod.player) #ENEMIES GRAVITY
    #--------------------------------------------

    #COLLECT RECOURCES--------------------------------------------
    for recource in mod.droped_resources: 
        return_dict = recource.check_collect_recource(mod.player, mod.meat.count, mod.egg.count, mod.key.count, mod.player.hp) #CHECKING FOR SELECTION OF RESOURCES
        if "egg_count" in return_dict: mod.egg.count = return_dict["egg_count"]
        if "key_count" in return_dict: mod.key.count = return_dict["key_count"]
        if "meat_count" in return_dict: mod.meat.count = return_dict["meat_count"]
        if "heart_count" in return_dict: mod.player.hp = return_dict["heart_count"]
    #--------------------------------------------

    #RENDER--------------------------------------------
    return_dict = mod.render(mod.move_left, mod.move_right, mod.move_jump, mod.move_crouch, mod.move_bottom, mod.screen, #DRAWING EVERYTHING
                             mod.player, last_side, number_for_choose_sprite, idle_count, crouch_count, run_count, mod.player.hide, mod.with_box)
    if "run_count" in return_dict: run_count = return_dict["run_count"]
    if "idle_count" in return_dict: idle_count = return_dict["idle_count"]
    if "crouch_count" in return_dict: crouch_count = return_dict["crouch_count"]
    if "number_for_choose_sprite" in return_dict: number_for_choose_sprite = return_dict["number_for_choose_sprite"]
    #--------------------------------------------

    #MODAL_INFO--------------------------------------------
    if modal_window_info:
        mod.modal_w.print_text_on_screen(mod.WIDTH, mod.HEIGHT, mod.screen, claim)
        pygame.time.delay(120)
    #--------------------------------------------

    #Pause--------------------------------------------
    if keys[pygame.K_ESCAPE]:
        pause = True
    if pause:
        pygame.time.delay(120)
        continue_b = mod.Button(525, 250, 190, 100, "images/resources/continue.png")
        exit_b = mod.Button(525, 450, 190, 100, "images/resources/exit.png")
        continue_b.screen_darkness(mod.screen)
        continue_b.show_image(mod.screen)
        exit_b.show_image(mod.screen)
    #--------------------------------------------
    
    pygame.display.flip()