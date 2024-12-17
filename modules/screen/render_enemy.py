from ..enemy import list_enemy, list_run_rooster, list_rooster, list_chicken, list_run_chicken
from .screen import screen

def render_enemy():
    for rooster in list_rooster:
        rooster.run(rooster.run_count, screen, rooster.vector_move, list_run_rooster)
    for chicken in list_chicken:
        chicken.run(chicken.run_count, screen, chicken.vector_move, list_run_chicken)