import re
import numpy as np
from libero.libero.envs import objects
from libero.libero.utils.bddl_generation_utils import *
from libero.libero.envs.objects import OBJECTS_DICT
from libero.libero.utils.object_utils import get_affordance_regions
from libero.libero.utils.mu_utils import register_mu, InitialSceneTemplates

# Import original kitchen scenes
from .mu_creation import (
    KitchenScene1, KitchenScene2, KitchenScene3, KitchenScene4, KitchenScene5,
    KitchenScene6, KitchenScene7, KitchenScene8, KitchenScene9, KitchenScene10
)


# Kitchen scenes extended to Living Room
@register_mu(scene_type="living_room")
class KitchenScene1LivingRoom(KitchenScene1):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "plate": 1,
        }

        super(KitchenScene1, self).__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "living_room_table"))
            for state in original_states
        ]


@register_mu(scene_type="living_room")
class KitchenScene2LivingRoom(KitchenScene2):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "akita_black_bowl": 3,
            "plate": 1,
        }

        super(KitchenScene2, self).__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "living_room_table"))
            for state in original_states
        ]


@register_mu(scene_type="living_room")
class KitchenScene3LivingRoom(KitchenScene3):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
            "moka_pot": 1,
        }

        super(KitchenScene3, self).__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "living_room_table"))
            for state in original_states
        ]


@register_mu(scene_type="living_room")
class KitchenScene4LivingRoom(KitchenScene4):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
            "white_cabinet": 1,
            "wine_rack": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "wine_bottle": 1,
        }

        super(KitchenScene4, self).__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "living_room_table"))
            for state in original_states
        ]


@register_mu(scene_type="living_room")
class KitchenScene5LivingRoom(KitchenScene5):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
            "white_cabinet": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "plate": 1,
            "ketchup": 1,
        }

        super(KitchenScene5, self).__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "living_room_table"))
            for state in original_states
        ]


@register_mu(scene_type="living_room")
class KitchenScene6LivingRoom(KitchenScene6):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
            "microwave": 1,
        }

        object_num_info = {
            "porcelain_mug": 1,
            "white_yellow_mug": 1,
        }

        super(KitchenScene6, self).__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "living_room_table"))
            for state in original_states
        ]


@register_mu(scene_type="living_room")
class KitchenScene7LivingRoom(KitchenScene7):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
            "microwave": 1,
        }

        object_num_info = {
            "white_bowl": 1,
            "plate": 1,
        }

        super(KitchenScene7, self).__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "living_room_table"))
            for state in original_states
        ]


@register_mu(scene_type="living_room")
class KitchenScene8LivingRoom(KitchenScene8):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "moka_pot": 2,
        }

        super(KitchenScene8, self).__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "living_room_table"))
            for state in original_states
        ]


@register_mu(scene_type="living_room")
class KitchenScene9LivingRoom(KitchenScene9):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
            "flat_stove": 1,
            "wooden_two_layer_shelf": 1,
        }

        object_num_info = {
            "white_bowl": 1,
            "chefmate_8_frypan": 1,
        }

        super(KitchenScene9, self).__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "living_room_table"))
            for state in original_states
        ]


@register_mu(scene_type="living_room")
class KitchenScene10LivingRoom(KitchenScene10):
    def __init__(self):
        fixture_num_info = {
            "living_room_table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "butter": 2,
            "chocolate_pudding": 1,
        }

        super(KitchenScene10, self).__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "living_room_table"))
            for state in original_states
        ]


# Kitchen scenes extended to Study
@register_mu(scene_type="study")
class KitchenScene1Study(KitchenScene1):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "plate": 1,
        }

        super(KitchenScene1, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "study_table"))
            for state in original_states
        ]


@register_mu(scene_type="study")
class KitchenScene2Study(KitchenScene2):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "akita_black_bowl": 3,
            "plate": 1,
        }

        super(KitchenScene2, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "study_table"))
            for state in original_states
        ]


