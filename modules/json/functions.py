import os
import json

<<<<<<< HEAD
path = os.path.abspath(__file__ + "/../../../json/main_info.json")
=======
path = os.path.abspath(__file__ + "/../../../instance/main_info.json")
>>>>>>> e7e5459d04f7b2c44e4a912a28f6c35d42377547

def get_info(WIDTH, HEIGHT, player_hp):
    with open(file = path, mode = "r", encoding = "utf-8") as file:
        info = json.load(file)
        WIDTH = info["width"]
        HEIGHT = info["height"]
        player_hp = info["hp"]

def save_info(WIDTH, HEIGHT, player_hp):
    with open(file = path, mode = "w", encoding = "utf-8") as file:
        last_info_game = {
            "width":WIDTH,
            "height":HEIGHT,
            "hp":player_hp
        }
        json.dump(obj = last_info_game,fp = file,ensure_ascii = False, indent = 4)