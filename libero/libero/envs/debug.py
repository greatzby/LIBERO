import numpy as np
import robosuite.utils.transform_utils as transform_utils
import os

DEBUG = os.getenv("LIBERO_DEBUG", "0") in ["1", "true", "True", "TRUE"]
ROTATION_MODE = os.getenv("LIBERO_ROTATION_MODE", "vector").lower()  # "euler" or "vector"

def print_states(goal_state, results, object_states_dict, debug_time):
    if not DEBUG:
        return

    if debug_time % 100 != 0:
        return
    
    if debug_time == 0:
        print("\033c", end='')

    print("\033[?25l", end='')
    num_lines = len(goal_state) + 4 + len(object_states_dict) + 4 + 3

    for _ in range(num_lines):
        print("\033[A", end='')
    
    print("Detect time:", debug_time)
    predicate_str_len = 60
    print("┌" + "─" * predicate_str_len + "┬" + "─" * 50 + "┐")
    print("│" + " predicate".ljust(predicate_str_len) + "│" + " result".ljust(50) + "│")
    print("├" + "─" * predicate_str_len + "┼" + "─" * 50 + "┤")
    
    for i, (state, result) in enumerate(zip(goal_state, results)):
        state_str = str(state)
        if len(state_str) > predicate_str_len:
            state_str = state_str[:predicate_str_len-3] + "..."
        result_str = str(result)
        print("│" + state_str.ljust(predicate_str_len) +"│" + result_str.ljust(50) + "│")
        
    print("└" + "─" * predicate_str_len + "┴" + "─" * 50 + "┘")

    # print the object states
    object_name_str_len = 30
    object_posi_str_len = 50
    
    if ROTATION_MODE == "euler":
        object_rotation_str_len = 35
        rotation_header = "roll, pitch, yaw"
    else:  # vector mode (default)
        object_rotation_str_len = 45
        header1, header2, header3 = "rotation_x", "rotation_y", "rotation_z"
    
    print("Object states:"+" "* (object_name_str_len + object_posi_str_len + object_rotation_str_len - 15))
    
    if ROTATION_MODE == "euler":
        print("┌" + "─" * object_name_str_len + "┬" + "─" * object_posi_str_len + "┬" + "─" * object_rotation_str_len + "┐")
        print("│" + " object".ljust(object_name_str_len) + "│" + " posi".ljust(object_posi_str_len) + "│" + f" {rotation_header}".ljust(object_rotation_str_len) + "│")
        print("├" + "─" * object_name_str_len + "┼" + "─" * object_posi_str_len + "┼" + "─" * object_rotation_str_len + "┤")
    else:
        print("┌" + "─" * object_name_str_len + "┬" + "─" * object_posi_str_len + "┬" + "─" * object_rotation_str_len + "┬" * object_rotation_str_len + "┬" * object_rotation_str_len + "┐")
        print("│" + " object".ljust(object_name_str_len) + "│" + " posi".ljust(object_posi_str_len) + "│" + f" {header1}".ljust(object_rotation_str_len) + "│" + f"{header2}".ljust(object_rotation_str_len) + "│" + f"{header3}".ljust(object_rotation_str_len) + "│")
        print("├" + "─" * object_name_str_len + "┼" + "─" * object_posi_str_len + "┼" + "─" * object_rotation_str_len + "┼" * object_rotation_str_len + "┼" * object_rotation_str_len + "┤")
    for object_name, object in object_states_dict.items():
        object_name_str = str(object_name)
        if len(object_name_str) > object_name_str_len:
            object_name_str = object_name_str[:object_name_str_len-3] + "..."
        geom = object.get_geom_state()
        object_state_str = str(geom["pos"])
        if len(object_state_str) > object_posi_str_len:
            object_state_str = object_state_str[:object_posi_str_len-3] + "..."
        w, x, y, z = geom["quat"]
        q_curr = np.array([x, y, z, w])
        R_curr = transform_utils.quat2mat(q_curr)
        
        if ROTATION_MODE == "euler":
            # Euler angle mode - show roll, pitch, yaw in single column
            roll, pitch, yaw = transform_utils.mat2euler(R_curr)
            # Convert to degrees and format with 2 decimal places
            roll_deg = np.degrees(roll)
            pitch_deg = np.degrees(pitch)
            yaw_deg = np.degrees(yaw)
            euler_str = f"({roll_deg:.2f}°, {pitch_deg:.2f}°, {yaw_deg:.2f}°)"
            
            if len(euler_str) > object_rotation_str_len:
                euler_str = euler_str[:object_rotation_str_len-3] + "..."
            
            print("│" + object_name_str.ljust(object_name_str_len) + "│" + object_state_str.ljust(object_posi_str_len) + "│" + euler_str.ljust(object_rotation_str_len) + "│")
        else:
            # Rotation vector mode (default) - show rotation matrix components
            rotation_x_str = str([f"{val:.3e}" for val in R_curr[0]])
            rotation_y_str = str([f"{val:.3e}" for val in R_curr[1]])
            rotation_z_str = str([f"{val:.3e}" for val in R_curr[2]])
            
            if len(rotation_x_str) > object_rotation_str_len:
                rotation_x_str = rotation_x_str[:object_rotation_str_len-3] + "..."
            if len(rotation_y_str) > object_rotation_str_len:
                rotation_y_str = rotation_y_str[:object_rotation_str_len-3] + "..."
            if len(rotation_z_str) > object_rotation_str_len:
                rotation_z_str = rotation_z_str[:object_rotation_str_len-3] + "..."
            
            print("│" + object_name_str.ljust(object_name_str_len) + "│" + object_state_str.ljust(object_posi_str_len) + "│" + rotation_x_str.ljust(object_rotation_str_len) + "│" + rotation_y_str.ljust(object_rotation_str_len) + "│" + rotation_z_str.ljust(object_rotation_str_len) + "│")
    
    if ROTATION_MODE == "euler":
        print("└" + "─" * object_name_str_len + "┴" + "─" * object_posi_str_len + "┴" + "─" * object_rotation_str_len + "┘")
    else:
        print("└" + "─" * object_name_str_len + "┴" + "─" * object_posi_str_len + "┴" + "─" * object_rotation_str_len + "┴" + "─" * object_rotation_str_len + "┴" + "─" * object_rotation_str_len + "┘")
    
    # Restore cursor visibility
    print("\033[?25h", end='')
