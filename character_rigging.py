```python
import bpy

# Load the character model
bpy.ops.import_scene.obj(filepath="character_model.obj")

# Select the character model
character = bpy.data.objects['character_model']

# Create an armature for the character
bpy.ops.object.armature_add(location=character.location)
armature = bpy.context.object

# Parent the character to the armature
character.parent = armature

# Define the bones for the armature
bones = [
    ('Head', (0, 0, 1.7), (0, 0, 2)),
    ('Torso', (0, 0, 1), (0, 0, 1.7)),
    ('RightArm', (-0.5, 0, 1.5), (-0.5, 0, 1)),
    ('LeftArm', (0.5, 0, 1.5), (0.5, 0, 1)),
    ('RightLeg', (-0.2, 0, 1), (-0.2, 0, 0)),
    ('LeftLeg', (0.2, 0, 1), (0.2, 0, 0)),
]

# Add the bones to the armature
bpy.ops.object.mode_set(mode='EDIT')
for bone_name, bone_head, bone_tail in bones:
    bone = armature.data.edit_bones.new(bone_name)
    bone.head = bone_head
    bone.tail = bone_tail

# Switch back to object mode
bpy.ops.object.mode_set(mode='OBJECT')

# Create the rigging for the character
for bone_name in armature.data.bones.keys():
    # Create a vertex group for this bone
    group = character.vertex_groups.new(name=bone_name)
    
    # Assign vertices to the group based on proximity to the bone
    for vertex in character.data.vertices:
        distance = (armature.data.bones[bone_name].head - vertex.co).length
        if distance < 0.5:
            group.add([vertex.index], 1 - distance / 0.5, 'REPLACE')

    # Add a bone modifier to the character
    modifier = character.modifiers.new(name=bone_name, type='ARMATURE')
    modifier.object = armature
    modifier.use_bone_envelopes = False
    modifier.use_vertex_groups = True
```
