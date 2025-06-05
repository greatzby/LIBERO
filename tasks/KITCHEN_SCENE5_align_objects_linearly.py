# filepath: /media/arca/ArcaEXT4/_codes/ResearchProjects/cua-vla-robotics/libero_project/LIBERO/tasks/KITCHEN_SCENE5_align_objects_linearly.py
from libero.libero.benchmark.mu_creation import KitchenScene5
from libero.libero.utils.task_generation_utils import (
    generate_bddl_from_task_info,
    register_task_info,
)


def main():
    register_task_info(
        language="Align the plate, bowl, and ketchup bottle linearly with the plate leftmost and bowl rightmost",
        scene_name="kitchen_scene5",
        objects_of_interest=["plate_1", "ketchup_1", "akita_black_bowl_1"],
        goal_states=[
            ("linear", "plate_1", "ketchup_1", "akita_black_bowl_1", 0.005),
        ],
    )
    bddl, _ = generate_bddl_from_task_info()
    print(bddl)


if __name__ == "__main__":
    main()
