import re
import numpy as np
from libero.libero.envs import objects
from libero.libero.utils.bddl_generation_utils import *
from libero.libero.envs.objects import OBJECTS_DICT
from libero.libero.utils.object_utils import get_affordance_regions
from libero.libero.utils.mu_utils import register_mu, InitialSceneTemplates

# Import original living room scenes
from .mu_creation import (
    LivingRoomScene1, LivingRoomScene2, LivingRoomScene3, LivingRoomScene4,
    LivingRoomScene5, LivingRoomScene6
)


# Living room scenes extended to Kitchen
@register_mu(scene_type="kitchen")
class LivingRoomScene1Kitchen(LivingRoomScene1):
    def __init__(self):
        fixture_num_info = {
            "kitchen_table": 1,
        }
        object_num_info = {
            "alphabet_soup": 1,
            "cream_cheese": 1,
            "tomato_sauce": 1,
            "ketchup": 1,
            "basket": 1,
        }
        super(LivingRoomScene1, self).__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "kitchen_table"))
            for state in original_states
        ]


@register_mu(scene_type="kitchen")
class LivingRoomScene2Kitchen(LivingRoomScene2):
    def __init__(self):
        fixture_num_info = {
            "kitchen_table": 1,
        }
        object_num_info = {
            "alphabet_soup": 1,
            "cream_cheese": 1,
            "tomato_sauce": 1,
            "ketchup": 1,
            "orange_juice": 1,
            "milk": 1,
            "butter": 1,
            "basket": 1,
        }
        super(LivingRoomScene2, self).__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "kitchen_table"))
            for state in original_states
        ]


@register_mu(scene_type="kitchen")
class LivingRoomScene3Kitchen(LivingRoomScene3):
    def __init__(self):
        fixture_num_info = {
            "kitchen_table": 1,
        }
        object_num_info = {
            "alphabet_soup": 1,
            "cream_cheese": 1,
            "tomato_sauce": 1,
            "ketchup": 1,
            "butter": 1,
            "wooden_tray": 1,
        }
        super(LivingRoomScene3, self).__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "kitchen_table"))
            for state in original_states
        ]


@register_mu(scene_type="kitchen")
class LivingRoomScene4Kitchen(LivingRoomScene4):
    def __init__(self):
        fixture_num_info = {
            "kitchen_table": 1,
        }

        object_num_info = {
            "akita_black_bowl": 2,
            "new_salad_dressing": 1,
            "chocolate_pudding": 1,
            "wooden_tray": 1,
        }

        super(LivingRoomScene4, self).__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "kitchen_table"))
            for state in original_states
        ]


@register_mu(scene_type="kitchen")
class LivingRoomScene5Kitchen(LivingRoomScene5):
    def __init__(self):
        fixture_num_info = {
            "kitchen_table": 1,
        }

        object_num_info = {
            "porcelain_mug": 1,
            "red_coffee_mug": 1,
            "white_yellow_mug": 1,
            "plate": 2,
        }

        super(LivingRoomScene5, self).__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "kitchen_table"))
            for state in original_states
        ]


@register_mu(scene_type="kitchen")
class LivingRoomScene6Kitchen(LivingRoomScene6):
    def __init__(self):
        fixture_num_info = {
            "kitchen_table": 1,
        }

        object_num_info = {
            "porcelain_mug": 1,
            "red_coffee_mug": 1,
            "plate": 1,
            "chocolate_pudding": 1,
        }

        super(LivingRoomScene6, self).__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "kitchen_table"))
            for state in original_states
        ]


# Living room scenes extended to Study
@register_mu(scene_type="study")
class LivingRoomScene1Study(LivingRoomScene1):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
        }
        object_num_info = {
            "alphabet_soup": 1,
            "cream_cheese": 1,
            "tomato_sauce": 1,
            "ketchup": 1,
            "basket": 1,
        }
        super(LivingRoomScene1, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "study_table"))
            for state in original_states
        ]


