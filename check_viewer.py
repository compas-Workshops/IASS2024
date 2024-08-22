from compas.geometry import Box
from compas_viewer import Viewer

# Create a box.
box = Box(1, 1, 1)

# Vizualize geometry.
viewer = Viewer()
viewer.scene.add(box)
viewer.show()
