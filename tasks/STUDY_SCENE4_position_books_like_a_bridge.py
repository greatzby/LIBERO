from libero.libero.utils.bddl_generation_utils import (
    get_xy_region_kwargs_list_from_regions_info,
)
from libero.libero.utils.mu_utils import register_mu, InitialSceneTemplates
from libero.libero.utils.task_generation_utils import (
    generate_bddl_from_task_info,
    register_task_info,
)


@register_mu("study")
class StudyScene4(InitialSceneTemplates):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
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
                region_name="yellow_book_right_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.05],
                region_name="yellow_book_left_init_region",
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
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "yellow_book_1", "study_table_yellow_book_right_init_region"),
            ("On", "yellow_book_2", "study_table_yellow_book_left_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
        ]


def main():
    register_task_info(
        language="Position the black book horizontally so it bridges across the tops of the two upright yellow book",
        scene_name="study_scene4",
        objects_of_interest=["black_book_1", "yellow_book_1", "yellow_book_2"],
        goal_states=[
            ("relaxedon", "black_book_1", "yellow_book_1"),
            ("relaxedon", "black_book_1", "yellow_book_2"),
            ("axisalignedwithin", "black_book_1", "z", 85, 95),
            ("linear", "yellow_book_2", "black_book_1", "yellow_book_1", 0.0005), # small tolerance due to close objects.
            ("upright", "yellow_book_1"),
            ("upright", "yellow_book_2"),
        ],
    )
    bddl, _ = generate_bddl_from_task_info()
    print(bddl)


if __name__ == "__main__":
    main()
