from typing import List
import numpy as np
import robosuite.utils.transform_utils as transform_utils



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


class FalsePredicateFn(MultiarayAtomic):
    def __init__(self):
        super().__init__()

    def __call__(self, *args):
        return False


class InContactPredicateFn(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return arg1.check_contact(arg2)


class In(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return arg2.check_contact(arg1) and arg2.check_contain(arg1)


class On(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return arg2.check_ontop(arg1)

        # if arg2.object_state_type == "site":
        #     return arg2.check_ontop(arg1)
        # else:
        #     obj_1_pos = arg1.get_geom_state()["pos"]
        #     obj_2_pos = arg2.get_geom_state()["pos"]
        #     # arg1.on_top_of(arg2) ?
        #     # TODO (Yfeng): Add checking of center of mass are in the same regions
        #     if obj_1_pos[2] >= obj_2_pos[2] and arg2.check_contact(arg1):
        #         return True
        #     else:
        #         return False

class Under(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return arg1.get_geom_state()["pos"][2] <= arg2.get_geom_state()["pos"][2]


class Up(BinaryAtomic):
    def __call__(self, arg1):
        return arg1.get_geom_state()["pos"][2] >= 1.0
    
class UpsideDown(UnaryAtomic):
    def __call__(self, arg):
        geom = arg.get_geom_state()
        w, x, y, z = geom["quat"]
        q_curr = np.array([x, y, z, w])
        R_curr = transform_utils.quat2mat(q_curr)
        z_curr = R_curr[:, 2]                  # current up-axis in world coords
        
        return z_curr[2] < -0.95

class Upright(UnaryAtomic): 
    """Check if the object is upright with respect to the z-axis."""
    """If this predicate fails, check the initial rotation of the object and use AxisAlignedWithin instead"""
    def __call__(self, arg):
        geom = arg.get_geom_state()
        w, x, y, z = geom["quat"]              # MuJoCo: [w, x, y, z]
        quat_for_rs = np.array([x, y, z, w])   # transform_utils: [x, y, z, w]

        R = transform_utils.quat2mat(quat_for_rs)
        z_axis_world = R[:, 2]
        return z_axis_world[2] >= 0.9

class AxisAlignedWithin(UnaryAtomic):
    """
    Check if the object's specified axis is within a degree range [min_deg, max_deg]
    from alignment with the world Z+ axis.
    
    Usage: Upright()(object, axis, min_deg, max_deg)
    """
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

        # print(cos_min, cos_max)

        geom = obj.get_geom_state()
        w, x, y, z = geom["quat"]
        quat_for_rs = np.array([x, y, z, w])  # Convert to [x, y, z, w] for robosuite
        R = transform_utils.quat2mat(quat_for_rs)

        axis_index = {"x": 0, "y": 1, "z": 2}[axis]
        object_axis_world = R[:, axis_index]
        cos_angle = object_axis_world[2]

        return cos_max <= cos_angle <= cos_min



class Stack(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return (
            arg1.check_contact(arg2)
            and arg2.check_contain(arg1)
            and arg1.get_geom_state()["pos"][2] > arg2.get_geom_state()["pos"][2]
        )

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
        # print([abs(pos1[0] - pos2[0]),abs(pos1[1] - pos2[1]),(pos1[2] - pos2[2])])
        return (
            arg1.check_contact(arg2)
            and horizontally_aligned
            and vertical_stack
        )

class PrintJointState(UnaryAtomic):
    """This is a debug predicate to allow you print the joint values of the object you care"""

    def __call__(self, arg):
        print(arg.get_joint_state())
        return True


class Open(UnaryAtomic):
    def __call__(self, arg):
        return arg.is_open()


class Close(UnaryAtomic):
    def __call__(self, arg):
        return arg.is_close()


class TurnOn(UnaryAtomic):
    def __call__(self, arg):
        return arg.turn_on()


class TurnOff(UnaryAtomic):
    def __call__(self, arg):
        return arg.turn_off()


# class UpRight45(UnaryAtomic):
#     """Check if the object is upright within 45 degrees"""
#     def __call__(self, arg):
#         geom = arg.get_geom_state()
#         w, x, y, z = geom["quat"]
#         quat_for_rs = np.array([x, y, z, w])

#         R = transform_utils.quat2mat(quat_for_rs)
#         z_axis = R[:, 2]
#         return z_axis[2] >= 0.7071