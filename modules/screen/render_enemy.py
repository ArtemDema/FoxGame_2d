from ..enemy import list_run_rooster, list_rooster, list_chicken, list_run_chicken, list_animation_death
from .screen import screen

def render_enemy():
    for rooster in list_rooster:
        if rooster.is_dead:
            rooster.death(rooster.death_count, screen, list_animation_death)
            rooster.dead_count()
        else:
            rooster.run(rooster.run_count, screen, rooster.vector_move, list_run_rooster)
    for chicken in list_chicken:
        if chicken.is_dead:
            chicken.death(chicken.death_count, screen, list_animation_death)
            chicken.dead_count()
        else:
            chicken.run(chicken.run_count, screen, chicken.vector_move, list_run_chicken)