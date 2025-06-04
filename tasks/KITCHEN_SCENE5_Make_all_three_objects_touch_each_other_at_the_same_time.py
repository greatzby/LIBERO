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
    scene_name = "kitchen_scene5"
    language = "Make ketchup, plate and bowl touch each other at the same time"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["ketchup_1", "plate_1", "akita_black_bowl_1"],
        goal_states=[
            ("InContact", "ketchup_1", "plate_1"),
            ("InContact", "ketchup_1", "akita_black_bowl_1"),
            ("InContact", "plate_1", "akita_black_bowl_1"),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
