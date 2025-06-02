## Introduction
LIBERO provides over 100 task examples, an intuitive teleoperation interface, and a clear, easy-to-follow task‐generation pipeline. However, its modular design and encapsulated logic make it essential to explore the source code yourself once you begin annotating.

Before you start, we recommend reviewing these key scripts and modules:

#### Task (BDDL file) generation and validation:
- `scripts/create_libero_task_example.py`
  - This file is an example to (1) define a scene in the scene class (2) define the task (3) generate bddl file for the task, which represents all necessary information of the task and will be used to set up the task.
- `scripts/collect_demonstration.py`
  - This file is used to teleoperate the robot to complete tasks. It is especially useful when you finish your task design and want to double-check the correctness of your reward code. We provide instructions in the later part.

#### Benchmark scene setup:
This file lists all scenes available in Libero. Each scene is defined as one separate class.
- `libero/libero/benchmark/mu_creation.py`

Predicate definition & Object-state specifications:
- `libero/libero/envs/base_predicates.py`
- `libero/libero/envs/__init__.py`
- `libero/libero/envs/object_states/base_object_states.py`

When designing tasks, feel free to use your imagination to extend or modify the code to achieve the desired effect, as long as the overall structure remains intact!

## Workflow Overview
1. Check the scene
   - First, consult the documentation to review the scene associated with your task. 
   - For a deeper dive, examine the implementation in `mu_creation.py` (You may design your own scenes afterwards!).
2. Implement the reward function
   - (If needed) Reference predefined object states in `base_object_states.py`.
   - (If needed) Define any custom predicates in `base_predicates.py` (and its `__init__.py`). Aim for reusable predicates, but one-offs are fine.
3. Generate the BDDL task file
   - Run your adapted `create_libero_task_example.py` to generate a BDDL task file under `/tmp/bddl/your-bddl-flie.bddl`.
4. Validate via teleoperation
   - Run collect_demonstration.py to ensure your task works as intended. You may try to use the following format:
   ```bash
   /path-to-your-collect_demonstration.py --bddl-file “/tmp/bddl/your-bddl-flie.bddl”--device keyboard --robots Panda
   ```

## A Concrete Example


 