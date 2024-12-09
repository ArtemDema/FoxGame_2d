from .screen.map import blocks
<<<<<<< HEAD
from .resourses import droped_resources
=======
>>>>>>> e7e5459d04f7b2c44e4a912a28f6c35d42377547

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
<<<<<<< HEAD
            for resource in droped_resources:
                resource.x -= player_speed
=======
>>>>>>> e7e5459d04f7b2c44e4a912a28f6c35d42377547

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
<<<<<<< HEAD
            for resource in droped_resources:
                resource.x += player_speed
=======
>>>>>>> e7e5459d04f7b2c44e4a912a28f6c35d42377547
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
<<<<<<< HEAD
            for resource in droped_resources:
                resource.y += player_speed * 3
=======
>>>>>>> e7e5459d04f7b2c44e4a912a28f6c35d42377547
            return_dict["player_strength_jump"] = player_strength_jump - 1
            return return_dict
    else:
        return_dict["move_jump"] = False
        return_dict["player_strength_jump"] = 17
        return return_dict