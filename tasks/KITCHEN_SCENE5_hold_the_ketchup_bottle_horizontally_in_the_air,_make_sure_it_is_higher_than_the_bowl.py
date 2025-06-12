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
    language = "Hold the ketchup bottle horizontally in the air, make sure it is higher than the bowl"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["ketchup_1"],
        goal_states=[
            ("InAir", "ketchup_1", 1),
            ("AxisAlignedWithin", "ketchup_1", "y", 85, 95),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
