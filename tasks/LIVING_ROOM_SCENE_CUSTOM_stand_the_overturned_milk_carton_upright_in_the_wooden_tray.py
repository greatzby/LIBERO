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


@register_mu(scene_type="livingroom")
class LivingRoomSceneCustom(InitialSceneTemplates):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
        }
        object_num_info = {
            "milk": 1,
            "wooden_tray": 1
        }

        super().__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.25],
                region_name="milk_init_region",
                target_name=self.workspace_name,
                region_half_len=0.02,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.25],
                region_name="wooden_tray_init_region",
                target_name=self.workspace_name,
                region_half_len=0.02,
            )
        )
    
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )
    
    @property
    def init_states(self):
        states = [
            ("On", "milk_1", "living_room_table_milk_init_region"),
            ("Override_Rotate", "milk_1", "x", "0"),
            ("On", "wooden_tray_1", "living_room_table_wooden_tray_init_region"),
        ]
        return states


def main():

    scene_name = "living_room_scene_custom"
    language = "Stand the overturned milk carton upright in the wooden tray"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["milk_1", "wooden_tray_1"],
        goal_states=[
            ("Upright", "milk_1"),
            ("In", "milk_1", "wooden_tray_1_contain_region"),
            ("Upright", "wooden_tray_1")
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
