"""This is a standalone file for create a task in libero."""
from libero.libero.utils.bddl_generation_utils import (
    get_xy_region_kwargs_list_from_regions_info,
)
from libero.libero.utils.mu_utils import register_mu, InitialSceneTemplates
from libero.libero.utils.task_generation_utils import (
    register_task_info,
    generate_bddl_from_task_info,
)
import numpy as np

from libero.libero.benchmark.mu_creation import TabletopScene1

def main():
    scene_name = "tabletop_scene1"
    language = "Heat the wine without letting it come into direct contact with the stove"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["akita_black_bowl_1", "flat_stove_1", "wine_bottle_1", "plate_1"],
        goal_states=[
            ("TurnOn", "flat_stove_1"),
            ("Or", ("And", ("On", "wine_bottle_1", "akita_black_bowl_1"), ("On", "akita_black_bowl_1", "flat_stove_1_cook_region")), ("And", ("On", "wine_bottle_1", "plate_1"), ("On", "plate_1", "flat_stove_1_cook_region"))),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
