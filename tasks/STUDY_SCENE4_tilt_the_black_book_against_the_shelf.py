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


@register_mu(scene_type="study")
class StudyScene4(InitialSceneTemplates):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
            "wooden_two_layer_shelf": 1,
        }

        object_num_info = {
            "black_book": 1,
            "yellow_book": 2,
        }

        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.0],
                region_name="study_table_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.0],
                region_name="yellow_book_right_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.15],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.0],
                region_name="black_book_goal_region",
                target_name=self.workspace_name,
                region_half_len=100.0,  # Large region to ensure the book is in contact
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.28],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(0, 0),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            (
                "On",
                "wooden_two_layer_shelf_1",
                "study_table_wooden_two_layer_shelf_init_region",
            ),
            ("On", "yellow_book_1", "study_table_yellow_book_right_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
        ]
        return states



def main():
    scene_name = "study_scene4"
    language = "Tilt the black book against the shelf"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["wooden_two_layer_shelf_1", "black_book_1"],
        goal_states=[
            ("incontact", "black_book_1", "wooden_two_layer_shelf_1"),
            ("on", "black_book_1", "study_table_black_book_goal_region"),
            ("AxisAlignedWithin", "black_book_1", "z", 0, 60),
        ],
    )


    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
