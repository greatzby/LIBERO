"""This is a standalone file for creating a task in libero."""
import numpy as np

from libero.libero.utils.bddl_generation_utils import (
    get_xy_region_kwargs_list_from_regions_info,
)
from libero.libero.utils.mu_utils import register_mu, InitialSceneTemplates
from libero.libero.utils.task_generation_utils import (
    register_task_info,
    get_task_info,
    generate_bddl_from_task_info,
)

from libero.libero.benchmark.mu_creation import *

def main():

    # Write your reward code here
    scene_name = "kitchen_scene8"
    language = "Place left pot on stove's heat region and right on stove but not heat"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["moka_pot_1", "moka_pot_2", "flat_stove_1"],
        goal_states = [
            ("On", "moka_pot_2", "flat_stove_1_cook_region"),
            ("Not", ("On", "moka_pot_1", "flat_stove_1_cook_region")),
            ("RelaxedOn", "moka_pot_1", "flat_stove_1"),
            ("Upright", "moka_pot_2"),
            ("Upright", "moka_pot_1"),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)

if __name__ == "__main__":
    main()
