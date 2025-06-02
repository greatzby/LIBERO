from typing import List
import numpy as np
import robosuite.utils.transform_utils as transform_utils
from libero.libero.envs.object_states.base_object_states import BaseObjectState


class Expression:
    def __init__(self):
        raise NotImplementedError

    def __call__(self):
        raise NotImplementedError


class UnaryAtomic(Expression):
    def __init__(self):
        pass

    def __call__(self, arg1):
        raise NotImplementedError


class BinaryAtomic(Expression):
    def __init__(self):
        pass

    def __call__(self, arg1, arg2):
        raise NotImplementedError


class MultiarayAtomic(Expression):
    def __init__(self):
        pass

    def __call__(self, *args):
        raise NotImplementedError


class TruePredicateFn(MultiarayAtomic):
    def __init__(self):
        super().__init__()

    def __call__(self, *args):
        return True

    def expected_arg_types(self):
        return []


class FalsePredicateFn(MultiarayAtomic):
    def __init__(self):
        super().__init__()

    def __call__(self, *args):
        return False

    def expected_arg_types(self):
        return []


class Not(UnaryAtomic):
    def __call__(self, arg):
        return not arg

    def expected_arg_types(self):
        return [bool]


class And(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return arg1 and arg2

    def expected_arg_types(self):
        return [bool, bool]


class Or(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return arg1 or arg2

    def expected_arg_types(self):
        return [bool, bool]


class Any(UnaryAtomic):
    def __call__(self, arg):
        if not isinstance(arg, tuple):
            raise TypeError("Any expects a tuple of booleans")
        return any(arg)

    def expected_arg_types(self):
        return [tuple]


class All(UnaryAtomic):
    def __call__(self, arg):
        if not isinstance(arg, tuple):
            raise TypeError("All expects a list or tuple of booleans")
        return all(arg)

    def expected_arg_types(self):
        return [tuple]



class InContactPredicateFn(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return arg1.check_contact(arg2)

    def expected_arg_types(self):
        return [BaseObjectState, BaseObjectState]


class In(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return arg2.check_contact(arg1) and arg2.check_contain(arg1)

    def expected_arg_types(self):
        return [BaseObjectState, BaseObjectState]


class On(BinaryAtomic):
    """
    With 3cm center alignement constraint (original)
    """
    def __call__(self, arg1, arg2):
        return arg2.check_ontop(arg1)

    def expected_arg_types(self):
        return [BaseObjectState, BaseObjectState]

class RelaxedOn(BinaryAtomic):
    """
    Without center alignment constraint
    """
    def __call__(self, arg1, arg2):
        return arg2.check_ontop(arg1, threshold=float('inf'))

    def expected_arg_types(self):
        return [BaseObjectState, BaseObjectState]


class Under(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return arg1.get_geom_state()["pos"][2] <= arg2.get_geom_state()["pos"][2]

    def expected_arg_types(self):
        return [BaseObjectState, BaseObjectState]


class Up(UnaryAtomic):
    def __call__(self, arg1):
        return arg1.get_geom_state()["pos"][2] >= 1.0

    def expected_arg_types(self):
        return [BaseObjectState]


class UpsideDown(UnaryAtomic):
    def __call__(self, arg):
        geom = arg.get_geom_state()
        w, x, y, z = geom["quat"]
        q_curr = np.array([x, y, z, w])
        R_curr = transform_utils.quat2mat(q_curr)
        z_curr = R_curr[:, 2]
        return z_curr[2] < -0.95

    def expected_arg_types(self):
        return [BaseObjectState]


class Upright(UnaryAtomic):
    def __call__(self, arg):
        geom = arg.get_geom_state()
        w, x, y, z = geom["quat"]
        quat_for_rs = np.array([x, y, z, w])
        R = transform_utils.quat2mat(quat_for_rs)
        z_axis_world = R[:, 2]
        return z_axis_world[2] >= 0.9

    def expected_arg_types(self):
        return [BaseObjectState]


class AxisAlignedWithin(UnaryAtomic):
    def __call__(self, *args):
        if len(args) != 4:
            raise ValueError("Upright expects 4 arguments: object, axis ('x', 'y', 'z'), min_degree, max_degree")
        obj, axis, min_deg, max_deg = args
        if axis not in {"x", "y", "z"}:
            raise ValueError("Axis must be one of 'x', 'y', or 'z'")
        if not (0 <= min_deg <= max_deg <= 180):
            raise ValueError("Degrees must satisfy 0 <= min_deg <= max_deg <= 180")

        min_rad = np.radians(min_deg)
        max_rad = np.radians(max_deg)
        cos_min = np.cos(min_rad)
        cos_max = np.cos(max_rad)

        geom = obj.get_geom_state()
        w, x, y, z = geom["quat"]
        quat_for_rs = np.array([x, y, z, w])
        R = transform_utils.quat2mat(quat_for_rs)

        axis_index = {"x": 0, "y": 1, "z": 2}[axis]
        object_axis_world = R[:, axis_index]
        cos_angle = object_axis_world[2]

        return cos_max <= cos_angle <= cos_min

    def expected_arg_types(self):
        return [BaseObjectState, str, float, float]


class Stack(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return (
            arg1.check_contact(arg2)
            and arg2.check_contain(arg1)
            and arg1.get_geom_state()["pos"][2] > arg2.get_geom_state()["pos"][2]
        )

    def expected_arg_types(self):
        return [BaseObjectState, BaseObjectState]


class StackBowl(BinaryAtomic):
    def __call__(self, arg1, arg2):
        pos1 = arg1.get_geom_state()["pos"]
        pos2 = arg2.get_geom_state()["pos"]

        xy_threshold = 0.02
        z_min_gap = 0.001
        z_max_gap = 0.5

        horizontally_aligned = (
            abs(pos1[0] - pos2[0]) < xy_threshold and
            abs(pos1[1] - pos2[1]) < xy_threshold
        )

        vertical_stack = (
            z_min_gap < abs(pos1[2] - pos2[2]) < z_max_gap
        )

        return (
            arg1.check_contact(arg2)
            and horizontally_aligned
            and vertical_stack
        )

    def expected_arg_types(self):
        return [BaseObjectState, BaseObjectState]


class PrintJointState(UnaryAtomic):
    def __call__(self, arg):
        print(arg.get_joint_state())
        return True

    def expected_arg_types(self):
        return [BaseObjectState]


class Open(UnaryAtomic):
    def __call__(self, arg):
        return arg.is_open()

    def expected_arg_types(self):
        return [BaseObjectState]


class Close(UnaryAtomic):
    def __call__(self, arg):
        return arg.is_close()

    def expected_arg_types(self):
        return [BaseObjectState]

class OpenRatio(UnaryAtomic):
    def __call__(self, arg, exp_ratio):
        tol = 0.2
        if abs(arg.open_ratio() - float(exp_ratio)) < tol:
            return True
        else:
            return False
    
    def expected_arg_types(self):
        return [BaseObjectState, float]


class TurnOn(UnaryAtomic):
    def __call__(self, arg):
        return arg.turn_on()

    def expected_arg_types(self):
        return [BaseObjectState]


class TurnOff(UnaryAtomic):
    def __call__(self, arg):
        return arg.turn_off()

    def expected_arg_types(self):
        return [BaseObjectState]

