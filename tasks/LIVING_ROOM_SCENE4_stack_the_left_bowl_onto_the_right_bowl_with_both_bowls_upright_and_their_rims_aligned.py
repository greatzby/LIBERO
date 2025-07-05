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
    language = "Stack the left bowl onto the right bowl with both bowls upright and their rims aligned"

    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["akita_black_bowl_1", "akita_black_bowl_2"],
        goal_states=[
            
             # Make sure that 1 is on 2 and contacts and is concentric horizontally
            ("on", "akita_black_bowl_1", "akita_black_bowl_2"),
            
            ("upright", "akita_black_bowl_1"),
            ("upright", "akita_black_bowl_2"),               
            
                
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)

if __name__ == "__main__":
    main()