@register_mu(scene_type="study")
class LivingRoomScene2Study(LivingRoomScene2):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
        }
        object_num_info = {
            "alphabet_soup": 1,
            "cream_cheese": 1,
            "tomato_sauce": 1,
            "ketchup": 1,
            "orange_juice": 1,
            "milk": 1,
            "butter": 1,
            "basket": 1,
        }
        super(LivingRoomScene2, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "study_table"))
            for state in original_states
        ]


@register_mu(scene_type="study")
class LivingRoomScene3Study(LivingRoomScene3):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
        }

        object_num_info = {
            "alphabet_soup": 1,
            "cream_cheese": 1,
            "tomato_sauce": 1,
            "ketchup": 1,
            "butter": 1,
            "wooden_tray": 1,
        }

        super(LivingRoomScene3, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "study_table"))
            for state in original_states
        ]


@register_mu(scene_type="study")
class LivingRoomScene4Study(LivingRoomScene4):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
        }

        object_num_info = {
            "akita_black_bowl": 2,
            "new_salad_dressing": 1,
            "chocolate_pudding": 1,
            "wooden_tray": 1,
        }

        super(LivingRoomScene4, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "study_table"))
            for state in original_states
        ]


@register_mu(scene_type="study")
class LivingRoomScene5Study(LivingRoomScene5):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
        }

        object_num_info = {
            "porcelain_mug": 1,
            "red_coffee_mug": 1,
            "white_yellow_mug": 1,
            "plate": 2,
        }

        super(LivingRoomScene5, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "study_table"))
            for state in original_states
        ]


@register_mu(scene_type="study")
class LivingRoomScene6Study(LivingRoomScene6):
    def __init__(self):
        fixture_num_info = {
            "study_table": 1,
        }

        object_num_info = {
            "porcelain_mug": 1,
            "red_coffee_mug": 1,
            "plate": 1,
            "chocolate_pudding": 1,
        }

        super(LivingRoomScene6, self).__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "study_table"))
            for state in original_states
        ]


# Living room scenes extended to Tabletop Manipulation
@register_mu(scene_type="tabletop_manipulation")
class LivingRoomScene1TabletopManipulation(LivingRoomScene1):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
        }
        object_num_info = {
            "alphabet_soup": 1,
            "cream_cheese": 1,
            "tomato_sauce": 1,
            "ketchup": 1,
            "basket": 1,
        }
        super(LivingRoomScene1, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class LivingRoomScene2TabletopManipulation(LivingRoomScene2):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
        }

        object_num_info = {
            "alphabet_soup": 1,
            "cream_cheese": 1,
            "tomato_sauce": 1,
            "ketchup": 1,
            "orange_juice": 1,
            "milk": 1,
            "butter": 1,
            "basket": 1,
        }

        super(LivingRoomScene2, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class LivingRoomScene3TabletopManipulation(LivingRoomScene3):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
        }

        object_num_info = {
            "alphabet_soup": 1,
            "cream_cheese": 1,
            "tomato_sauce": 1,
            "ketchup": 1,
            "butter": 1,
            "wooden_tray": 1,
        }

        super(LivingRoomScene3, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class LivingRoomScene4TabletopManipulation(LivingRoomScene4):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
        }

        object_num_info = {
            "akita_black_bowl": 2,
            "new_salad_dressing": 1,
            "chocolate_pudding": 1,
            "wooden_tray": 1,
        }

        super(LivingRoomScene4, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class LivingRoomScene5TabletopManipulation(LivingRoomScene5):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
        }

        object_num_info = {
            "porcelain_mug": 1,
            "red_coffee_mug": 1,
            "white_yellow_mug": 1,
            "plate": 2,
        }

        super(LivingRoomScene5, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "main_table"))
            for state in original_states
        ]


@register_mu(scene_type="tabletop_manipulation")
class LivingRoomScene6TabletopManipulation(LivingRoomScene6):
    def __init__(self):
        fixture_num_info = {
            "table": 1,
        }

        object_num_info = {
            "porcelain_mug": 1,
            "red_coffee_mug": 1,
            "plate": 1,
            "chocolate_pudding": 1,
        }

        super(LivingRoomScene6, self).__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    @property
    def init_states(self):
        original_states = super().init_states
        return [
            (state[0], state[1], state[2].replace("living_room_table", "main_table"))
            for state in original_states
        ]
