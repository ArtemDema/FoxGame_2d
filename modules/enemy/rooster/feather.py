from ...main_classes import Enemy
import math

class Feather(Enemy):
    def __init__(self, x, y, width, height, image, angle):
        self.angle = angle
        self.is_dead = False
        self.death_animation = False
        self.death_count = 0
        self.death_sprite_frequency = 0
        super().__init__(x, y, width, height, image, 0, 0)

    def move(self, WIDTH, HEIGHT, player, blocks, chests, boxes):
        if self.is_dead == False:
            self.x = self.x + 4 * math.cos(self.angle * math.pi / 180)
            self.y = self.y + 4 * math.sin(self.angle * math.pi / 180)

            #DAMAGE PLAYER
            if player.hide == False:
                answer = player.check_collision_left(self.x, self.y, self.x + self.width, self.y + self.height)
                if answer:
                    player.damage_player()
                    list_feather.remove(self)
                    return

                answer = player.check_collision_right(self.x, self.y, self.x + self.width, self.y + self.height)
                if answer:
                    player.damage_player()
                    list_feather.remove(self)
                    return

                answer = player.check_collision_top(self.x, self.y, self.x + self.width, self.y + self.height)
                if answer:
                    player.damage_player()
                    list_feather.remove(self)
                    return

                answer = player.check_collision_bottom(self.x, self.y, self.x + self.width, self.y + self.height)
                if answer:
                    player.damage_player()
                    list_feather.remove(self)
                    return

            #DEATH
            for block in blocks:
                answer = block.check_collision_top_wall(self.x - 23, self.y - 20, self.x + self.width + 20, self.y + self.height)
                if answer:
                    self.is_dead = True
                    return

                answer = block.check_collision_bottom_wall(self.x - 20, self.y - 20, self.x + self.width + 20, self.y + self.height)
                if answer:
                    self.is_dead = True
                    return

                answer = block.check_collision_left_wall(self.x - 20, self.y - 30, self.x + self.width + 15, self.y + self.height + 5)
                if answer:
                    self.is_dead = True
                    return

                answer = block.check_collision_right_wall(self.x - 15, self.y - 30, self.x + self.width + 20, self.y + self.height + 5)
                if answer:
                    self.is_dead = True
                    return

            for chest in chests:
                answer = chest.check_collision_top_wall(self.x - 23, self.y - 20, self.x + self.width + 20, self.y + self.height)
                if answer:
                    self.is_dead = True
                    return

                answer = chest.check_collision_bottom_wall(self.x - 20, self.y - 20, self.x + self.width + 20, self.y + self.height)
                if answer:
                    self.is_dead = True
                    return

                answer = chest.check_collision_left_wall(self.x - 20, self.y - 30, self.x + self.width + 15, self.y + self.height + 5)
                if answer:
                    self.is_dead = True
                    return

                answer = chest.check_collision_right_wall(self.x - 15, self.y - 30, self.x + self.width + 20, self.y + self.height + 5)
                if answer:
                    self.is_dead = True
                    return

            for box in boxes:
                answer = box.check_collision_top_wall(self.x - 23, self.y - 20, self.x + self.width + 20, self.y + self.height)
                if answer:
                    self.is_dead = True
                    return

                answer = box.check_collision_bottom_wall(self.x - 20, self.y - 20, self.x + self.width + 20, self.y + self.height)
                if answer:
                    self.is_dead = True
                    return

                answer = box.check_collision_left_wall(self.x - 20, self.y - 30, self.x + self.width + 15, self.y + self.height + 5)
                if answer:
                    self.is_dead = True
                    return

                answer = box.check_collision_right_wall(self.x - 15, self.y - 30, self.x + self.width + 20, self.y + self.height + 5)
                if answer:
                    self.is_dead = True
                    return

            if self.x + self.width <= 0 and self.x >= WIDTH and self.y + self.height >= HEIGHT and self.y <= 0:
                self.is_dead = True
                return
        else:
            self.death_timer()
        
    def death_timer(self):
        if self.death_count == 6:
            self.death_animation = True
            self.death_count = 0
        else:
            if self.death_sprite_frequency >= 10: 
                self.death_count += 1
                self.death_sprite_frequency = 0
            else: self.death_sprite_frequency += 1


list_feather = []