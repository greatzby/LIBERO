import re
import numpy as np
from libero.libero.envs import objects
from libero.libero.utils.bddl_generation_utils import *
from libero.libero.envs.objects import OBJECTS_DICT
from libero.libero.utils.object_utils import get_affordance_regions
from libero.libero.utils.mu_utils import register_mu, InitialSceneTemplates

# Import original tabletop manipulation scenes
from .mu_creation import TabletopScene1


# Tabletop Manipulation scenes extended to Kitchen
@register_mu(scene_type="kitchen")
class TabletopScene1Kitchen(TabletopScene1):
    def __init__(self):
        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_cabinet": 1,
            "flat_stove": 1,
            "wine_rack": 1,
        }
        object_num_info = {
            "akita_black_bowl": 1,
            "cream_cheese": 1,
            "wine_bottle": 1,
            "plate": 1,
        }
        super(TabletopScene1, self).__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("main_table", "kitchen_table"))
            for state in original_states
        ]


# Tabletop Manipulation scenes extended to Living Room
@register_mu(scene_type="living_room")
class TabletopScene1LivingRoom(TabletopScene1):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
            "wooden_cabinet": 1,
            "flat_stove": 1,
            "wine_rack": 1,
        }
        object_num_info = {
            "akita_black_bowl": 1,
            "cream_cheese": 1,
            "wine_bottle": 1,
            "plate": 1,
        }
        super(TabletopScene1, self).__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("main_table", "living_room_table"))
            for state in original_states
        ]


# Tabletop Manipulation scenes extended to Study
@register_mu(scene_type="study")
class TabletopScene1Study(TabletopScene1):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
            "wooden_cabinet": 1,
            "flat_stove": 1,
            "wine_rack": 1,
        }
        object_num_info = {
            "akita_black_bowl": 1,
            "cream_cheese": 1,
            "wine_bottle": 1,
            "plate": 1,
        }
        super(TabletopScene1, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("main_table", "study_table"))
            for state in original_states
        ]
