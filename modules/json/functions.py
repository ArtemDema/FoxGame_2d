import os
import json


def get_info(path): #
    """
    ### Give information from last session
    """
    with open(file = path, mode = "r", encoding = "utf-8") as file:
        info = json.load(file)
        return info

def save_info(WIDTH, HEIGHT, player_hp, path): #
    """
    ### Save information from session
    """
    with open(file = path, mode = "w", encoding = "utf-8") as file:
        last_info_game = {
            "width":WIDTH,
            "height":HEIGHT,
            "hp":player_hp
        }
        json.dump(obj = last_info_game,fp = file,ensure_ascii = False, indent = 4)