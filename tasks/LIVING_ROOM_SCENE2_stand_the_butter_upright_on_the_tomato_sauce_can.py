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
class LivingRoomScene2(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "living_room_table": 1,
        }

        object_num_info = {
            "alphabet_soup": 1,
            "cream_cheese": 1,
            "tomato_sauce": 1,
            "ketchup": 1,
            "orange_juice": 1,
            "milk": 1,
            "butter": 1,
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
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.10],
                region_name="milk_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, -0.20],
                region_name="cream_cheese_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.25],
                region_name="orange_juice_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, 0.05],
                region_name="tomato_sauce_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.10, -0.15],
                region_name="alphabet_soup_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.05],
                region_name="butter_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.25, -0.15],
                region_name="ketchup_init_region",
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
            ("On", "alphabet_soup_1", "living_room_table_alphabet_soup_init_region"),
            ("On", "cream_cheese_1", "living_room_table_cream_cheese_init_region"),
            ("On", "tomato_sauce_1", "living_room_table_tomato_sauce_init_region"),
            ("On", "ketchup_1", "living_room_table_ketchup_init_region"),
            ("On", "milk_1", "living_room_table_milk_init_region"),
            ("On", "orange_juice_1", "living_room_table_orange_juice_init_region"),
            ("On", "butter_1", "living_room_table_butter_init_region"),
            ("On", "basket_1", "living_room_table_basket_init_region"),
        ]
        return states

def main():
    scene_name = "living_room_scene2"
    language = "Stand the butter upright on the tomato sauce can"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["tomato_sauce_1","butter_1"],
        goal_states=[
            ("Or", 
                ("AxisAlignedWithin", "butter_1", "x", 0, 5),
                ("AxisAlignedWithin", "butter_1", "x", 175, 180),
            ),
            ("On", "butter_1", "tomato_sauce_1"),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()