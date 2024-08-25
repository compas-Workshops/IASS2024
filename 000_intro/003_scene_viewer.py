from compas.geometry import Box
from compas_viewer import Viewer

box = Box(1)

# The COMPAS Viewer provides a standalone visualisation context for scenes
# that is not dependent on any CAD software
# and can be used on Windows, Mac and Linux.

# A scene is automatically available as an attribute of a viewer instance.

viewer = Viewer()
viewer.scene.add(box)

# When the viewer is shown
# it will automatically draw the scene.
# There is no need to do this explicitly...

viewer.show()
