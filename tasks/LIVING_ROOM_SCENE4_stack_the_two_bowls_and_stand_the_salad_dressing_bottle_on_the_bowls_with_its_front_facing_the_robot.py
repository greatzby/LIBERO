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
    language = "Stack the left bowl onto the right bowl and stand the salad dressing bottle on the bowls with its front facing the robot"

    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["akita_black_bowl_1", "akita_black_bowl_2", "new_salad_dressing_1"],
        goal_states=[
            
            ("on", "akita_black_bowl_1", "akita_black_bowl_2"),
            ("upright", "akita_black_bowl_1"),
            ("upright", "akita_black_bowl_2"),

            ("on", "new_salad_dressing_1", "akita_black_bowl_1"),
            

            ("axisalignedwithinworldaxis",
                "new_salad_dressing_1", "z", 0, 15, "x"), 
            
                
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)

if __name__ == "__main__":
    main()