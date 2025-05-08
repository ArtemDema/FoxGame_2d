def check_open(with_box,chests, key, player, droped_resources, reload_chest):
    return_list = {}
    if with_box == False:
        for chest in chests: #CHECKING AN ATTEMPT TO OPEN A CHEST
            answer = chest.check_open(key.count, player, droped_resources) #
            if answer[0]: 
                return_list["key.count"] = key.count - 1
                return_list["modal_window_info"] = True
                return_list["claim"] = answer[1]
            elif answer[0] == False: 
                return_list["player.hide"] = True
                chest.hide_in_him = True
    else:
        return_list["reload_chest"] = 1
    return return_list

def up_a_box(player, boxes, Discarded_Item, droped_resources, with_box):
    return_list = {}
    if player.hide == False and with_box == False:
        for box in boxes: #CHECKING AN ATTEMPT TO UP A BOX 
            answer = box.check_up_the_box(player)
            if answer:
                return_list["with_box"] = True
                return_list["box_player"] = box
                if box.random_item == "key":
                    key1 = Discarded_Item(x = box.x, y = box.y, width = 35, height = 25, image = "images/resources/key.png", whatIsThis= "key")
                    droped_resources.append(key1)
                    box.random_item = " "
                elif box.random_item == "egg":
                        egg1 = Discarded_Item(x = box.x, y = box.y, width = 25, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
                        droped_resources.append(egg1)
                        box.random_item = " "
                elif box.random_item == "meat":
                        meat1 = Discarded_Item(x = box.x, y = box.y, width = 40, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
                        droped_resources.append(meat1)
                        box.random_item = " "
    return return_list