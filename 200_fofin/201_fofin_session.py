import pathlib
import compas
from compas.scene import Scene
from compas.datastructures import Mesh

session = compas.json_load(pathlib.Path(__file__).parent / "TexasShell.json")

# print(session)

scene = session["FormFinder.Scene"]

meshobj = scene.get_node_by_name(name="CableMesh")

constraints = meshobj.mesh.constraints
meshobj.mesh.constraints = {}

mesh = meshobj.mesh.copy(cls=Mesh)


print(mesh)

scene = Scene()
scene.clear_context()
scene.add(mesh.thickened(50, both=False), show_vertices=False, disjoint=True)
scene.draw()
