```python
import bpy

# Load the character model and rigging
bpy.ops.import_scene.obj(filepath="character_model.obj")
character = bpy.data.objects['character_model']
armature = bpy.data.objects['character_model'].parent

# Define the animation actions
actions = {
    'idle': [
        ('Head', [(0, 0, 0), (30, 0, 0), (60, 0, 0)]),
        ('Torso', [(0, 0, 0), (30, 0, 0), (60, 0, 0)]),
        ('RightArm', [(0, 0, 0), (30, -10, 0), (60, 0, 0)]),
        ('LeftArm', [(0, 0, 0), (30, 10, 0), (60, 0, 0)]),
        ('RightLeg', [(0, 0, 0), (30, 0, 0), (60, 0, 0)]),
        ('LeftLeg', [(0, 0, 0), (30, 0, 0), (60, 0, 0)]),
    ],
    'walk': [
        ('Head', [(0, 0, 0), (15, -5, 0), (30, 0, 0), (45, 5, 0), (60, 0, 0)]),
        ('Torso', [(0, 0, 0), (15, -5, 0), (30, 0, 0), (45, 5, 0), (60, 0, 0)]),
        ('RightArm', [(0, 0, 0), (15, -30, 0), (30, 0, 0), (45, 30, 0), (60, 0, 0)]),
        ('LeftArm', [(0, 0, 0), (15, 30, 0), (30, 0, 0), (45, -30, 0), (60, 0, 0)]),
        ('RightLeg', [(0, 0, 0), (15, 30, 0), (30, 0, 0), (45, -30, 0), (60, 0, 0)]),
        ('LeftLeg', [(0, 0, 0), (15, -30, 0), (30, 0, 0), (45, 30, 0), (60, 0, 0)]),
    ],
}

# Create the animations
for action_name, action_data in actions.items():
    # Create a new action
    bpy.ops.object.action_new(name=action_name)
    action = bpy.data.actions[action_name]

    # Add the keyframes to the action
    for bone_name, keyframes in action_data:
        for frame, rotation in enumerate(keyframes):
            # Select the bone
            bpy.context.object.data.bones.active = bpy.context.object.data.bones[bone_name]

            # Set the pose rotation
            bpy.context.object.pose.bones[bone_name].rotation_euler = rotation

            # Insert a keyframe for the pose rotation
            bpy.ops.anim.keyframe_insert_menu(type='Rotation')

            # Move to the next frame
            bpy.context.scene.frame_set(frame + 1)

    # Link the action to the armature
    armature.animation_data.action = action
```
