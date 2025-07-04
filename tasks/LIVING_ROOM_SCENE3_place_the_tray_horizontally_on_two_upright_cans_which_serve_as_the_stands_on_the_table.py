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
    scene_name = "living_room_scene3"
    language = "Place the tray horizontally on two upright cans which serve as the stands on the table"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["wooden_tray_1", "alphabet_soup_1", "tomato_sauce_1"],
        goal_states=[
            ("RelaxedOn", "wooden_tray_1", "alphabet_soup_1"),
            ("RelaxedOn", "wooden_tray_1", "tomato_sauce_1"),
            ("AxisAlignedWithin", "alphabet_soup_1", "y", 0, 10),
            ("AxisAlignedWithin", "tomato_sauce_1", "y", 0, 10),
            ("AxisAlignedWithin", "wooden_tray_1", "x", 80, 100),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
