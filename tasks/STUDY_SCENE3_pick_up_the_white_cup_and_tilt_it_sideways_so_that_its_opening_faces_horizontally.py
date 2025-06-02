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

@register_mu(scene_type="study")
class StudyScene3(InitialSceneTemplates):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
            "desk_caddy": 1,
        }

        object_num_info = {
            "black_book": 1,
            "red_coffee_mug": 1,
            "porcelain_mug": 1,
        }

        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.20, 0.15],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.15],
                region_name="red_coffee_mug_behind_region",
                target_name=self.workspace_name,
                region_half_len=0.05,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.0],
                region_name="porcelain_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.0],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.20, -0.14],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.15],
                region_name="desk_caddy_front_left_contain_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.20, 0.15],
                region_name="desk_caddy_right_region",
                target_name=self.workspace_name,
                region_half_len=0.05,
                yaw_rotation=(np.pi, np.pi),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "black_book_1", "study_table_desk_caddy_front_left_contain_region"),
            ("On", "porcelain_mug_1", "study_table_porcelain_mug_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]
        return states
    

def main():
    # study_scene3
    scene_name = "study_scene3"
    language = "Pick up the white cup and tilt it sideways so that its opening faces horizontally"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["porcelain_mug_1"],
        goal_states=[
            ("posigreaterthan", "porcelain_mug_1", "z", 1.0),
            ("axisalignedwithin", "porcelain_mug_1", "z",85, 95),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
