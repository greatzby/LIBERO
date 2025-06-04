from libero.libero.benchmark.mu_creation import KitchenScene5
from libero.libero.utils.task_generation_utils import (
    generate_bddl_from_task_info,
    register_task_info,
)


def main():
    register_task_info(
        language="Place the ketchup bottle diagonally across the top drawer and close it",
        scene_name="kitchen_scene5",
        objects_of_interest=["ketchup_1", "white_cabinet_1"],
        goal_states=[
            ("In", "ketchup_1", "white_cabinet_1_top_region"),
            ("AxisAlignedWithin", "ketchup_1", "x", 60, 120),
            ("AxisAlignedWithin", "ketchup_1", "y", 60, 120),
            ("Close", "white_cabinet_1_top_region"),
        ],
    )
    bddl, _ = generate_bddl_from_task_info()
    print(bddl)


if __name__ == "__main__":
    main()
