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

<<<<<<< HEAD
from libero.libero.benchmark.mu_creation import LivingRoomScene2

def main():
    scene_name = "living_room_scene2"
    language = "Arrange the ketchup, alphabet soup, and orange juice in a straight line with the ketchup upside down and the other two upright"

    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["ketchup_1", "alphabet_soup_1", "orange_juice_1"],
        goal_states=[
            ("upsidedown", "ketchup_1"),
            ("upright", "alphabet_soup_1"),
            ("upright", "orange_juice_1"),
            ("linear", "ketchup_1", "alphabet_soup_1", "orange_juice_1", 0.05),
        ],
=======

@register_mu(scene_type="kitchen")
class KitchenScene2(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "akita_black_bowl": 3,
            "plate": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.30],
                region_name="wooden_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.20],
                region_name="akita_black_bowl_middle_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.15],
                region_name="akita_black_bowl_front_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.05],
                region_name="akita_black_bowl_back_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.0],
                region_name="plate_init_region",
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
                "akita_black_bowl_1",
                "kitchen_table_akita_black_bowl_front_init_region",
            ),
            (
                "On",
                "akita_black_bowl_2",
                "kitchen_table_akita_black_bowl_middle_init_region",
            ),
            (
                "On",
                "akita_black_bowl_3",
                "kitchen_table_akita_black_bowl_back_init_region",
            ),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("On", "wooden_cabinet_1", "kitchen_table_wooden_cabinet_init_region"),
        ]
        return states


def main():
    # kitchen_scene_2
    scene_name = "kitchen_scene2"
    language = "Stack the three bowls in the top drawer"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["wooden_cabinet_1", "akita_black_bowl_1", "akita_black_bowl_2", "akita_black_bowl_3"],
        goal_states=[
            ("Any", (
                ("All", (
                    # 1, 2, 3 / 3, 2, 1 
                    ("StackBowl", "akita_black_bowl_1", "akita_black_bowl_2"),
                    ("StackBowl", "akita_black_bowl_2", "akita_black_bowl_3"),
                    )),
                ("All", (
                    # 1, 3, 2 / 2, 3, 1
                    ("StackBowl", "akita_black_bowl_1", "akita_black_bowl_3"),
                    ("StackBowl", "akita_black_bowl_3", "akita_black_bowl_2"),
                    )),
                ("All", (
                    # 2, 1, 3 / 3, 1, 2
                    ("StackBowl", "akita_black_bowl_2", "akita_black_bowl_1"),
                    ("StackBowl", "akita_black_bowl_1", "akita_black_bowl_3"),
                    )),
                ),
            ),
            ("In", "akita_black_bowl_1", "wooden_cabinet_1_top_region"),
            ("In", "akita_black_bowl_2", "wooden_cabinet_1_top_region"),
            ("In", "akita_black_bowl_3", "wooden_cabinet_1_top_region"),
            ("Upright", "akita_black_bowl_1"),
            ("Upright", "akita_black_bowl_2"),
            ("Upright", "akita_black_bowl_3"),
            # ("Close", "wooden_cabinet_1_top_region"),
        ]
>>>>>>> upstream/master
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)

if __name__ == "__main__":
    main()