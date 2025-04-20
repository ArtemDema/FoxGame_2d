from ..main_classes import Block

class Water(Block):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)
    
    def check_death_of_player(self, player):
        answer = self.check_collision_top_wall(player.x + 20, player.y, player.x + player.width - 20, player.y + player.height - 10)
        if answer:
            return True
        else:
            return False