@register_mu(scene_type="study")
class KitchenScene3Study(KitchenScene3):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
            "moka_pot": 1,
        }

        super(KitchenScene3, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "study_table"))
            for state in original_states
        ]


@register_mu(scene_type="study")
class KitchenScene4Study(KitchenScene4):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
            "white_cabinet": 1,
            "wine_rack": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "wine_bottle": 1,
        }

        super(KitchenScene4, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "study_table"))
            for state in original_states
        ]


@register_mu(scene_type="study")
class KitchenScene5Study(KitchenScene5):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
            "white_cabinet": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "plate": 1,
            "ketchup": 1,
        }

        super(KitchenScene5, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "study_table"))
            for state in original_states
        ]


@register_mu(scene_type="study")
class KitchenScene6Study(KitchenScene6):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
            "microwave": 1,
        }

        object_num_info = {
            "porcelain_mug": 1,
            "white_yellow_mug": 1,
        }

        super(KitchenScene6, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "study_table"))
            for state in original_states
        ]


@register_mu(scene_type="study")
class KitchenScene7Study(KitchenScene7):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
            "microwave": 1,
        }

        object_num_info = {
            "white_bowl": 1,
            "plate": 1,
        }

        super(KitchenScene7, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "study_table"))
            for state in original_states
        ]


@register_mu(scene_type="study")
class KitchenScene8Study(KitchenScene8):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "moka_pot": 2,
        }

        super(KitchenScene8, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "study_table"))
            for state in original_states
        ]


@register_mu(scene_type="study")
class KitchenScene9Study(KitchenScene9):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
            "flat_stove": 1,
            "wooden_two_layer_shelf": 1,
        }

        object_num_info = {
            "white_bowl": 1,
            "chefmate_8_frypan": 1,
        }

        super(KitchenScene9, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "study_table"))
            for state in original_states
        ]


@register_mu(scene_type="study")
class KitchenScene10Study(KitchenScene10):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "butter": 2,
            "chocolate_pudding": 1,
        }

        super(KitchenScene10, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "study_table"))
            for state in original_states
        ]


# Kitchen scenes extended to Tabletop Manipulation
@register_mu(scene_type="tabletop_manipulation")
class KitchenScene1TabletopManipulation(KitchenScene1):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "plate": 1,
        }

        super(KitchenScene1, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class KitchenScene2TabletopManipulation(KitchenScene2):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "akita_black_bowl": 3,
            "plate": 1,
        }

        super(KitchenScene2, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class KitchenScene3TabletopManipulation(KitchenScene3):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
            "moka_pot": 1,
        }

        super(KitchenScene3, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class KitchenScene4TabletopManipulation(KitchenScene4):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
            "white_cabinet": 1,
            "wine_rack": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "wine_bottle": 1,
        }

        super(KitchenScene4, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class KitchenScene5TabletopManipulation(KitchenScene5):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
            "white_cabinet": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "plate": 1,
            "ketchup": 1,
        }

        super(KitchenScene5, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class KitchenScene6TabletopManipulation(KitchenScene6):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
            "microwave": 1,
        }

        object_num_info = {
            "porcelain_mug": 1,
            "white_yellow_mug": 1,
        }

        super(KitchenScene6, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class KitchenScene7TabletopManipulation(KitchenScene7):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
            "microwave": 1,
        }

        object_num_info = {
            "white_bowl": 1,
            "plate": 1,
        }

        super(KitchenScene7, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class KitchenScene8TabletopManipulation(KitchenScene8):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "moka_pot": 2,
        }

        super(KitchenScene8, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class KitchenScene9TabletopManipulation(KitchenScene9):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
            "flat_stove": 1,
            "wooden_two_layer_shelf": 1,
        }

        object_num_info = {
            "white_bowl": 1,
            "chefmate_8_frypan": 1,
        }

        super(KitchenScene9, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class KitchenScene10TabletopManipulation(KitchenScene10):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "butter": 2,
            "chocolate_pudding": 1,
        }

        super(KitchenScene10, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("kitchen_table", "main_table"))
            for state in original_states
        ]
