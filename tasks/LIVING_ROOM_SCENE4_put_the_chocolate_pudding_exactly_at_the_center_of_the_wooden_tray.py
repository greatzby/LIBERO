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
    language = "Put the chocolate pudding exactly at the center of the wooden tray"

    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["chocolate_pudding_1", "wooden_tray_1"],
        goal_states=[
            
            # Position error ± 2cm
            ("positionwithinobject", "chocolate_pudding_1", "wooden_tray_1",
             -0.02, -0.02, -0.05, 0.02, 0.02, 0.05),
            ("incontact","chocolate_pudding_1", "wooden_tray_1"),
            # Constraint: keep the pallet level throughout the whole process (to prevent users from tilting the pallet to cheat)
            ("constraintalways", ("upright", "wooden_tray_1")),            
            
                
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)

if __name__ == "__main__":
    main()