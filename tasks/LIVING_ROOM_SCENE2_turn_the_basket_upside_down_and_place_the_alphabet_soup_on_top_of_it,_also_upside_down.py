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

from libero.libero.benchmark.mu_creation import LivingRoomScene2

def main():

    scene_name = "living_room_scene2"
    language = "Turn the basket upside down and place the alphabet soup on top of it, also upside down"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["basket_1", "alphabet_soup_1"],
        goal_states=[
            ("UpsideDown", "basket_1"),
            ("On", "alphabet_soup_1", "basket_1"),
            ("AxisAlignedWithin", "alphabet_soup_1", "y", 170, 180),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
