import re
import numpy as np
from libero.libero.envs import objects
from libero.libero.utils.bddl_generation_utils import *
from libero.libero.envs.objects import OBJECTS_DICT
from libero.libero.utils.object_utils import get_affordance_regions
from libero.libero.utils.mu_utils import register_mu, InitialSceneTemplates

# Import original study scenes
from .mu_creation import (
    StudyScene1, StudyScene2, StudyScene3, StudyScene4
)


# Study scenes extended to Kitchen
@register_mu(scene_type="kitchen")
class StudyScene1Kitchen(StudyScene1):
    def __init__(self):
        fixture_num_info = {
            "kitchen_table": 1,
            "desk_caddy": 1,
        }
        object_num_info = {
            "black_book": 1,
            "white_yellow_mug": 1,
        }
        super(StudyScene1, self).__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("study_table", "kitchen_table"))
            for state in original_states
        ]


@register_mu(scene_type="kitchen")
class StudyScene2Kitchen(StudyScene2):
    def __init__(self):
        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
        }
        object_num_info = {
            "black_book": 1,
            "red_coffee_mug": 1,
        }
        super(StudyScene2, self).__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("study_table", "kitchen_table"))
            for state in original_states
        ]


@register_mu(scene_type="kitchen")
class StudyScene3Kitchen(StudyScene3):
    def __init__(self):
        fixture_num_info = {
            "kitchen_table": 1,
            "desk_caddy": 1,
        }
        object_num_info = {
            "black_book": 1,
            "red_coffee_mug": 1,
            "porcelain_mug": 1,
        }
        super(StudyScene3, self).__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("study_table", "kitchen_table"))
            for state in original_states
        ]


@register_mu(scene_type="kitchen")
class StudyScene4Kitchen(StudyScene4):
    def __init__(self):
        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
        }
        object_num_info = {
            "black_book": 1,
            "yellow_book": 2,
        }
        super(StudyScene4, self).__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("study_table", "kitchen_table"))
            for state in original_states
        ]


# Study scenes extended to Living Room
@register_mu(scene_type="living_room")
class StudyScene1LivingRoom(StudyScene1):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
            "desk_caddy": 1,
        }
        object_num_info = {
            "black_book": 1,
            "white_yellow_mug": 1,
        }
        super(StudyScene1, self).__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("study_table", "living_room_table"))
            for state in original_states
        ]


@register_mu(scene_type="living_room")
class StudyScene2LivingRoom(StudyScene2):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
            "desk_caddy": 1,
        }
        object_num_info = {
            "black_book": 1,
            "red_coffee_mug": 1,
        }
        super(StudyScene2, self).__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("study_table", "living_room_table"))
            for state in original_states
        ]


@register_mu(scene_type="living_room")
class StudyScene3LivingRoom(StudyScene3):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
            "desk_caddy": 1,
        }
        object_num_info = {
            "black_book": 1,
            "red_coffee_mug": 1,
            "porcelain_mug": 1,
        }
        super(StudyScene3, self).__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("study_table", "living_room_table"))
            for state in original_states
        ]


@register_mu(scene_type="living_room")
class StudyScene4LivingRoom(StudyScene4):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
            "wooden_two_layer_shelf": 1,
        }
        object_num_info = {
            "black_book": 1,
            "yellow_book": 2,
        }
        super(StudyScene4, self).__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("study_table", "living_room_table"))
            for state in original_states
        ]


# Study scenes extended to Tabletop Manipulation
@register_mu(scene_type="tabletop_manipulation")
class StudyScene1Tabletop(StudyScene1):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
            "desk_caddy": 1,
        }
        object_num_info = {
            "black_book": 1,
            "white_yellow_mug": 1,
        }
        super(StudyScene1, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("study_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class StudyScene2Tabletop(StudyScene2):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
            "desk_caddy": 1,
        }
        object_num_info = {
            "black_book": 1,
            "red_coffee_mug": 1,
        }
        super(StudyScene2, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("study_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class StudyScene3Tabletop(StudyScene3):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
            "desk_caddy": 1,
        }
        object_num_info = {
            "black_book": 1,
            "red_coffee_mug": 1,
            "porcelain_mug": 1,
        }
        super(StudyScene3, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("study_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class StudyScene4Tabletop(StudyScene4):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
            "wooden_two_layer_shelf": 1,
        }
        object_num_info = {
            "black_book": 1,
            "yellow_book": 2,
        }
        super(StudyScene4, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("study_table", "main_table"))
            for state in original_states
        ]
