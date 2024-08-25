import pathlib

import compas
from compas.colors import Color
from compas.geometry import Box
from compas.geometry import Sphere
from compas_viewer import Viewer

box = Box(10)

mesh = box.to_mesh()

mesh.update_default_vertex_attributes(sphere=None)

for vertex in mesh.vertices():
    mesh.vertex_attribute(
        vertex,
        name="sphere",
        value=Sphere(radius=0.2, point=mesh.vertex_point(vertex)),
    )

subd = mesh.subdivided(k=3)

viewer = Viewer()
viewer.scene.add(subd)
for vertex in subd.vertices():
    sphere = subd.vertex_attribute(vertex, name="sphere")
    if sphere:
        sphere.frame.point = subd.vertex_point(vertex)
        viewer.scene.add(sphere, color=Color.red())
viewer.show()

# subd.to_json("subd.json")
session = {
    "box": box,
    "subd": subd,
}

compas.json_dump(session, pathlib.Path(__file__).parent / "session.json")
