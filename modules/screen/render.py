import pygame

from .map import blocks, background, list_trees, list_of_clouds, chests, boxes, list_bush, list_big_boss_tree, droped_resources
from ..interface import interface, hearts, Column_Meat_Egg_Hp_Key
from .render_enemy import render_enemy
from ..enemy import list_feather
from .load_all_images import list_idle_with_chest, list_idle, list_jump, list_jump_with_chest, list_crouch, list_run_with_chest, list_run

pygame.init()

def render(move_left, move_right, move_jump, move_crouch, move_bottom, screen, #DRAWING ALL
           player, last_side, number_for_choose_sprite, idle_count, crouch_count, run_count, hide, with_chest):
    """
    ### Render EVERYTHING what will be on the screen
    """
    
    return_dict = {}

    hearts = []

    for index in range(5):
        if index < player.hp:
            hp = Column_Meat_Egg_Hp_Key(10 + (index * 30), 19, 27, 27, "images/resources/heart.png", 0)
            hearts.append(hp)
        else:
            hp = Column_Meat_Egg_Hp_Key(10 + (index * 30), 19, 27, 27, "images/resources/hollow_heart.png", 0)
            hearts.append(hp)

    #background rendering
    background.draw_image(screen)

    for tree in list_big_boss_tree:
        tree.draw_image(screen)

    for cloud in list_of_clouds:
        cloud.draw_image(screen)

    #rendering all blocks
    for block in blocks: 
        block.draw_image(screen)

    for tree in list_trees:
        tree.draw_image(screen)

    for chest in chests:
        if chest.open_chest == True:
            if chest.hide_in_him:
                chest.image = "images/chest/chest_player_in.png"
            else:
                chest.image = "images/chest/chest_open.png"
        else:
            chest.image = "images/chest/chest_lock.png"
        chest.load_image()
        chest.draw_image(screen)
    
    for box in boxes:
        if box.open_box == True:
            if box.hide_in_him:
                box.image = "images/box/box_player_in.png"
            else:
                box.image = "images/box/box_open.png"
        else:
            box.image = "images/box/box_lock.png"
        box.load_image()
        box.draw_image(screen)

    for recource in droped_resources: 
        recource.draw_image(screen)

    for hp in hearts:
        hp.draw_image(screen)

    for item in interface:
        item.draw_image(screen)
        item.print_text(screen)

    render_enemy() #RENDER ALL ENEMY

    if len(list_feather) != 0:
        for feather in list_feather:
            feather.draw_image(screen)

    # pygame.draw.rect(screen, (255, 255, 255),player.rect)
    #check for drawing in a idle
    if move_left == False and move_right == False and move_bottom == False and move_jump == False and move_crouch == False and hide == False:
        player.idle(idle_count, screen, last_side, with_chest, list_idle_with_chest, list_idle)
        if number_for_choose_sprite == 10:
            if idle_count != 3:
                return_dict["idle_count"] = idle_count + 1
            else:
                return_dict["idle_count"] = 0
            return_dict["number_for_choose_sprite"] = 0
        else:
            return_dict["number_for_choose_sprite"] = number_for_choose_sprite + 1

    #Jump drawing check
    elif move_jump: 
        player.jump(screen, last_side, list_jump)
    
    #check falling rendering
    elif move_bottom:
        player.fall(screen, last_side, with_chest, list_jump_with_chest, list_jump)

    #check for squat rendering
    elif move_crouch:
        player.crouch(crouch_count, screen, last_side, list_crouch)
        if number_for_choose_sprite == 10:
            if crouch_count == 0:
                return_dict["crouch_count"] = crouch_count + 1
                crouch_count += 1
            else:
                return_dict["crouch_count"] = 0
                crouch_count = 0
            return_dict["number_for_choose_sprite"] = 0
        else:
            return_dict["number_for_choose_sprite"] = number_for_choose_sprite + 1

    #check for moving rendering
    elif move_left or move_right:
        player.run(run_count, screen, last_side, with_chest, list_run_with_chest, list_run)
        if number_for_choose_sprite == 10:
            if run_count != 5:
                return_dict["run_count"] = run_count + 1
            else:
                return_dict["run_count"] = 0
            return_dict["number_for_choose_sprite"] = 0
        else:
            return_dict["number_for_choose_sprite"] = number_for_choose_sprite + 1

    for bush in list_bush:
        bush.draw_image(screen)
    
    #check for climbing rendering
    else:
        pass #climb 

    # for block in blocks:
    #     pygame.draw.rect(screen, (255, 0, 255), block.rect)
    
    return return_dict