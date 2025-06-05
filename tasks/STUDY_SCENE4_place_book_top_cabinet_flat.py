from libero.libero.utils.bddl_generation_utils import (
    get_xy_region_kwargs_list_from_regions_info,
)
from libero.libero.utils.mu_utils import register_mu, InitialSceneTemplates
from libero.libero.utils.task_generation_utils import (
    generate_bddl_from_task_info,
    register_task_info,
)

from libero.libero.benchmark.mu_creation import StudyScene4

def main():
    scene_name = "study_scene4"
    language = "Place the black book on the top side of the bookshelf, laying it flat."
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["wooden_two_layer_shelf_1", "black_book_1"],
        goal_states=[
            ("On", "black_book_1", "wooden_two_layer_shelf_1_top_side"),
            ("AxisAlignedWithin", "black_book_1", "z", 85, 95),
        ],
    )


    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()