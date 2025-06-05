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


@register_mu("living_room")
class CustomizedLivingRoomScene2(InitialSceneTemplates):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
        }
        object_num_info = {
            "tomato_sauce": 2,
            "basket": 1,
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
                region_name="basket_init_region",
                target_name=self.workspace_name,
                region_half_len=0.05,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, 0.05],
                region_name="tomato_sauce_L_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.25],
                region_name="tomato_sauce_R_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "tomato_sauce_1", "living_room_table_tomato_sauce_L_init_region"),
            ("On", "tomato_sauce_2", "living_room_table_tomato_sauce_R_init_region"),
            ("On", "basket_1", "living_room_table_basket_init_region"),
        ]


def main():
    scene_name = "customized_living_room_scene2"
    language = "Put two bottles diagonally across from each other inside the basket"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["tomato_sauce_2", "tomato_sauce_1", "basket_1"],
        goal_states=[
            ("In", "tomato_sauce_1", "basket_1_contain_region"),
            ("In", "tomato_sauce_2", "basket_1_contain_region"),
            ("InContact", "tomato_sauce_1", "basket_1"),
            ("InContact", "tomato_sauce_2", "basket_1"),
            ("Not", ("InContact", "tomato_sauce_1", "tomato_sauce_2")),
            (
                "or",
                ("linear", 0.005, "tomato_sauce_1", "basket_1", "tomato_sauce_2"),
                ("linear", 0.005, "tomato_sauce_2", "basket_1", "tomato_sauce_1"),
            ),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
