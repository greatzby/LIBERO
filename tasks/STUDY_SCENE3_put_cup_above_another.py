from libero.libero.utils.bddl_generation_utils import (
    get_xy_region_kwargs_list_from_regions_info,
)
from libero.libero.utils.mu_utils import register_mu, InitialSceneTemplates
from libero.libero.utils.task_generation_utils import (
    generate_bddl_from_task_info,
    register_task_info,
)


@register_mu(scene_type="study")
class StudyScene3(InitialSceneTemplates):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
        }

        object_num_info = {
            "red_coffee_mug": 1,
            "white_yellow_mug": 1,
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
                region_name="white_yellow_mug_init_region",
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
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
        ]
        return states


def main():
    scene_name = "study_scene3"
    language = "Pick up the white-yellow cup, flip it upside down, and hold it directly above the red cup."
    register_task_info(
        language=language,
        scene_name=scene_name,
        objects_of_interest=["red_coffee_mug_1", "white_yellow_mug_1"],
        goal_states=[
            ("upsidedown", "white_yellow_mug_1"),
            ("above", "white_yellow_mug_1", "red_coffee_mug_1"),
        ],
    )

    bddl, _ = generate_bddl_from_task_info()
    print(bddl)


if __name__ == "__main__":
    main()
