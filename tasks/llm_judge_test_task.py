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

from libero.libero.benchmark.mu_creation import *

@register_mu(scene_type="kitchen")
class KitchenScene4(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "white_cabinet": 1,
            "wine_rack": 1,
        }

        object_num_info = {"wine_bottle": 1}

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.30],
                region_name="white_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.10, -0.30],
                region_name="wine_rack_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )


        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.05],
                region_name="wine_bottle_init_region",
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
            ("On", "wine_bottle_1", "kitchen_table_wine_bottle_init_region"),
            ("On", "white_cabinet_1", "kitchen_table_white_cabinet_init_region"),
            ("On", "wine_rack_1", "kitchen_table_wine_rack_init_region"),
        ]
        return states

def main():
    scene_name = "kitchen_scene4"
    language = "In the scene, there is a wine rack, a wine bottle, and a three-drawer cabinet. Open the top drawer, and put the wine bottle in the drawer so that its leaning towards the lefthand side of the camera view"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["wine_bottle_1"],
        goal_states=[
            ("NeuralJudge", )
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
