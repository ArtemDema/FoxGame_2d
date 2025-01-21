from ..enemy import list_run_rooster
from ..enemy import list_run_chicken, list_animation_death, list_jump_frog, list_idle_frog, list_animation_death_birds, list_idle_chicken, list_idle_rooster
from .screen import screen
from .map import list_frog, list_chicken, list_rooster


def render_enemy():
    for rooster in list_rooster:
        if rooster.is_dead:
            rooster.death(rooster.death_count, screen, list_animation_death_birds) #RENDER DEATH SPRITE
            rooster.dead_count(list_rooster) #CHANGE SPRITE DEATH AND THEN DROPE A MEAT
        else:
            if rooster.random_move >= 0:
                rooster.run(rooster.run_count, screen, rooster.vector_move, list_run_rooster) #RENDER RUN SPRITE
            else:
                rooster.idle(rooster.idle_count, screen, rooster.vector_move, list_idle_rooster) #RENDER IDLE SPRITE

    for chicken in list_chicken:
        if chicken.is_dead:
            chicken.death(chicken.death_count, screen, list_animation_death_birds) #RENDER DEATH SPRITE
            chicken.dead_count(list_chicken) #CHANGE SPRITE DEATH AND THEN DROPE A MEAT
        else:
            if chicken.random_move >= 0:
                chicken.run(chicken.run_count, screen, chicken.vector_move, list_run_chicken) #RENDER RUN SPRITE
            else:
                chicken.idle(chicken.idle_count, screen, chicken.vector_move, list_idle_chicken) #RENDER IDLE SPRITE

    for frog in list_frog:
        if frog.is_dead:
            frog.death(frog.death_count, screen, list_animation_death) #RENDER DEATH SPRITE
            frog.dead_count(list_frog) #CHANGE SPRITE DEATH AND THEN DROPE A MEAT
        else:
            if frog.angle > 0:
                frog.fall(screen, frog.vector_move, list_jump_frog) #RENDER FALL SPRITE
            else:
                frog.idle(frog.idle_count, screen, frog.vector_move, list_idle_frog) #RENDER IDLE SPRITE