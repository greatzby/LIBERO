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
    language = "Stack the three books so that the black book is sandwiched between two yellow books, with their centers aligned and keep all the books flat"
    register_task_info(
        language=language,
        scene_name=scene_name,
        objects_of_interest=["black_book_1", "yellow_book_1", "yellow_book_2"],
        goal_states=[
            (
                "Or",
                (
                    "And",
                    ("On", "black_book_1", "yellow_book_1"),
                    ("On", "yellow_book_2", "black_book_1"),
                ),
                (
                    "And",
                    ("On", "black_book_1", "yellow_book_2"),
                    ("On", "yellow_book_1", "black_book_1"),
                ),
            ),
            ("AxisAlignedWithin", "yellow_book_1", "z", 85, 95),
            ("AxisAlignedWithin", "yellow_book_2", "z", 85, 95),
            ("AxisAlignedWithin", "black_book_1", "z", 85, 95),
        ],
    )

    bddl, _ = generate_bddl_from_task_info()
    print(bddl)


if __name__ == "__main__":
    main()
