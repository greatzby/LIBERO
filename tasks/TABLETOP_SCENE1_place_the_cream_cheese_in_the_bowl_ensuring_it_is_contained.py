"""This is an exmaple file for creating a task in libero."""
import numpy as np
import libero.libero.benchmark.mu_creation
from libero.libero.utils.bddl_generation_utils import (
    get_xy_region_kwargs_list_from_regions_info,
)
from libero.libero.utils.mu_utils import register_mu, InitialSceneTemplates
from libero.libero.utils.task_generation_utils import (
    register_task_info,
    get_task_info,
    generate_bddl_from_task_info,
)



def main():
  
    scene_name = "tabletop_scene1"
    language = "Place the cream cheese in the bowl ensuring it is contained"
    register_task_info(
        language=language,
        scene_name=scene_name,
        objects_of_interest=["cream_cheese_1", "akita_black_bowl_1"],
        goal_states=[
            
            ("InContact", "cream_cheese_1", "akita_black_bowl_1")
        ],
    )
    
    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
