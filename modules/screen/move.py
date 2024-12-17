from .map import blocks
from ..chest import chests
from ..resourses import droped_resources
from ..enemy import list_enemy

def move_left_player(player, move_jump, push_chest, with_chest, chest_player):
    dict_return = {}
    if with_chest:
        for block in blocks:
            answer = block.check_collision_right_wall(player.x, chest_player.y, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                dict_return["last_side"] = 0
                return dict_return
            
        for chest in chests:
            answer = chest.check_collision_right_wall(player.x, player.y + 5, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                if push_chest:
                    for block in blocks:
                        answer = block.check_collision_right_wall(chest.x + 17, chest.y, 
                                                    chest.x + chest.width + 17, chest.y + chest.height)
                        if answer:
                            dict_return["last_side"] = 0
                            return dict_return
                    chest.x -= player.speed
                else:
                    dict_return["last_side"] = 0
                    return dict_return
            
        if answer != True:
            if move_jump == False:
                dict_return["move_left"] = True
            if push_chest: dict_return["push_chest"] = False
            dict_return["last_side"] = 0
            for block in blocks:
                block.x += player.speed
            for resource in droped_resources:
                resource.x += player.speed
            for chest in chests:
                chest.x += player.speed
            for enemy in list_enemy:
                enemy.x += player.speed
    else:
        for block in blocks:
            answer = block.check_collision_right_wall(player.x, player.y, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                dict_return["last_side"] = 0
                return dict_return
            
        for chest in chests:
            answer = chest.check_collision_right_wall(player.x, player.y + 5, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                if push_chest:
                    for block in blocks:
                        answer = block.check_collision_right_wall(chest.x - 10, chest.y, 
                                                    chest.x + chest.width - 7, chest.y + chest.height)
                        if answer:
                            dict_return["last_side"] = 0
                            return dict_return
                    chest.x -= player.speed
                else:
                    dict_return["last_side"] = 0
                    return dict_return
            
        if answer != True:
            if move_jump == False:
                dict_return["move_left"] = True
            if push_chest: dict_return["push_chest"] = False
            dict_return["last_side"] = 0
            for block in blocks:
                block.x += player.speed
            for resource in droped_resources:
                resource.x += player.speed
            for chest in chests:
                chest.x += player.speed
            for enemy in list_enemy:
                enemy.x += player.speed

    return dict_return

def move_right_player(player, move_jump, push_chest, with_chest, chest_player):
    dict_return = {}
    if with_chest:
        for block in blocks:
            answer = block.check_collision_left_wall(player.x, chest_player.y, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                dict_return["last_side"] = 1
                return dict_return
            
        for chest in chests:
            answer = chest.check_collision_left_wall(player.x, player.y + 5, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                if push_chest:
                    for block in blocks:
                        answer = block.check_collision_left_wall(chest.x + 17, chest.y, 
                                                    chest.x + chest.width + 17, chest.y + chest.height)
                        if answer:
                            dict_return["last_side"] = 1
                            return dict_return
                    chest.x += player.speed
                else:
                    dict_return["last_side"] = 1
                    return dict_return
            
        if answer != True:
            if move_jump == False:
                dict_return["move_right"] = True
            if push_chest: dict_return["push_chest"] = False
            dict_return["last_side"] = 1
            for block in blocks:
                block.x -= player.speed
            for resource in droped_resources:
                resource.x -= player.speed
            for chest in chests:
                chest.x -= player.speed
            for enemy in list_enemy:
                enemy.x -= player.speed
    else:
        for block in blocks:
            answer = block.check_collision_left_wall(player.x, player.y, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                dict_return["last_side"] = 1
                return dict_return
            
        for chest in chests:
            answer = chest.check_collision_left_wall(player.x, player.y + 5, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                if push_chest:
                    for block in blocks:
                        answer = block.check_collision_left_wall(chest.x + 17, chest.y, 
                                                    chest.x + chest.width + 17, chest.y + chest.height)
                        if answer:
                            dict_return["last_side"] = 1
                            return dict_return
                    chest.x += player.speed
                else:
                    dict_return["last_side"] = 1
                    return dict_return
            
        if answer != True:
            if move_jump == False:
                dict_return["move_right"] = True
            if push_chest: dict_return["push_chest"] = False
            dict_return["last_side"] = 1
            for block in blocks:
                block.x -= player.speed
            for resource in droped_resources:
                resource.x -= player.speed
            for chest in chests:
                chest.x -= player.speed
            for enemy in list_enemy:
                enemy.x -= player.speed

    return dict_return