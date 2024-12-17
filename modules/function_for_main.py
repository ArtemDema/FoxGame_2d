from .screen.map import blocks
from .resourses import droped_resources
from .chest import chests
from .enemy import list_enemy

def check_push_chest(player, last_side):
    if last_side == 1:
        for chest in chests:
            answer = chest.check_collision_left_wall(player.x, player.y, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                return True
    else:
        for chest in chests:
            answer = chest.check_collision_right_wall(player.x, player.y, 
                                                    player.x + player.width, player.y + player.height)
            if answer:
                return True
    return False

def check_jump(player_x, player_y, player_width, player_height, player_strength_jump, blocks, player_speed):
    return_dict = {}
    if player_strength_jump != 0:
            for block in blocks:
                answer = block.check_collision_bottom_wall(player_x, player_y, 
                                                    player_x + player_width, player_y + player_height)
                if answer:
                    return_dict["move_jump"] = False
                    return_dict["player_strength_jump"] = 17
                    return return_dict
            for chest in chests:
                answer = chest.check_collision_bottom_wall(player_x, player_y, 
                                                    player_x + player_width, player_y + player_height)
                if answer:
                    return_dict["move_jump"] = False
                    return_dict["player_strength_jump"] = 17
                    return return_dict
            
            for block in blocks:
                block.y += player_speed * 3
            for resource in droped_resources:
                resource.y += player_speed * 3
            for chest in chests:
                chest.y += player_speed * 3
            for enemy in list_enemy:
                enemy.y += player_speed * 3

            return_dict["player_strength_jump"] = player_strength_jump - 1
            return return_dict
    else:
        return_dict["move_jump"] = False
        return_dict["player_strength_jump"] = 17
        return return_dict
    
def gravity(player, move_jump):
    list_return = {}
    for block in blocks:
        answer_fall = block.check_collision_top_wall(player.x, player.y, #checking whether the player is standing on some block
                                                     player.x + player.width, player.y + player.height)
        if answer_fall: #if the player is standing on some block
            list_return["move_bottom"] = False
            return list_return
    for chest in chests:
        answer_fall = chest.check_collision_top_wall(player.x, player.y,
                                                     player.x + player.width, player.y + player.height)
        if answer_fall:
            list_return["move_bottom"] = False
            return list_return

    if answer_fall != True: #if he does not
        if move_jump == False:
            list_return["move_bottom"] = True
            for block in blocks:
                block.y -= player.speed
            for recource in droped_resources:
                recource.y -= player.speed
            for chest in chests:
                chest.y -= player.speed
            for enemy in list_enemy:
                enemy.y -= player.speed

    return list_return

def gravity_resources(player):
    for recource in droped_resources:
        recource.gravity(player)

def gravity_chests(player):
    for chest in chests:
        chest.gravity(player)

def gravity_enemy(player):
    for enemy in list_enemy:
        enemy.gravity(player, blocks)