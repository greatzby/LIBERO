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
    language = "Lean the black book against the shelf, then lean the yellow book against the black book"
    register_task_info(
        language=language,
        scene_name=scene_name,
        objects_of_interest=["black_book_1", "yellow_book_1", "yellow_book_2", "wooden_two_layer_shelf_1"],
        goal_states=[
            ("InContact", "black_book_1", "wooden_two_layer_shelf_1"),
            ("Not", ("InContact", "yellow_book_1", "wooden_two_layer_shelf_1")),
            ("AxisAlignedWithin", "black_book_1", "z", 10, 80),
            (
                "Or",
                (   
                    "And", 
                        ("InContact", "black_book_1", "yellow_book_1"),
                        ("AxisAlignedWithin", "yellow_book_1", "z", 10, 80),
                ),
                (
                    "And",
                        ("InContact", "black_book_1", "yellow_book_2"),
                        ("AxisAlignedWithin", "yellow_book_2", "z", 10, 80),
                )
            )
        ],
    )

    bddl, _ = generate_bddl_from_task_info()
    print(bddl)


if __name__ == "__main__":
    main()
