from ..main_classes import Settings

list_sprite_bush = ["images/bush/0.png","images/bush/1.png","images/bush/2.png",
             "images/bush/3.png","images/bush/4.png","images/bush/5.png",
             "images/bush/6.png"]

class Bush(Settings):
    """
    ### Bush class
    """
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)