import pathlib

import compas
from compas.colors import Color
from compas.datastructures import Mesh
from compas.geometry import Sphere
from compas.scene import Scene

session = compas.json_load(pathlib.Path(__file__).parent / "session.json")

subd: Mesh = session["subd"]

scene = Scene()
scene.clear()

scene.add(subd)

for vertex in subd.vertices():
    sphere: Sphere = subd.vertex_attribute(vertex, name="sphere")
    if sphere:
        sphere.frame.point = subd.vertex_point(vertex)
        scene.add(sphere, color=Color.red())

session["scene"] = scene

compas.json_dump(session, pathlib.Path(__file__).parent / "scenesession.json")
