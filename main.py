import pygame
import modules as mod

pygame.init()

tick = pygame.time.Clock()

#
add_hp_egg = 0
add_hp_meat = 0

#task counters
task_egg  = 0
task_meat = 0
task_enemy = 0
task_chest = 0

#saves the last motion vector (0 - left, 1 - right)
last_side = 0

reload_chest = 0
box_player = 0
modal_window_info = False
pause = False
tasks = False
last_block = 0

#counters (elements for the array) for changing the sprite:
idle_count = 0
run_count = 0
crouch_count = 0

#sprite change frequency
number_for_choose_sprite = 10
frequency_cloud = 120

#getting information from the last session
info = mod.get_info(__file__ + "/../json/main_info.json")
WIDTH = info["width"]
HEIGHT = info["height"]
mod.player.hp = info["hp"]

#show menu
game_run = mod.main_menu.menu(screen = mod.screen)
player_level = 1
task = mod.get_info(__file__ + "/../level_task/tasks.json")
task_egg  = int(task[f'{player_level}']['1'])
task_meat = int(task[f'{player_level}']['3'])
task_enemy = int(task[f'{player_level}']['5'])
task_chest = int(task[f'{player_level}']['7'])
mod.music.set_volume(0.06)
mod.music.play(loops = -1)
while game_run:
    tick.tick(60) #set the number of fps

    if mod.player.hp <= 0:
        game_run = False

    # print(tick.get_fps())

    keys = pygame.key.get_pressed() #getting keys to process pressed keys

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #SAVES INFORMATION
            mod.save_info(WIDTH = mod.WIDTH, HEIGHT = mod.HEIGHT, player_hp = mod.player.hp, path = __file__ + "/../json/main_info.json")
            game_run = False
        
        if event.type == pygame.MOUSEMOTION:
                position_mouse = event.pos
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if modal_window_info:
                modal_window_info = mod.modal_w.check_click(position_mouse[0], position_mouse[1])
            elif pause:
                pause = continue_b.check_click(position_mouse_x = position_mouse[0], position_mouse_y = position_mouse[1])
                game_run = exit_b.check_click(position_mouse_x = position_mouse[0], position_mouse_y = position_mouse[1])
                if game_run ==False:
                    mod.save_info(WIDTH = mod.WIDTH, HEIGHT = mod.HEIGHT, player_hp = mod.player.hp, path = __file__ + "/../json/main_info.json")
            elif tasks:
                tasks = exit_b.check_click(position_mouse_x = position_mouse[0], position_mouse_y = position_mouse[1])
    #CLOUD--------------------------------------------
    mod.list_of_clouds = mod.cloud_check(mod.list_of_clouds, mod.Cloud, frequency_cloud)
    if frequency_cloud <= 0:
        frequency_cloud = 120
    else:
        frequency_cloud -= 1
    #--------------------------------------------

    #TREE--------------------------------------------
    mod.droped_resources = mod.tree_check(mod.list_trees, mod.list_bubble_tree, mod.player, mod.Discarded_Item, mod.droped_resources)
    #--------------------------------------------

    #ENEMY--------------------------------------------
    task_enemy = mod.enemy(mod.list_enemy, mod.player, mod.boxes, mod.move_bottom, mod.blocks, mod.chests, mod.list_feather, mod.WIDTH, mod.HEIGHT, task_enemy)
    #--------------------------------------------

    #CHEST AND BOX--------------------------------------------
      #OPEN AND HIDE IN CHEST
    if keys[pygame.K_e]:
        return_dict = mod.check_open(mod.with_box, mod.chests, mod.key, mod.player, mod.droped_resources, reload_chest)
        if "key.count" in return_dict: mod.key.count = return_dict["key.count"]
        if "modal_window_info" in return_dict: modal_window_info = return_dict["modal_window_info"]
        if "player.hide" in return_dict: mod.player.hide = return_dict["player.hide"]
        if "reload_chest" in return_dict: reload_chest = return_dict["reload_chest"]

      #UP THE BOX
    if keys[pygame.K_q]:
        return_dict = mod.up_a_box(mod.player, mod.boxes, mod.Discarded_Item, mod.droped_resources, mod.with_box)
        if "with_box" in return_dict: mod.with_box = return_dict["with_box"]
        if "box_player" in return_dict: box_player = return_dict["box_player"]

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
                mod.drop_box.set_volume(0.2)
                mod.drop_box.play(loops = 0)
            else:
                box_player.throw = True
                box_player.angle = -55
                mod.drop_box.set_volume(0.2)
                mod.drop_box.play(loops = 0)
    #--------------------------------------------

    #MOVE--------------------------------------------
      #LEFT
    if keys[pygame.K_a]:
        mod.move_crouch = False
        mod.player.hide = False

        for chest in mod.chests:
            chest.hide_in_him = False
        if mod.player.x >= 1:
            if mod.move_bottom == False:
                dict_left = mod.move_left_player(mod.player, mod.move_jump, mod.push_box, mod.with_box, 
                                                 box_player, mod.list_enemy) #FUNCTION FOR PLAYER WALKING TO THE LEFT
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

        if mod.move_bottom == False:
            dict_right = mod.move_right_player(mod.player, mod.move_jump, 
                                            mod.push_box, mod.with_box, box_player, mod.WIDTH, mod.droped_resources,
                                            mod.list_enemy) #FUNCTION FOR PLAYER WALKING TO THE RIGHT
            if "move_right" in dict_right: mod.move_right = dict_right["move_right"]
            if "last_side" in dict_right: last_side = dict_right["last_side"]
            if "push_box" in dict_right: mod.push_box = dict_right["push_box"]
    else:
        if mod.player.x >= mod.end_of_level.x - 250:
            if task_egg <= 0 and task_meat <= 0 and task_enemy <= 0 and task_chest <= 0:
                mod.player.x += mod.player.speed
                mod.move_right = True
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
    if "last_block" in list_return: last_block = list_return["last_block"]

      #GRAVITY OF RESOURCES AND CHESTS
    mod.gravity_resources(mod.player) #RESOURCE GRAVITY
    mod.gravity_boxes(mod.player) #GRAVITY OF BOX
    mod.gravity_enemy(mod.player) #ENEMIES GRAVITY
    #--------------------------------------------
    #COLLECT RECOURCES--------------------------------------------
    for recource in mod.droped_resources: 
        return_dict = recource.check_collect_recource(mod.player, mod.meat.count, mod.egg.count, mod.key.count, mod.player.hp,
                                                      task_egg, task_meat, mod.collect_item) #CHECKING FOR SELECTION OF RESOURCES
        if "egg_count" in return_dict: mod.egg.count = return_dict["egg_count"]
        if "key_count" in return_dict: mod.key.count = return_dict["key_count"]
        if "meat_count" in return_dict: mod.meat.count = return_dict["meat_count"]
        if "heart_count" in return_dict: mod.player.hp = return_dict["heart_count"]
        if "task_egg" in return_dict: task_egg = return_dict["task_egg"]
        if "task_meat" in return_dict: task_meat = return_dict["task_meat"]
    #--------------------------------------------

    #RENDER--------------------------------------------
    return_dict = mod.render(mod.move_left, mod.move_right, mod.move_jump, mod.move_crouch, mod.move_bottom, mod.screen, #DRAWING EVERYTHING
                             mod.player, last_side, number_for_choose_sprite, idle_count, crouch_count, run_count, mod.player.hide, mod.with_box)
    if "run_count" in return_dict: run_count = return_dict["run_count"]
    if "idle_count" in return_dict: idle_count = return_dict["idle_count"]
    if "crouch_count" in return_dict: crouch_count = return_dict["crouch_count"]
    if "number_for_choose_sprite" in return_dict: number_for_choose_sprite = return_dict["number_for_choose_sprite"]
    #--------------------------------------------

    return_dict = mod.add_hp(mod.egg, mod.player, mod.meat, add_hp_egg, add_hp_meat)
    if "add_hp_egg" in return_dict: add_hp_egg = return_dict["add_hp_egg"]
    if "add_hp_meat" in return_dict: add_hp_meat = return_dict["add_hp_meat"]
    if "add_hp_sound" in return_dict: 
       mod.sound_add_hp.set_volume(0.3)
       mod.sound_add_hp.play(loops = 0)

    #MODAL_INFO--------------------------------------------
    if modal_window_info:
        mod.modal_w.print_text_on_screen(mod.WIDTH, mod.HEIGHT, mod.screen, mod.claim)
        pygame.time.delay(120)
    #--------------------------------------------

    #TASK MENU--------------------------------------------
    list_task = [task_egg, task_meat, task_enemy, task_chest]
    if keys[pygame.K_t]:
        tasks = True
    if tasks:
        #--------------------------------------------!!!!!!!!!!!!!!!
        task_photo = mod.Button(325, 75, 600, 700, "images/screen/task.png")
        exit_b = mod.Button(900, 600, 150, 70, "images/resources/exit.png")
        task_photo.show_image(mod.screen)
        number = 0
        for index in range(len(task["1"])):
            if index % 2 == 0:
                text_task = mod.Button(535, 200 + index * 50, 0, 0, "images/resources/exit.png")
                text_task.text(mod.screen, f"{task['1'][f'{index}']}", 48, 0, 0, 0)
            else:
                text_task = mod.Button(610, 200 + index * 50, 0, 0, "images/resources/exit.png")
                if list_task[number] >= 0:
                    text_task.text(mod.screen, f"{list_task[number]}", 48, 0, 0, 0)
                else:
                    text_task.text(mod.screen, "0", 48, 0, 0, 0)
                number += 1
        exit_b.show_image(mod.screen)
        #--------------------------------------------!!!!!!!!!!!!!!!
    #--------------------------------------------

    #PAUSE--------------------------------------------
    if keys[pygame.K_ESCAPE]:
        pause = True
    if pause:
        pygame.time.delay(120)
        continue_b = mod.Button(525, 250, 190, 100, "images/resources/continue.png")
        exit_b = mod.Button(525, 450, 190, 100, "images/resources/exit.png")
        continue_b.screen_darkness(mod.screen)
        continue_b.show_image(mod.screen)
        exit_b.show_image(mod.screen)
    #--------------------------------------------!!!!!!!!!!!!!!!
    if mod.player.player_in_the_water:
        if mod.player.y <= mod.HEIGHT + 50:
            mod.player.y += 1
        else:
            mod.player.x = last_block.x - 20
            mod.player.y = last_block.y - 90
            mod.player.rect.x = mod.player.x + 30
            mod.player.rect.y = mod.player.y + 30
            mod.player.player_in_the_water = False
    else:
        for water in mod.list_water:
            answer = water.check_death_of_player(mod.player)
            if answer:
                mod.player.damage_player(mod.sound_damage)
                mod.player.player_in_the_water = True
                break
    #--------------------------------------------!!!!!!!!!!!!!!!

    pygame.display.flip()