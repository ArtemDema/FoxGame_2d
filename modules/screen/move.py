from .map import blocks, list_trees, list_of_clouds,chests, boxes, list_enemy, list_bush, list_big_boss_tree, list_water, end_of_level
from ..enemy import list_feather

def move_left_player(player, move_jump, push_box, with_box, chest_player): #CHECK MOVE LEFT
    """
    ### Checking blocks for moving player to the left side
    """
    dict_return = {}
    if with_box:
        for block in blocks:
            answer = block.check_collision_right_wall(player.x, chest_player.y + 5, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                dict_return["last_side"] = 0
                return dict_return
            
        for chest in chests:
            answer = chest.check_collision_right_wall(player.x, chest_player.y + 5, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                dict_return["last_side"] = 0
                return dict_return
            
        for box in boxes:
            answer = box.check_collision_right_wall(player.x, player.y + 5, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                if push_box:
                    for block in blocks:
                        answer = block.check_collision_right_wall(box.x + 17, box.y, 
                                                    box.x + box.width + 17, box.y + box.height)
                        if answer:
                            dict_return["last_side"] = 0
                            return dict_return
                    box.x -= player.speed
                else:
                    dict_return["last_side"] = 0
                    return dict_return
            
        if answer != True:
            if move_jump == False:
                dict_return["move_left"] = True
            if push_box: dict_return["push_box"] = False
            dict_return["last_side"] = 0
            player.x -= player.speed
            player.rect.x -= player.speed
    else:
        for block in blocks:
            answer = block.check_collision_right_wall_p(player)
            if answer:
                dict_return["last_side"] = 0
                return dict_return
            
        for chest in chests:
            answer = chest.check_collision_right_wall(player.x, player.y + 5, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                dict_return["last_side"] = 0
                return dict_return

        for box in boxes:
            answer = box.check_collision_right_wall(player.x, player.y + 5, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                if push_box:
                    for block in blocks:
                        answer = block.check_collision_right_wall(box.x - 15, box.y, 
                                                    box.x + box.width, box.y + box.height)
                        if answer:
                            dict_return["last_side"] = 0
                            return dict_return
                    
                    for chest in chests:
                        answer = chest.check_collision_right_wall(box.x - 15, box.y, 
                                                    box.x + box.width, box.y + box.height)
                        if answer:
                            dict_return["last_side"] = 0
                            return dict_return

                    box.x -= player.speed
                else:
                    dict_return["last_side"] = 0
                    return dict_return
            
        if answer != True:
            if move_jump == False:
                dict_return["move_left"] = True
            if push_box: dict_return["push_box"] = False
            dict_return["last_side"] = 0
            player.x -= player.speed
            player.rect.x -= player.speed

    return dict_return

def move_right_player(player, move_jump, push_box, with_box, chest_player, WIDTH, droped_resources): #CHECK MOVE RIGHT
    """
    ### Checking blocks for moving player to the right side
    """
    dict_return = {}
    if with_box:
        for block in blocks:
            answer = block.check_collision_left_wall(player.x, chest_player.y + 5, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                dict_return["last_side"] = 1
                return dict_return
            
        for chest in chests:
            answer = chest.check_collision_left_wall(player.x, chest_player.y + 5, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                dict_return["last_side"] = 1
                return dict_return
            
        for box in boxes:
            answer = box.check_collision_left_wall(player.x, player.y + 5, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                if push_box:
                    for block in blocks:
                        answer = block.check_collision_left_wall(box.x + 17, box.y, 
                                                    box.x + box.width + 17, box.y + box.height)
                        if answer:
                            dict_return["last_side"] = 1
                            return dict_return
                    box.x += player.speed
                else:
                    dict_return["last_side"] = 1
                    return dict_return
            
        if answer != True:
            if move_jump == False:
                dict_return["move_right"] = True
            if push_box: dict_return["push_box"] = False
            dict_return["last_side"] = 1
            
            for chest in chests:
                chest.hide_in_him = False

            if player.x == WIDTH // 2:
                if player.x + WIDTH // 2 >= end_of_level.x + end_of_level.width:
                    player.x += player.speed
                    player.rect.x += player.speed
                else:
                    for block in blocks:
                        block.x -= player.speed
                        block.rect.x -= player.speed
                        block.top_rect.x -= player.speed
                        block.bottom_rect.x -= player.speed
                    for resource in droped_resources:
                        resource.x -= player.speed
                    for chest in chests:
                        chest.x -= player.speed
                    for box in boxes:
                        box.x -= player.speed
                    for enemy in list_enemy:
                        enemy.x -= player.speed
                    for tree in list_trees:
                        tree.x -= player.speed
                    for cloud in list_of_clouds:
                        cloud.x -= player.speed
                    for feather in list_feather:
                        feather.x -= player.speed
                    for bush in list_bush:
                        bush.x -= player.speed
                    for tree in list_big_boss_tree:
                        tree.x -= player.speed
                    for water in list_water:
                        water.x -= player.speed
                    end_of_level.x -= player.speed
            else:
                player.x += player.speed
                player.rect.x += player.speed
    else:
        for block in blocks:
            answer = block.check_collision_left_wall_p(player)
            if answer:
                dict_return["last_side"] = 1
                return dict_return
        
        for chest in chests:
            answer = chest.check_collision_left_wall(player.x, player.y + 5, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                dict_return["last_side"] = 1
                return dict_return
            
        for box in boxes:
            answer = box.check_collision_left_wall(player.x, player.y + 5, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                if push_box:
                    for block in blocks:
                        answer = block.check_collision_left_wall(box.x + 17, box.y, 
                                                    box.x + box.width + 17, box.y + box.height)
                        if answer:
                            dict_return["last_side"] = 1
                            return dict_return
                    
                    for chest in chests:
                        answer = chest.check_collision_left_wall(box.x + 17, box.y, 
                                                    box.x + box.width + 17, box.y + box.height)
                        if answer:
                            dict_return["last_side"] = 1
                            return dict_return

                    box.x += player.speed
                else:
                    dict_return["last_side"] = 1
                    return dict_return
            
        if answer != True:
            if move_jump == False:
                dict_return["move_right"] = True
            if push_box: dict_return["push_box"] = False
            dict_return["last_side"] = 1
            if player.x == WIDTH // 2:
                if player.x + WIDTH // 2 >= end_of_level.x + end_of_level.width:
                    player.x += player.speed
                    player.rect.x += player.speed
                else:
                    for block in blocks:
                        block.x -= player.speed
                        block.rect.x -= player.speed
                        block.top_rect.x -= player.speed
                        block.bottom_rect.x -= player.speed
                    for resource in droped_resources:
                        resource.x -= player.speed
                    for chest in chests:
                        chest.x -= player.speed
                    for box in boxes:
                        box.x -= player.speed
                    for enemy in list_enemy:
                        enemy.x -= player.speed
                    for tree in list_trees:
                        tree.x -= player.speed
                    for cloud in list_of_clouds:
                        cloud.x -= player.speed
                    for feather in list_feather:
                        feather.x -= player.speed
                    for bush in list_bush:
                        bush.x -= player.speed
                    for tree in list_big_boss_tree:
                        tree.x -= player.speed
                    for water in list_water:
                        water.x -= player.speed
                    end_of_level.x -= player.speed
            else:
                player.x += player.speed
                player.rect.x += player.speed

    return dict_return