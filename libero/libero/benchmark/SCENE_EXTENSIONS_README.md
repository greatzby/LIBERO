# Scene Extension Summary

This document summarizes the extended scene classes created for cross-type scene variations in the LIBERO benchmark.

## Overview

All existing scene types have been expanded to create cross-type variations by replacing the table type and updating corresponding region names. Each extended scene inherits from the original class to save code and follows the naming convention `{OriginalSceneName}{NewType}`.

## Files Created

### 1. kitchen_scenes_extended.py
Contains Kitchen scenes extended to other scene types:

**Kitchen → Living Room (10 scenes):**
- KitchenScene1LivingRoom to KitchenScene10LivingRoom
- Table type: kitchen_table → living_room_table
- Workspace name: kitchen_table → living_room_table

**Kitchen → Study (10 scenes):**
- KitchenScene1Study to KitchenScene10Study
- Table type: kitchen_table → study_table
- Workspace name: kitchen_table → study_table

**Kitchen → Tabletop Manipulation (10 scenes):**
- KitchenScene1TabletopManipulation to KitchenScene10TabletopManipulation
- Table type: kitchen_table → table
- Workspace name: kitchen_table → main_table

### 2. living_room_scenes_extended.py
Contains Living Room scenes extended to other scene types:

**Living Room → Kitchen (6 scenes):**
- LivingRoomScene1Kitchen to LivingRoomScene6Kitchen
- Table type: living_room_table → kitchen_table
- Workspace name: living_room_table → kitchen_table

**Living Room → Study (6 scenes):**
- LivingRoomScene1Study to LivingRoomScene6Study
- Table type: living_room_table → study_table
- Workspace name: living_room_table → study_table

**Living Room → Tabletop Manipulation (6 scenes):**
- LivingRoomScene1TabletopManipulation to LivingRoomScene6TabletopManipulation
- Table type: living_room_table → table
- Workspace name: living_room_table → main_table

### 3. study_scenes_extended.py
Contains Study scenes extended to other scene types:

**Study → Kitchen (4 scenes):**
- StudyScene1Kitchen to StudyScene4Kitchen
- Table type: study_table → kitchen_table
- Workspace name: study_table → kitchen_table

**Study → Living Room (4 scenes):**
- StudyScene1LivingRoom to StudyScene4LivingRoom
- Table type: study_table → living_room_table
- Workspace name: study_table → living_room_table

**Study → Tabletop Manipulation (4 scenes):**
- StudyScene1TabletopManipulation to StudyScene4TabletopManipulation
- Table type: study_table → table
- Workspace name: study_table → main_table

### 4. tabletop_scenes_extended.py
Contains Tabletop Manipulation scenes extended to other scene types:

**Tabletop Manipulation → Kitchen (1 scene):**
- TabletopScene1Kitchen
- Table type: table → kitchen_table
- Workspace name: main_table → kitchen_table

**Tabletop Manipulation → Living Room (1 scene):**
- TabletopScene1LivingRoom
- Table type: table → living_room_table
- Workspace name: main_table → living_room_table

**Tabletop Manipulation → Study (1 scene):**
- TabletopScene1Study
- Table type: table → study_table
- Workspace name: main_table → study_table

## Implementation Details

### Class Structure
Each extended scene class:
1. Inherits from the original scene class
2. Updates `fixture_num_info` to replace table types
3. Updates `workspace_name` to match the new scene type
4. Overrides `define_regions()` to update region names
5. Overrides `init_states` property to update region references

### Table Type Mappings
- **Kitchen**: kitchen_table
- **Living Room**: living_room_table
- **Study**: study_table
- **Tabletop Manipulation**: table (fixture), main_table (workspace)

### Region Name Updates
All region names are automatically updated to use the new workspace name prefix:
- `kitchen_table_*` → `living_room_table_*` (Kitchen → Living Room)
- `living_room_table_*` → `study_table_*` (Living Room → Study)
- `main_table_*` → `kitchen_table_*` (Tabletop → Kitchen)
- etc.

## Total Extended Scenes Created

| Original Type | Extended To | Count | Total |
|---------------|-------------|-------|-------|
| Kitchen (10)  | Living Room | 10    | 30    |
|               | Study       | 10    |       |
|               | Tabletop    | 10    |       |
| Living Room (6) | Kitchen   | 6     | 18    |
|               | Study       | 6     |       |
|               | Tabletop    | 6     |       |
| Study (4)     | Kitchen     | 4     | 12    |
|               | Living Room | 4     |       |
|               | Tabletop    | 4     |       |
| Tabletop (1)  | Kitchen     | 1     | 3     |
|               | Living Room | 1     |       |
|               | Study       | 1     |       |

**Total Extended Scenes: 63**

## Usage

To use these extended scenes, import the appropriate file and register the scenes:

```python
# Example usage
from libero.libero.benchmark.kitchen_scenes_extended import *
from libero.libero.benchmark.living_room_scenes_extended import *
from libero.libero.benchmark.study_scenes_extended import *
from libero.libero.benchmark.tabletop_scenes_extended import *
```

Each scene is automatically registered with the appropriate scene type using the `@register_mu` decorator.
