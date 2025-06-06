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
    scene_name = "living_room_scene2"
    language = "Stand the butter upright on the tomato sauce can"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["tomato_sauce_1","butter_1"],
        goal_states=[
            ("Or", 
                ("AxisAlignedWithin", "butter_1", "x", 0, 5),
                ("AxisAlignedWithin", "butter_1", "x", 175, 180),
            ),
            ("On", "butter_1", "tomato_sauce_1"),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()