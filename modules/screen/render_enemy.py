from ..enemy import list_feather
from ..enemy import list_animation_death, list_animation_death_birds
from .screen import screen
from .map import list_frog, list_chicken, list_rooster, droped_resources, list_opossum
from .load_all_images import list_run_rooster, list_idle_rooster, list_idle_frog, list_jump_frog, list_run_chicken, list_idle_chicken, list_run_opossum


def render_enemy():
    """
    ### Render all enemy sprites
    """
    for rooster in list_rooster:
        if rooster.is_dead:
            rooster.death(rooster.death_count, screen, list_animation_death_birds) #RENDER DEATH SPRITE
            rooster.dead_count(list_rooster, droped_resources) #CHANGE SPRITE DEATH AND THEN DROPE A MEAT
        else:
            if rooster.random_move >= 0:
                rooster.run(rooster.run_count, screen, rooster.vector_move, list_run_rooster) #RENDER RUN SPRITE
            else:
                rooster.idle(rooster.idle_count, screen, rooster.vector_move, list_idle_rooster) #RENDER IDLE SPRITE

    for feather in list_feather:
        if feather.death_animation:
            feather.death(feather.death_count, screen, list_animation_death)
            if feather.death_count == 6:
                list_feather.remove(feather)

    for chicken in list_chicken:
        if chicken.is_dead:
            chicken.death(chicken.death_count, screen, list_animation_death_birds) #RENDER DEATH SPRITE
            chicken.dead_count(list_chicken, droped_resources) #CHANGE SPRITE DEATH AND THEN DROPE A MEAT
        else:
            if chicken.random_move >= 0:
                chicken.run(chicken.run_count, screen, chicken.vector_move, list_run_chicken) #RENDER RUN SPRITE
            else:
                chicken.idle(chicken.idle_count, screen, chicken.vector_move, list_idle_chicken) #RENDER IDLE SPRITE

    for frog in list_frog:
        if frog.is_dead:
            frog.death(frog.death_count, screen, list_animation_death) #RENDER DEATH SPRITE
            frog.dead_count(list_frog, droped_resources) #CHANGE SPRITE DEATH AND THEN DROPE A MEAT
        else:
            if frog.move_bottom:
                    frog.fall(screen, frog.vector_move, list_jump_frog) #RENDER FALL SPRITE
            elif frog.move_jump:
                    frog.jump(screen, frog.vector_move, list_jump_frog) #RENDER JUMP SPRITE
            else:
                frog.idle(frog.idle_count, screen, frog.vector_move, list_idle_frog) #RENDER IDLE SPRITE

    for opossum in list_opossum:
        if opossum.is_dead:
            opossum.death(opossum.death_count, screen, list_animation_death) #RENDER DEATH SPRITE
            opossum.dead_count(list_opossum, droped_resources) #CHANGE SPRITE DEATH AND THEN DROPE A MEAT
        else:
            opossum.run(opossum.run_count, screen, opossum.vector_move, list_run_opossum) #RENDER RUN SPRITE