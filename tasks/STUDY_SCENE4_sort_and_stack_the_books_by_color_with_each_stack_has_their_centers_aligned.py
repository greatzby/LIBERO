"""This is a standalone file for creating a task in libero."""
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

@register_mu(scene_type="study")
class StudyScene4(InitialSceneTemplates):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
            "wooden_two_layer_shelf": 1,
        }

        object_num_info = {
            "black_book": 2,
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
                region_name="yellow_book_right_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, -0.25],
                region_name="yellow_book_left_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.15],
                region_name="black_book_left_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.20],
                region_name="black_book_right_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
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
            ("On", "yellow_book_2", "study_table_yellow_book_left_init_region"),
            ("On", "black_book_1", "study_table_black_book_left_init_region"),
            ("On", "black_book_2", "study_table_black_book_right_init_region")
        ]
        return states

def main():

    # Write your reward code here
    scene_name = "study_scene4"
    language = "Sort and stack the books by color with each stack has their centers aligned"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["yellow_book_1", "yellow_book_2", "black_book_1", "black_book_2"],
        goal_states=[
            ("Or", ("On", "yellow_book_1", "yellow_book_2"), ("On", "yellow_book_2", "yellow_book_1")),
            ("Or", ("On", "black_book_1", "black_book_2"), ("On", "black_book_2", "black_book_1")),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
