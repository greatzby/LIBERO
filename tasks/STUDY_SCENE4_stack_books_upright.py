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
    language = "Place the yellow book on top of the black book, with both books upright."
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["black_book_1", "yellow_book_1", "yellow_book_2"],
        goal_states=[
            ("Or", 
                ("All", (
                    ("RelaxedOn", "yellow_book_1", "black_book_1"),
                    ("AxisAlignedWithin", "black_book_1", "z", 0, 5),
                    ("AxisAlignedWithin", "yellow_book_1", "z", 0, 5),
                    ("PositionWithin", "yellow_book_1", 1, 1, 1.01, 1000, 1000, 0.01),
                )),
                ("All", (
                    ("RelaxedOn", "yellow_book_2", "black_book_1"),
                    ("AxisAlignedWithin", "black_book_1", "z", 0, 5),
                    ("AxisAlignedWithin", "yellow_book_2", "z", 0, 5),
                    ("PositionWithin", "yellow_book_2", 1, 1, 1.01, 1000, 1000, 0.01),
                ))
            )
        ],
    )


    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()