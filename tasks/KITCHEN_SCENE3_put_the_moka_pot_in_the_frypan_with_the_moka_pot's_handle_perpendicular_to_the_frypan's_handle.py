"""This is a standalone file for create a task in libero."""
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

    scene_name = "kitchen_scene3"
    language = "Put the moka pot in the frypan with the moka pot's handle perpendicular to the frypan's handle"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["moka_pot_1", "chefmate_8_frypan_1"],
        goal_states=[
            ("On", "moka_pot_1", "chefmate_8_frypan_1"),
            ("Any",
             (
                ("Equal",
                    ("Minus", ("GetOrientation", "moka_pot_1", "yaw"), ("GetOrientation", "chefmate_8_frypan_1", "yaw")),
                    0,
                    8
                ), 
                ("Equal",
                    ("Minus", ("GetOrientation", "moka_pot_1", "yaw"), ("GetOrientation", "chefmate_8_frypan_1", "yaw")),
                    -180,
                    8
                ),
                ("Equal",
                    ("Minus", ("GetOrientation", "moka_pot_1", "yaw"), ("GetOrientation", "chefmate_8_frypan_1", "yaw")),
                    180,
                    8
                )   
             )
            )
        ]
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
