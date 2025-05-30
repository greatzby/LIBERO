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


@register_mu(scene_type="living_room")
class LivingRoomScene4(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "living_room_table": 1,
        }

        object_num_info = {
            "akita_black_bowl": 2,
            "new_salad_dressing": 1,
            "chocolate_pudding": 1,
            "wooden_tray": 1,
        }

        super().__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.26],
                region_name="wooden_tray_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, -0.20],
                region_name="chocolate_pudding_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, 0.05],
                region_name="akita_black_bowl_right_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.10, -0.15],
                region_name="akita_black_bowl_left_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.25, -0.10],
                region_name="salad_dressing_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
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
                "chocolate_pudding_1",
                "living_room_table_chocolate_pudding_init_region",
            ),
            (
                "On",
                "akita_black_bowl_1",
                "living_room_table_akita_black_bowl_left_init_region",
            ),
            (
                "On",
                "akita_black_bowl_2",
                "living_room_table_akita_black_bowl_right_init_region",
            ),
            (
                "On",
                "new_salad_dressing_1",
                "living_room_table_salad_dressing_init_region",
            ),
            ("On", "wooden_tray_1", "living_room_table_wooden_tray_init_region"),
        ]
        return states


def main():
    # living_room_scene_4
    scene_name = "living_room_scene4"
    language = "Stack the two bowls together"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["akita_black_bowl_1", "akita_black_bowl_2"],
        goal_states=[
            ("StackBowl", "akita_black_bowl_1", "akita_black_bowl_2"),
        ],
    )


    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
