import random
from ..screen import sound_damage, sound_death_enemy

def cloud_check(list_of_clouds, Cloud, frequency):
    if frequency <= 0:
        if len(list_of_clouds) < 5:
            cloud = Cloud(x = 1430, 
                                y = 25, 
                                width = random.randint(140, 200),
                                height = random.randint(100, 160), 
                                image = f"images/cloud/cloud_{random.randint(0, 4)}.png")
            list_of_clouds.append(cloud)

    for cloud in list_of_clouds:
        answer = cloud.move()
        if answer:
            list_of_clouds.remove(cloud)
    return list_of_clouds

def tree_check(list_trees,list_bubble_tree,player, Discarded_Item, droped_resources):
    for tree in list_trees:
        tree.idle(list_bubble_tree)
        answer = tree.drop_egg(player)
        if answer:
            egg1 = Discarded_Item(x = tree.x + 70, y = tree.y - 30, width = 20, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
            droped_resources.append(egg1)
            tree.ramdom_egg = 0
    return droped_resources

def add_hp(egg, player, meat, add_hp_egg, add_hp_meat):
    return_dict = {}
    return_dict["add_hp_egg"] = add_hp_egg
    return_dict["add_hp_meat"] = add_hp_meat
    if egg.count == 20:
        if player.hp <= 4:
            if add_hp_egg == 0:
                player.hp += 1
                return_dict["add_hp_egg"] = add_hp_egg + 1
                return_dict["add_hp_sound"] = True

    elif egg.count == 40:
        if player.hp <= 4:
            if add_hp_egg == 1:
                player.hp += 1
                return_dict["add_hp_egg"] = add_hp_egg + 1
                return_dict["add_hp_sound"] = True

    elif egg.count == 50:
        if player.hp <= 4:
            if add_hp_egg == 2:
                player.hp += 1
                return_dict["add_hp_egg"] = add_hp_egg + 1
                return_dict["add_hp_sound"] = True
    #--------------------------------------------
    elif meat.count == 10:
        if player.hp <= 4:
            if add_hp_meat == 0:
                player.hp += 1
                return_dict["add_hp_meat"] = add_hp_meat + 1
                return_dict["add_hp_sound"] = True

    elif meat.count == 20:
        if player.hp <= 4:
            if add_hp_meat == 1:
                player.hp += 1
                return_dict["add_hp_meat"] = add_hp_meat + 1
                return_dict["add_hp_sound"] = True

    elif meat.count == 30:
        if player.hp <= 4:
            if add_hp_meat == 2:
                player.hp += 1
                return_dict["add_hp_meat"] = add_hp_meat + 1
                return_dict["add_hp_sound"] = True
    return return_dict

def enemy(list_enemy, player, boxes, move_bottom, blocks, chests, list_feather, WIDTH, HEIGHT, task_enemy):
    for enemy in list_enemy:
        task_enemy = enemy.check_death(player, boxes, move_bottom, task_enemy, sound_death_enemy) #CHECKING IF THE PLAYER IS TRYING TO KILL THE ENEMY
        if enemy.is_dead == False:
            enemy.player_visibility = enemy.player_visibility_zone(player)
            enemy.move(player, blocks, chests, boxes, sound_damage) #ENEMY MOVE

    if len(list_feather) != 0:
        for feather in list_feather:
            feather.move(WIDTH, HEIGHT, player, blocks, chests, boxes, sound_damage)
    return task_enemy