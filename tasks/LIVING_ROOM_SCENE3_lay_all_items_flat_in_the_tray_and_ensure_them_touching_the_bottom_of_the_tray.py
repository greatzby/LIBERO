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
    language = "Lay all items flat in the tray and ensure them touching the bottom of the tray"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["alphabet_soup_1", "cream_cheese_1", "tomato_sauce_1", "ketchup_1", "butter_1", "wooden_tray_1"],
        goal_states=[
            ("RelaxedOn", "alphabet_soup_1", "wooden_tray_1"),
            ("RelaxedOn", "cream_cheese_1", "wooden_tray_1"),
            ("RelaxedOn", "tomato_sauce_1", "wooden_tray_1"),
            ("RelaxedOn", "ketchup_1", "wooden_tray_1"),
            ("RelaxedOn", "butter_1", "wooden_tray_1"),
            ("InContact", "alphabet_soup_1", "wooden_tray_1"),
            ("InContact", "cream_cheese_1", "wooden_tray_1"),
            ("InContact", "tomato_sauce_1", "wooden_tray_1"),
            ("InContact", "ketchup_1", "wooden_tray_1"),
            ("InContact", "butter_1", "wooden_tray_1"),
            ("AxisAlignedWithinWorldAxis", "alphabet_soup_1", "y", 85, 95, "z"),
            ("AxisAlignedWithinWorldAxis", "tomato_sauce_1", "y", 85, 95, "z"),
            ("Or", ("AxisAlignedWithinWorldAxis", "cream_cheese_1", "z", 0, 5, "z"), ("AxisAlignedWithinWorldAxis", "cream_cheese_1", "z", 175, 180, "z")),
            ("Or", ("AxisAlignedWithinWorldAxis", "butter_1", "z", 0, 5, "z"), ("AxisAlignedWithinWorldAxis", "butter_1", "z", 175, 180, "z")),
            ("Or", ("AxisAlignedWithinWorldAxis", "ketchup_1", "z", 0, 5, "z"), ("AxisAlignedWithinWorldAxis", "ketchup_1", "z", 175, 180, "z")),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
