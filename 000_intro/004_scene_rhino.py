from compas.colors import Color
from compas.geometry import Box
from compas.scene import Scene

box = Box(1)

# Rhino provides another visualisation context for scenes.
# When running this script in Rhino,
# the context is automatically detected.

scene = Scene()
scene.clear_context()
scene.add(box, facecolor=Color(1, 0, 0))

# print(scene)
scene.draw()
