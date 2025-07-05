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

from libero.libero.benchmark.mu_creation import LivingRoomScene4

def main():
    scene_name = "living_room_scene4"
    language = "Lift the chocolate pudding box at least five centimetres above the table and tilt it so it rests on its long side"

    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["chocolate_pudding_1"],
        goal_states=[
            
            # 1) The long side of the box is vertical: the angle between the local z-axis and the world Z+is 80 to 100 °
            ("axisalignedwithin", "chocolate_pudding_1", "z", 80, 100),

            # 2) z ≥ 0.46 m ⇒ At least 5 cm away from the desktop
            ("posigreaterthan",  "chocolate_pudding_1", "z", 0.46),

            
            
            
                
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)

if __name__ == "__main__":
    main()