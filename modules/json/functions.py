import os
import json

path = os.path.abspath(__file__ + "/../../../json/main_info.json")

def get_info(): #
    """
    ### Give information from last session
    """
    with open(file = path, mode = "r", encoding = "utf-8") as file:
        info = json.load(file)
        return info

def save_info(WIDTH, HEIGHT, player_hp): #
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