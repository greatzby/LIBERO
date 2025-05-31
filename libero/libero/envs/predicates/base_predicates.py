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
        z_curr = R_curr[:, 2]      # current up-axis in world coords
        
        return z_curr[2] < -0.95

# works only for objects with initial rotation {x: pi/2, z: pi/2}
# y-axis Upright
class Upright(UnaryAtomic):

    def __call__(self, arg):
        geom = arg.get_geom_state()
        w, x, y, z = geom["quat"]              # MuJoCo: [w, x, y, z]
        quat_for_rs = np.array([x, y, z, w])   # transform_utils: [x, y, z, w]

        R = transform_utils.quat2mat(quat_for_rs)
        z_axis_world = R[:, 1]
        return z_axis_world[2] >= 0.95


class Stack(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return (
            arg1.check_contact(arg2)
            and arg2.check_contain(arg1)
            and arg1.get_geom_state()["pos"][2] > arg2.get_geom_state()["pos"][2]
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


class UpRight45(UnaryAtomic):
    """Check if the object is upright within 45 degrees"""
    def __call__(self, arg):
        geom = arg.get_geom_state()
        w, x, y, z = geom["quat"]
        quat_for_rs = np.array([x, y, z, w])

        R = transform_utils.quat2mat(quat_for_rs)
        z_axis = R[:, 2]
        return z_axis[2] >= 0.7071