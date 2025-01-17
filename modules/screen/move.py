from .map import blocks, list_trees, list_of_clouds,chests, boxes
from ..resourses import droped_resources
from ..enemy import list_enemy, list_feather

def move_left_player(player, move_jump, push_box, with_box, chest_player): #CHECK MOVE LEFT
    dict_return = {}
    if with_box:
        for block in blocks:
            answer = block.check_collision_right_wall(player.x, chest_player.y, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                dict_return["last_side"] = 0
                return dict_return
            
        for chest in chests:
            answer = chest.check_collision_right_wall(player.x, chest_player.y, 
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
    else:
        for block in blocks:
            answer = block.check_collision_right_wall(player.x, player.y, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                dict_return["last_side"] = 0
                return dict_return
            
        for chest in chests:
            answer = chest.check_collision_right_wall(player.x, player.y, 
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

    return dict_return

def move_right_player(player, move_jump, push_box, with_box, chest_player, WIDTH): #CHECK MOVE RIGHT
    dict_return = {}
    if with_box:
        for block in blocks:
            answer = block.check_collision_left_wall(player.x, chest_player.y, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                dict_return["last_side"] = 1
                return dict_return
            
        for chest in chests:
            answer = chest.check_collision_left_wall(player.x, chest_player.y, 
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

            for box in boxes:
                box.hide_in_him = False
            for chest in chests:
                chest.hide_in_him = False

            if player.x == WIDTH // 2:
                for block in blocks:
                    block.x -= player.speed
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
            else:
                player.x += player.speed
    else:
        for block in blocks:
            answer = block.check_collision_left_wall(player.x, player.y, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                dict_return["last_side"] = 1
                return dict_return
        
        for chest in chests:
            answer = chest.check_collision_left_wall(player.x, player.y, 
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
                for block in blocks:
                    block.x -= player.speed
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
            else:
                player.x += player.speed

    return dict_return