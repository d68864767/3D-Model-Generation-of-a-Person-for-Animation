```python
import bpy

# Load the scene setup
import scene_setup

# Load the character animation
import character_animation

# Set the start and end frames for the animation
bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = 60

# Set the output format to PNG
bpy.context.scene.render.image_settings.file_format = 'PNG'

# Set the output path
bpy.context.scene.render.filepath = "/path/to/output/directory/"

# Render the animation
bpy.ops.render.render(animation=True)
```
