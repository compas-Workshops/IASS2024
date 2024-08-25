from compas.geometry import Box
from compas.scene import Scene

box = Box(1)

scene = Scene()
scene.add(box)

# Without a visualisation context,
# the scene cannot be drawn...

# scene.draw()

# However, you can still print out the hierarchy of objects
# in the scene tree.

print(scene)
