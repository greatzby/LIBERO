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

from libero.libero.benchmark.mu_creation import LivingRoomScene3

def main():

    scene_name = "living_room_scene2"
    language = "Put the two cans on two side of the milk while keeping them in contact"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["milk_1", "alphabet_soup_1", "tomato_sauce_1"],
        goal_states=[
            ("Between", "alphabet_soup_1", "milk_1", "tomato_sauce_1", "x"),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
