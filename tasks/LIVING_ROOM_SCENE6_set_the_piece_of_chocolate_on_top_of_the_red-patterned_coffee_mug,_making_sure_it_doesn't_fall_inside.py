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

from libero.libero.benchmark.mu_creation import LivingRoomScene6


def main():

    # Write your reward code here
    scene_name = "living_room_scene6"
    language = "Set the piece of chocolate on top of the red-patterned coffee mug, making sure it doesn't fall inside"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["chocolate_pudding_1", "red_coffee_mug_1"],
        goal_states=[
            ("On", "chocolate_pudding_1", "red_coffee_mug_1"),
            ("PosiGreaterThan", "chocolate_pudding_1", "z", 0.582),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
