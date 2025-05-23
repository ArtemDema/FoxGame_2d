from .screen import blocks, chests, boxes, list_enemy, droped_resources

def check_push_box(player, last_side): #CHECK PUSH BOX
    """
    ### The name speaks for itself
    """
    if last_side == 1:
        for box in boxes:
            answer = box.check_collision_left_wall(player.x, player.y, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                return True
    else:
        for box in boxes:
            answer = box.check_collision_right_wall(player.x, player.y, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                return True
    return False

def check_jump(player, blocks): #CHECK JUMP
    """
    ### Checking blocks for moving player to the up(jump) side
    """
    return_dict = {}
    if player.strength_jump != 0:
        for block in blocks:
            answer = block.check_collision_bottom_wall_p(player)
            if answer:
                return_dict["move_jump"] = False
                return_dict["player_strength_jump"] = 20
                return return_dict
            
        for box in boxes:
            answer = box.check_collision_bottom_wall(player.x, player.y, 
                                                player.x + player.width, player.y + player.height)
            if answer:
                return_dict["move_jump"] = False
                return_dict["player_strength_jump"] = 20
                return return_dict
            
            player.y -= player.speed * 1.5
            player.rect.y -= player.speed * 1.5
            # for block in blocks:
            #     block.y += player_speed * 3
            # for resource in droped_resources:
            #     resource.y += player_speed * 3
            # for box in boxes:
            #     box.y += player_speed * 3
            # for chest in chests:
            #     chest.y += player_speed * 3
            # for enemy in list_enemy:
            #     enemy.y += player_speed * 3
            # for tree in list_trees:
            #     tree.y += player_speed * 3
            # for cloud in list_of_clouds:
            #     cloud.y += player_speed * 3
            # for feather in list_feather:
            #     feather.y += player_speed * 3
            # for bush in list_bush:
            #     bush.y += player_speed * 3
            # for tree in list_big_boss_tree:
            #     tree.y += player_speed * 3
            # for text in list_of_text:
            #     text.y += player_speed * 3

            return_dict["player_strength_jump"] = player.strength_jump - 1
            return return_dict
    else:
        return_dict["move_jump"] = False
        return_dict["player_strength_jump"] = 20
        return return_dict
    
def gravity(player, move_jump): #GRAVITY PLAYER
    """
    ### Player gravity
    """
    list_return = {}
    list_of_all_blocks = []
    list_of_all_blocks += chests
    list_of_all_blocks += boxes

    answer_fall = True

    for block in list_of_all_blocks:
        answer_fall = block.check_collision_top_wall(player.x, player.y,
                                                    player.x + player.width, player.y + player.height)
        if answer_fall: #if the player is standing on some block
            list_return["move_bottom"] = False
            return list_return

    for block in blocks:
        answer_fall = block.check_collision_top_wall_p(player)
        if answer_fall: #if the player is standing on some block
            list_return["move_bottom"] = False
            list_return["last_block"] = block
            return list_return

    if answer_fall != True: #if he does not
        if move_jump == False:
            list_return["move_bottom"] = True
            player.y += player.speed_fall
            player.rect.y += player.speed_fall

    return list_return

def gravity_resources(player): #GRAVITY RESOURCES
    for recource in droped_resources:
        recource.gravity(player, blocks, chests, boxes)

def gravity_boxes(player): #GRAVITY BOXES
    for box in boxes: 
        box.gravity(player, blocks, chests, boxes)

def gravity_enemy(player): #GRAVITY ENEMY
    for enemy in list_enemy:
        enemy.gravity(player, blocks)