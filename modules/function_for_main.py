from .screen.map import blocks
from .resourses import droped_resources

def check_run(player_x, player_y, player_width, player_height, move_jump, player_speed, side):
    dict_return = {}
    if side == "right":
        for block in blocks:
            answer = block.check_collision_left_wall(player_x, player_y, 
                                                    player_x + player_width, player_y + player_height)
            if answer:
                dict_return["last_side"] = 1
                break
        if answer != True:
            if move_jump == False:
                dict_return["move_right"] = True
            dict_return["last_side"] = 1
            for block in blocks:
                block.x -= player_speed
            for resource in droped_resources:
                resource.x -= player_speed

    else:
        for block in blocks:
            answer = block.check_collision_right_wall(player_x, player_y, 
                                                    player_x + player_width, player_y + player_height)
            if answer:
                dict_return["last_side"] = 0
                break
        if answer != True:
            if move_jump == False:
                dict_return["move_left"] = True
            dict_return["last_side"] = 0
            for block in blocks:
                block.x += player_speed
            for resource in droped_resources:
                resource.x += player_speed
    return dict_return

def check_jump(player_x, player_y, player_width, player_height, player_strength_jump, blocks, player_speed, move_jump):
    return_dict = {}
    if player_strength_jump != 0:
            for block in blocks:
                answer = block.check_collision_bottom_wall(player_x, player_y, 
                                                    player_x + player_width, player_y + player_height)
                if answer:
                    return_dict["move_jump"] = False
                    return_dict["player_strength_jump"] = 17
                    return return_dict
            
            for block in blocks:
                block.y += player_speed * 3
            for resource in droped_resources:
                resource.y += player_speed * 3
            return_dict["player_strength_jump"] = player_strength_jump - 1
            return return_dict
    else:
        return_dict["move_jump"] = False
        return_dict["player_strength_jump"] = 17
        return return_dict