"""This is a standalone file for create a task in libero."""
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
    scene_name = "study_scene3"
    language = "Keep the book upright and elevate the white cup to be exactly level with the book's top surface and keep it upright"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["porcelain_mug_1", "black_book_1"],
        goal_states=[
            ("AxisAlignedWithin", "black_book_1", "z", 0, 5),
            ("AxisAlignedWithin", "porcelain_mug_1", "z", 0, 5),
            
        ],
    )


    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
