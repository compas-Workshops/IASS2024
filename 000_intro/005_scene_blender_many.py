from random import random

from compas.colors import Color
from compas.geometry import Box
from compas.geometry import Pointcloud
from compas.scene import Scene

box = Box(1)

cloud = Pointcloud.from_box(Box(10, 10, 10), n=10)

# Blender provides another visualisation context for scenes.
# When running this script in Blender,
# the context is automatically detected.

# Note that there is no difference between a Rhino script and a Blender script...

scene = Scene()
scene.clear_context()

for point in cloud:
    scene.add(box.translated(point), color=Color.from_number(random()))

scene.draw()
