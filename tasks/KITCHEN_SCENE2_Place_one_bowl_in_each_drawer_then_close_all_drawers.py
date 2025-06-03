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

import itertools

def main():

    scene_name = "kitchen_scene2"
    language = "Place one bowl in each drawer then close all drawers"

    bowls = ["akita_black_bowl_1", "akita_black_bowl_2", "akita_black_bowl_3"]
    regions = ["wooden_cabinet_1_top_region", "wooden_cabinet_1_middle_region", "wooden_cabinet_1_bottom_region"]
    
    def nest_and(predicates):
        """Nest ANDs pairwise, right-associative."""
        if len(predicates) == 1:
            return predicates[0]
        else:
            return ("And", predicates[0], nest_and(predicates[1:]))

    def nest_or(exprs):
        """Nest ORs pairwise, right-associative."""
        if len(exprs) == 1:
            return exprs[0]
        else:
            return ("Or", exprs[0], nest_or(exprs[1:]))

    def make_permutation_on_goals(bowls, regions):
        perms = list(itertools.permutations(bowls))
        and_clauses = []
        for perm in perms:
            and_clauses.append(
                nest_and([
                    ("In", bowl, region)
                    for bowl, region in zip(perm, regions)
                ])
            )
        return nest_or(and_clauses)

    goal_state_expr = make_permutation_on_goals(bowls, regions)
    goal_states = [goal_state_expr]
    goal_states.extend([
        ("Upright", "akita_black_bowl_1"),
        ("Upright", "akita_black_bowl_2"),
        ("Upright", "akita_black_bowl_3"),
        ("Close", "wooden_cabinet_1_top_region"),
        ("Close", "wooden_cabinet_1_middle_region"),
        ("Close", "wooden_cabinet_1_bottom_region"),
    ])

    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["akita_black_bowl_1", "akita_black_bowl_2", "akita_black_bowl_3", "wooden_cabinet_1"],
        goal_states=goal_states
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)

if __name__ == "__main__":
    main()
