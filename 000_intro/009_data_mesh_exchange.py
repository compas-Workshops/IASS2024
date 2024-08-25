import compas
from compas.colors import Color
from compas.datastructures import Mesh
from compas.geometry import Sphere
from compas.scene import Scene

# session = compas.json_load("session.json")
session = compas.json_load("/Users/vanmelet/Workshops/IASS2024/000_intro/session.json")

subd: Mesh = session["subd"]

scene = Scene()
scene.clear_context()

scene.add(subd)

for vertex in subd.vertices():
    sphere: Sphere = subd.vertex_attribute(vertex, name="sphere")
    if sphere:
        sphere.frame.point = subd.vertex_point(vertex)
        scene.add(sphere, color=Color.red())

scene.draw()
