from ...main_classes import Enemy, Block
from ...resourses import Discarded_Item
from ...interface import interface
from .feather import list_feather, Feather

import random, math, pygame

class Rooster(Enemy, Block):
    """
    ### Rooster class with aggressive character
    """
    def __init__(self, x, y, width, height, image, hp, speed, vector_move, sprite_frequency_rooster, is_dead, death_count):
        self.vector_move = vector_move
        self.run_count = 0
        self.random_idle = 0
        self.random_move = 0
        self.sprite_frequency_rooster = sprite_frequency_rooster
        self.is_dead = is_dead
        self.death_count = death_count
        self.player_visibility = False
        self.idle_count = 0
        self.angle = 0
        self.timer_throw_feather = 20
        Enemy.__init__(self, x, y, width, height, image, hp, speed)

    def move(self, player, blocks, chests, boxes, sound_damage): #RUN ROOSTER
        if self.player_visibility:
            if player.hide == False:
                distance = player.x - self.x
                if distance <= 0:
                    self.random_move = 75
                    self.vector_move = 0
                    if self.timer_throw_feather <= 0:
                        self.throw_rooster_feather(player)
                        feather = Feather(self.x, self.y + (self.height // 2), 25, 25, "images/enemy/rooster/feather/0.png", self.angle)
                        feather.image = pygame.transform.rotate(feather.image, self.angle - 240)
                        list_feather.append(feather)
                        self.timer_throw_feather = 100
                    else:
                        self.timer_throw_feather -= 1
                else:
                    self.random_move = 75
                    self.vector_move = 1
                    if self.timer_throw_feather <= 0:
                        self.throw_rooster_feather(player)
                        feather = Feather(self.x, self.y + (self.height // 2) + 3, 25, 25, "images/enemy/rooster/feather/0.png", self.angle)
                        feather.image = pygame.transform.rotate(feather.image, self.angle - 200)
                        list_feather.append(feather)
                        self.timer_throw_feather = 100
                    else:
                        self.timer_throw_feather -= 1
 
        if self.random_move >= 0:
            if self.vector_move == 0:
                if player.hide == False:
                    answer = player.check_collision_right(self.x, self.y, self.x + self.width, self.y + self.height)
                    if answer:
                        player.damage_player(sound_damage)

                for block in blocks: #CHECKING IF THERE IS SOIL AT THE FUTURE LOCATION OF THE POINT
                    answer = block.check_collision_top_wall(self.x - 15, self.y, self.x + self.width - 15, self.y + self.height + 20)
                    if answer:
                        break
                    
                if answer:
                    list_of_all_blocks = []
                    list_of_all_blocks += blocks
                    list_of_all_blocks += chests
                    list_of_all_blocks += boxes

                    for block in list_of_all_blocks: #CHECK TOUCH RIGHT WALL OF BLOCK
                        answer = block.check_collision_right_wall(self.x, self.y, 
                                                                self.x + self.width, self.y + self.height)
                        if answer:
                            if self.run_count == 3: 
                                self.run_count = 0
                            else:
                                if self.sprite_frequency_rooster >= 10: 
                                    self.run_count += 1
                                    self.sprite_frequency_rooster = 0
                                else: self.sprite_frequency_rooster += 1
                            self.random_move =- 1
                            return

                    if answer != True:
                        self.x -= self.speed
                        self.random_move -= self.speed

                        if self.run_count == 3: 
                            self.run_count = 0
                        else:
                            if self.sprite_frequency_rooster >= 10: 
                                self.run_count += 1
                                self.sprite_frequency_rooster = 0
                            else: self.sprite_frequency_rooster += 1
                else:
                    self.random_move = -1
            else:
                if player.hide == False:
                    answer = player.check_collision_left(self.x, self.y, self.x + self.width, self.y + self.height)
                    if answer:
                        player.damage_player(sound_damage)

                for block in blocks: #CHECKING IF THERE IS SOIL AT THE FUTURE LOCATION OF THE POINT
                    answer = block.check_collision_top_wall(self.x + 15, self.y, self.x + self.width + 15, self.y + self.height + 20)
                    if answer:
                        break
                    
                if answer:
                    list_of_all_blocks = []
                    list_of_all_blocks += blocks
                    list_of_all_blocks += chests
                    list_of_all_blocks += boxes

                    for block in list_of_all_blocks: #CHECK TOUCH RIGHT WALL OF BLOCK
                        answer = block.check_collision_left_wall(self.x, self.y, 
                                                                self.x + self.width, self.y + self.height)
                        if answer:
                            if self.run_count == 3: 
                                self.run_count = 0
                            else:
                                if self.sprite_frequency_rooster >= 10: 
                                    self.run_count += 1
                                    self.sprite_frequency_rooster = 0
                                else: self.sprite_frequency_rooster += 1
                            self.random_move =- 1
                            return

                    if answer != True:
                        self.x += self.speed
                        self.random_move -= self.speed

                        if self.run_count == 3: 
                            self.run_count = 0
                        else:
                            if self.sprite_frequency_rooster == 10: 
                                self.run_count += 1
                                self.sprite_frequency_rooster = 0
                            else: self.sprite_frequency_rooster += 1
                else:
                    self.random_move = -1
        elif self.random_idle >= 0:
            self.random_idle -= 1
            if self.idle_count == 3: 
                self.idle_count = 0
            else:
                if self.sprite_frequency_rooster >= 10: 
                    self.idle_count += 1
                    self.sprite_frequency_rooster = 0
                else: self.sprite_frequency_rooster += 1
            return
        else:
            self.actions_rooster()

    def actions_rooster(self): #RANDOM ACTION
        random_antion = random.randint(0, 1)
        if random_antion == 0:
            self.random_idle = random.randint(120, 260)
        else:
            self.vector_move = random.randint(0, 1)
            self.random_move = random.randint(50, 250)
    
    def check_death(self, player, boxes, move_bottom, task_enemy, death_enemy): #CHECK DEATH opossum
        if self.is_dead == False:
            for box in boxes:
                answer = box.check_collision_bottom_wall(self.x, self.y, #CHECK BOX FOR DEATH
                                                        self.x + self.width, self.y + self.height)
                if answer:
                    self.is_dead = True
                    interface[5].count += 1
                    task_enemy -= 1
                    death_enemy.set_volume(0.1)
                    death_enemy.play(loops = 0)

            if move_bottom == True:
                right_x = self.x + self.width
                bottom_y = self.y + self.height

                bottom_y_p = player.y + player.height
                left_x_p = player.x
                right_x_p = player.x + player.width
                top_y_p = player.y
                #left angle
                if bottom_y_p >= self.y:
                    if left_x_p + 33 <= self.x:
                        if right_x_p - 30 >= self.x:
                            if top_y_p + 20 <= self.y:
                                if bottom_y_p + 10 <= bottom_y:
                                    self.is_dead = True
                                    interface[5].count += 1
                                    task_enemy -= 1
                                    death_enemy.set_volume(0.1)
                                    death_enemy.play(loops = 0)

                #middle (golden)
                if bottom_y_p >= self.y:
                    if left_x_p + 33 >= self.x:
                        if right_x_p - 30 <= right_x:
                            if top_y_p + 20 <= self.y:
                                if bottom_y_p + 10 <= bottom_y:
                                    self.is_dead = True
                                    interface[5].count += 1
                                    task_enemy -= 1
                                    death_enemy.set_volume(0.1)
                                    death_enemy.play(loops = 0)
                                            
                #right angle
                if bottom_y_p >= self.y:
                    if left_x_p + 33 <= right_x:
                        if right_x_p - 30 >= right_x:
                            if top_y_p + 20 <= self.y:
                                if bottom_y_p + 10 <= bottom_y:
                                    self.is_dead = True
                                    interface[5].count += 1
                                    task_enemy -= 1
                                    death_enemy.set_volume(0.1)
                                    death_enemy.play(loops = 0)
        return task_enemy

    def throw_rooster_feather(self, player):
        randian = math.atan2(self.y - player.y, self.x - player.x)
        self.angle = (randian * 180 / math.pi) - 180

    def dead_count(self, list_rooster, droped_resources): #CHANGE SPRITE DEATH AND THEN DROPE A MEAT
        if self.death_count == 6:
            meat1 = Discarded_Item(x = self.x, y = self.y, width = 50, height = 25, image = "images/resources/meat.png", whatIsThis= "meat")
            droped_resources.append(meat1)
            list_rooster.remove(self)
            self.x = 10000
            self.y = 10000
        else:
            if self.sprite_frequency_rooster >= 10: 
                self.death_count += 1
                self.sprite_frequency_rooster = 0
            else: self.sprite_frequency_rooster += 1